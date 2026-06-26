#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$PLIST_DIR/com.adobe.crawler.monthly.plist"

mkdir -p "$PLIST_DIR"

cat > "$PLIST_FILE" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.adobe.crawler.monthly</string>

  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${SCRIPT_DIR}/monthly_crawler_pipeline.sh</string>
  </array>

  <key>StartCalendarInterval</key>
  <dict>
    <key>Day</key>
    <integer>1</integer>
    <key>Hour</key>
    <integer>7</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>

  <key>StandardOutPath</key>
  <string>${SCRIPT_DIR}/monthly_crawler.out.log</string>
  <key>StandardErrorPath</key>
  <string>${SCRIPT_DIR}/monthly_crawler.err.log</string>

  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
PLIST

launchctl bootout "gui/$UID" "$PLIST_FILE" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$UID" "$PLIST_FILE"
launchctl enable "gui/$UID/com.adobe.crawler.monthly"

printf 'Installed: %s\n' "$PLIST_FILE"
printf 'Scripts directory: %s\n' "$SCRIPT_DIR"
