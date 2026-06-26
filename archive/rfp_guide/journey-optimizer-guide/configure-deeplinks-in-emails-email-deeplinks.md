---
title: "Configure deeplinks in emails email-deeplinks"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/configure-email/deeplinks"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:27.589793+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Configure deeplinks in emails email-deeplinks

Last update: May 12, 2026
- Topics:
- [Email](#)

CREATED FOR:

- Intermediate
- User
- Developer

Deeplinks in emails help you take recipients from an email to a specific screen or piece of content in your mobile app. It helps bring people straight to the intended in-app experience, without routing them through a web browser or an app store, so the journey stays relevant and on-brand.

To add a deeplink to an email, make sure [link tracking is enabled](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/message-tracking#enable-tracking). Select the element you want to link (text, button, or image) in the Email Designer, click **Insert link** in the contextual toolbar, and choose **Deeplink** to enter your deeplink URL. [Learn more on inserting links](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/message-tracking#insert-links)

When your recipients click the deeplink, they are taken directly to the intended in-app content - **provided you have completed the configuration steps** detailed on this page, which covers:

- How to configure deeplinks for emails in Journey Optimizer
- How to implement deeplink handling for iOS and Android in your mobile app

NOTE
Adobe Journey Optimizer supports deeplinking for both iOS and Android using tracked URLs (
/ee/v1/mclick/*
) to ensure compatibility and click tracking.
## Configuration in Journey Optimizer configuration

To be able to use deeplinks in emails for your mobile apps, complete the configuration steps below.

NOTE
This section applies when you use
universal links (iOS)
and
app links (Android)
(HTTPS-based deeplinks).
- In Journey Optimizer, delegate the subdomain where deeplinking is enabled. Learn more
- Host the AASA file for iOS and the assetLinks.json file for Android on your subdomain. Contact Adobe Customer Care or your Adobe representative with the details below: For iOS (AASA) : Delegated subdomain App bundle ID For Android (assetLinks.json) : Delegated subdomain App bundle ID SHA-256 certificate fingerprint

IMPORTANT
Deeplinking through Adobe email infrastructure applies when
link tracking is enabled
. Tracked deeplink clicks use URLs under
/ee/v1/mclick/*
, which Adobe hosts and resolves.
For
non-tracked
links, the URL is not rewritten through Adobe systems. You must configure universal links or app links on your own domains and hosting so those links open your app as intended.
## Mobile app implementation mobile-implementation

This section explains how to implement mobile deeplinks with Adobe Journey Optimizer so that, in a typical **HTTPS** setup (universal links and app links), a single URL can:

- Open a specific screen inside your mobile app when the app is installed, or
- Open your website as a fallback when the app is not installed.

When [link tracking is enabled](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/message-tracking#enable-tracking) for your message, Journey Optimizer continues to track these clicks, includes them in reporting, and can use them in [content experiments](/en/docs/journey-optimizer/using/content-management/content-experiment/content-experiment) if you run them on the message.

This section provides common implementation patterns for deeplinks. Your exact setup depends on your app architecture and routing framework.

### iOS (Universal Links) ios-implementation

- In Xcode, select your target through Signing & Capabilities > + Capability > Associated Domains .
- Add entries for your delegated subdomains, for example: code language-text applinks:www.mybusiness.com applinks:data.email.mybusiness.com
- Handle Universal Links in the app and get the original link from the response header. accordion Example: iOS 13+ with scenes code language-swift class SceneDelegate: UIResponder, UIWindowSceneDelegate { func scene(_ scene: UIScene, continue userActivity: NSUserActivity) { guard userActivity.activityType == NSUserActivityTypeBrowsingWeb, let incomingURL = userActivity.webpageURL else { return } handleUniversalLink(url: incomingURL) } private func handleUniversalLink(url: URL) { // Only handle AJO tracked mobile clicks guard url.host == "data.email.mybusiness.com", url.path.hasPrefix("/ee/v1/mclick") else { // Could also handle direct www.mybusiness.com links here return } resolveTrackedUrlAndRoute(url) } private func resolveTrackedUrlAndRoute(_ trackedUrl: URL) { var request = URLRequest(url: trackedUrl) request.httpMethod = "GET" URLSession.shared.dataTask(with: request) { _, response, error in guard error == nil, let httpResponse = response as? HTTPURLResponse, let locationValue = httpResponse.allHeaderFields["Location"] as? String, let finalUrl = URL(string: locationValue) else { return } DispatchQueue.main.async { self.routeToDestination(finalUrl) } }.resume() } private func routeToDestination(_ url: URL) { // Example: map URL paths to screens // https://www.mybusiness.com/dashboard/offers/coupons // → OffersViewController for Coupons } }

IMPORTANT
The app must perform a
GET
on the
mclick
URL and read the
Location
header, then route based on the
final
URL.
Do not simply open the
mclick
URL in Safari; that defeats the purpose of deeplinking.
### Android (App Links) android-implementation

- Add App Link intent filter in your Android app. code language-xml <activity android:name=".DeepLinkActivity" android:exported="true"> <intent-filter android:autoVerify="true"> <action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> <data android:scheme="https" android:host="data.email.mybusiness.com" android:pathPrefix="/ee/v1/mclick" /> </intent-filter> </activity>
- Implement the deep link handler. accordion In Kotlin: code language-kotlin class DeepLinkActivity : AppCompatActivity() { override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState) val trackedUri = intent?.data if (trackedUri == null || trackedUri.host != "data.email.mybusiness.com" || !trackedUri.path.orEmpty().startsWith("/ee/v1/mclick")) { finish() return } resolveTrackedUrlAndRoute(trackedUri) } private fun resolveTrackedUrlAndRoute(trackedUri: Uri) { lifecycleScope.launch(Dispatchers.IO) { try { val finalUrl = followRedirect(trackedUri.toString()) withContext(Dispatchers.Main) { routeToDestination(finalUrl) finish() } } catch (e: Exception) { // Optionally log error, fallback to browser finish() } } } private fun followRedirect(trackedUrl: String): Uri { val client = OkHttpClient.Builder() .followRedirects(false) // We want to read Location ourselves .build() val request = Request.Builder() .url(trackedUrl) .get() .build() client.newCall(request).execute().use { response -> val location = response.header("Location") ?: throw IllegalStateException("Missing Location header") return Uri.parse(location) } } private fun routeToDestination(finalUri: Uri) { // Example: interpret https://www.mybusiness.com/dashboard/offers/coupons // and open the correct Activity / Fragment } }

IMPORTANT
Like iOS, the app must call the
mclick
URL and use the
Location
header to determine the final destination.
Use
followRedirects(false)
so you control redirect handling and can log analytics accurately if needed.
Routing logic is app‑specific; define a clear mapping from URLs to screens.
## Recommended practices deeplink-best-practices

- **Use stable paths**: Prefer routes that are resilient to app UI changes (for example /account/orders instead of /tab/3/view/2).
- **Account for tracked paths**: When link tracking is enabled, the clicked link may use tracked path patterns (for example /ee/v1/mclick/). Make sure your router can parse the final URL after resolving the tracked link.
- **Keep parameters predictable**: Define a consistent parameter scheme (for example ?orderId=12345).
- **Avoid sensitive data in URLs**: Do not put secrets or personal data directly into the deeplink URL.
- **Test your deeplink**: Send a proof and click the deeplink on a device where the app is installed.
- **Validate on real devices**: Universal links and tracked-link resolution behaviors are more reliable to validate on physical devices rather than simulators.
- **Validate the app-side routing**: If the deeplink does not open the expected screen, validate the app-side routing and the URL format (host/path/query and URL encoding).
- **Keep app initialization in mind**: App Links / Universal Links behavior is most reliable after the app has been installed and opened at least once.

## Troubleshooting and FAQ troubleshooting-faq

The app doesn't open when I tap the deeplink.
- Verify the URL matches the host and path patterns your app is registered to handle, including tracked click paths when link tracking is enabled (for example paths under /ee/v1/mclick/).
- For iOS universal links and Android app links, confirm domain association (AASA / assetlinks.json) is correctly configured and reachable.
- Test on a real device (simulators/emulators can behave differently for link association).

The app opens but doesn't navigate to the expected screen.
- Confirm the app-side router correctly parses the URL path/query.
- Check URL encoding: reserved characters should be URL-encoded.
- Validate parameter names and values match what the router expects.

What happens if the app is not installed?
- If the same HTTPS URL can be served by your website, the link can open a web page as a fallback when the app is not installed (configure your web destination and routing accordingly).

How do I safely include special characters in parameters?
URL-encode query parameter values. This reduces delivery and rendering issues and helps prevent parsing errors in your app.
How should we test end-to-end?
- Create a proof with a deeplink, click it on iOS and Android devices (installed and not installed scenarios).
- Validate: The final email link value (host/path/query) The OS-level association (if using universal links / app links) The in-app routing outcome

I have one app but different subdomains for the organization. Should I request AASA and assetLinks.json to be created for each subdomain?
Yes. If you want deeplinking on every delegated subdomain, request AASA and
assetlinks.json
configuration for each subdomain that should support the feature.
Should the URL I configure use a deeplinking format (for example
appname://path
)?
You can use a custom URL scheme (for example
appname://path
), but the recommended approach is a universal link or app link (
https://
), which matches the HTTPS-based setup in the configuration and implementation sections on this page.
Will UTM parameters on the URL be available in the mobile app for analytics?
Yes. UTM parameters you configure in Journey Optimizer are included in the final URL returned in the
Location
header when your app performs a GET on the
mclick
URL, so you can use them for in-app analytics.
What is the user experience for
/ee/v1/click/
URLs?
The link opens in the device’s default web browser (standard click tracking behavior), rather than being handled as an app deep link through the
mclick
flow described on this page.
recommendation-more-help
