#!/usr/bin/env python3
"""
Adobe Journey Optimizer B2B (AJO B2B) — Knowledge Builder

O que faz:
- Rastreia a documentação do Adobe Journey Optimizer B2B Edition a partir de URLs iniciais
- Mantém apenas links internos de documentação sob o caminho do AJO B2B
- Extrai o conteúdo principal do artigo e converte para Markdown
- Organiza a saída por categoria (guides/tutorials/reference/release-notes/overview/other)
- Escreve um arquivo .md por página ou subseção H2
- Cria um README.md de índice e um manifest.json para publicação downstream

Cobre os dois guias da doc: Ultimate (user) e Prime (prime).

Instalação sugerida:
    pip install requests beautifulsoup4

Exemplo:
    python ajob2b_crawler.py \
        --output-dir "./ajob2b_guides" \
        --max-pages 300 \
        --split-h2 \
        --only guides tutorials reference overview
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
ALLOWED_PREFIXES = [
    "/en/docs/journey-optimizer-b2b",
    "/legal/product-descriptions",
]
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Safari/605.1.15"
    )
}

CATEGORY_MAP = {
    "overview": "overview",
    "landing": "overview",
    "home": "overview",
    "vis\u00e3o geral": "overview",
    "guias": "guides",
    "guia": "guides",
    "guides": "guides",
    "guide": "guides",
    "tutoriais": "tutorials",
    "tutorial": "tutorials",
    "tutorials": "tutorials",
    "reference": "reference",
    "api": "reference",
    "apis": "reference",
    "refer\u00eancia": "reference",
    "recursos relacionados": "reference",
    "related resources": "reference",
    "release notes": "release-notes",
    "release-notes": "release-notes",
    "informa\u00e7\u00f5es da vers\u00e3o": "release-notes",
    "novidades": "release-notes",
    "what's new": "release-notes",
}

GENERIC_TOPICS = {
    "documenta\u00e7\u00e3o",
    "documentation",
    "journey optimizer b2b",
    "adobe journey optimizer b2b",
    "journey optimizer b2b edition",
    "adobe journey optimizer b2b edition",
}

ALLOWED_DEFAULT = ["guides", "tutorials", "reference", "overview"]

DEFAULT_START_URLS = [
    # ---- Guia Ultimate (user) ----
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/guide-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/release-notes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/about-journey-optimizer-b2b-edition",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/setup-ultimate",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/namespaces-schemas",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/xdm-field-management",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/configure-aep-events",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/branding-domains",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/email-protocols",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/email-setup",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/marketo-actions-connect",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/admin-setup/user-management",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/get-started",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/get-started/home-page",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/ai-assistant-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/enable-ai-assistant-access",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/question-guidance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/use-ai-assistant",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/generative-ai-content",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/ai-agents/audience-agent-b2b",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/ai-agents/journey-agent",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/ai-assistant/ai-agents/sales-qualifier",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journeys-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/create-publish-journey",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-re-entry",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/account-audience-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/person-audience-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/action-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/listen-for-event-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/split-merge-paths-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/variant-split-paths-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/next-best-path-node",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/wait-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-nodes/external-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journeys/journey-details",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/sms-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/whatsapp-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/add-email",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-send-time-optimization",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/ai-assistant-emails",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/genstudio-email-workflow",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-dark-mode",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-authoring-governance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/sales-alert-email",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-deduplication",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/email-channel/email-tracking-manage",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/web-channel/web-experiences",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/web-channel/web-experience-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/web-channel/web-single-page-applications",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/personalization-my-tokens",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/journey-content/channels-consent-preferences",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/audiences/account-audience-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/audiences/target-external-audience",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/audiences/linkedin-account-matched-audiences",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/audiences/field-mapping",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/audiences/test-profiles",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/buying-groups-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/solution-interests",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/buying-groups-role-templates",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/default-custom-roles",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/buying-group-role-insights",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/scoring/engagement-scores",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/scoring/completeness-scores",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/buying-group-stages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/buying-groups-create",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/account-list-export",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/marketo-engage-smart-list-buying-group-filters",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/buying-groups/incrm-insights",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/account-lists/account-lists",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/account-lists/account-lists-journeys",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/sales-experience/account-details",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/sales-experience/buying-group-details",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/sales-experience/person-details",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/accounts/sales-experience/crm-linking",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/emails/emails-list",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/emails/preview/email-simulate-content",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/emails/preview/email-test-rendering",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/emails/preview/email-spam-report",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/emails/email-collaboration-tools",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/assets/assets-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/assets/internal-dam/internal-image-assets",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/assets/internal-dam/image-edit-adobe-express",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/assets/aem-assets",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/template-content-governance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/email-templates/email-templates",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/email-templates/email-template-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/email-templates/email-template-advanced-html",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/email-templates/email-template-image-convert",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/landing-page-templates/landing-page-templates",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/templates/landing-page-templates/landing-page-template-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/visual-fragments/fragments",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/visual-fragments/fragment-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/forms/forms",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/forms/form-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/landing-pages/landing-pages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/landing-pages/landing-pages-create-publish",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/landing-pages/landing-page-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/landing-pages/ai-assistant-landing-pages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/content-design/structure-components",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/content-design/content-components",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/content-design/design-custom-css",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/brands/brands-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/brands/brands-manage-create",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/brands/generative-ai-models",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/brand-themes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/content-evaluation",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/conditional-content",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/accessible-content",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/personalization/personalization",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/personalization/personalization-syntax",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/content-management/personalization/personalization-helper-functions",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/intelligent-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/engagement-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/web-engagement-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/email-performance-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/buying-groups-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/dashboards/journeys-dashboard",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/governance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/persona-mapping",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/configurations/configure-aem-repositories",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/configurations/intent-data",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/configurations/engagement-score-weighting",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/configurations/configure-external-actions",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/configurations/aep-event-collection",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-emails",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-sms",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-whatsapp",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-web",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-landing-pages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/user/admin/channels/configure-channels-forms",
    # ---- Guia Prime (prime) ----
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/guide-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/start/setup-prime",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/start/user-management",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/start/email-deliverability",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/home-page",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/chat-interface",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/skills",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/program-from-brief",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/audience-creation",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/lead-scoring-model",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/marketing-management",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/programs/programs",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/programs/personalization-my-tokens",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/person-journeys",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/person-journey-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/person-audience-node",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/action-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/listen-for-event-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/wait-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/split-merge-paths-nodes",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/journey-nodes/next-best-path",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/email-channel/email-channel",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/email-channel/email-send-time-optimization",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/email-channel/email-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/email-channel/email-dark-mode",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/marketing-management/whatsapp-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/journey-traffic-control",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/people-lists",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/person-details",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/event-based-audiences",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/engagement-scores",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/personas",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/audiences/destinations",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/digital-asset-management",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/templates/templates",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/templates/templates-create",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/templates/template-content-governance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/visual-fragments/fragments",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/visual-fragments/fragment-authoring",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/landing-pages/landing-pages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/landing-pages/landing-pages-create-publish",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/landing-pages/landing-page-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/forms/forms",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/forms/form-design",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/personalization-expressions",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/conditional-content",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/content-design/structure-components",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/content-design/content-components",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/content/content-design/design-custom-css",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/channels/email-channel-configuration",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/channels/configuration-channels-whatsapp",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/channels/configuration-presets-landing-pages",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/channels/configuration-presets-forms",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/business-rules",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/program-types",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/sales-qualifier",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/admin/persona-mapping",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/ai-assistant-overview",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/enable-ai-assistant-access",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/question-guidance",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/use-ai-assistant",
    "https://experienceleague.adobe.com/en/docs/journey-optimizer-b2b/prime/ai-assistant/generative-ai-content",
    # ---- Product Description ----
    "https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer-b2b.html",
]


@dataclass
class Page:
    url: str
    title: str
    category: str
    topic_path: str
    content_md: str
    breadcrumbs: List[str]
    section_slug: Optional[str] = None


# ----------------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = unescape(text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


def normalize_url(base_url: str, href: str) -> Optional[str]:
    if not href:
        return None

    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:")):
        return None

    abs_url = urljoin(base_url, href)
    abs_url, _frag = urldefrag(abs_url)
    parsed = urlparse(abs_url)

    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc not in ALLOWED_DOMAINS:
        return None
    if not any(parsed.path.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        return None

    return abs_url


def is_doc_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.path.endswith(
        (".pdf", ".zip", ".png", ".jpg", ".jpeg", ".svg")
    ):
        return False
    return any(
        parsed.path.startswith(prefix)
        for prefix in ALLOWED_PREFIXES
    )


def fetch(url: str, session: requests.Session, delay_s: float = 0.0) -> str:
    if delay_s:
        time.sleep(delay_s)
    resp = session.get(url, headers=DEFAULT_HEADERS, timeout=120)
    resp.raise_for_status()
    return resp.text


# ----------------------------------------------------------------------------
# HTML extraction
# ----------------------------------------------------------------------------

def extract_title(soup: BeautifulSoup) -> str:
    h1 = soup.select_one("h1")
    if h1 and h1.get_text(" ", strip=True):
        return h1.get_text(" ", strip=True)

    og = soup.select_one('meta[property="og:title"]')
    if og and og.get("content"):
        return og["content"].strip()

    title = soup.select_one("title")
    if title and title.get_text(" ", strip=True):
        return title.get_text(" ", strip=True)

    return "untitled"


def extract_breadcrumbs(soup: BeautifulSoup) -> List[str]:
    selectors = [
        'nav[aria-label*="breadcrumb"] a',
        'nav[aria-label*="Breadcrumb"] a',
        ".breadcrumb a",
        '[class*="breadcrumb"] a',
    ]
    crumbs: List[str] = []
    for sel in selectors:
        nodes = soup.select(sel)
        if nodes:
            for n in nodes:
                txt = n.get_text(" ", strip=True)
                if txt:
                    crumbs.append(txt)
            break

    deduped = []
    seen = set()
    for c in crumbs:
        key = c.lower()
        if key not in seen:
            deduped.append(c)
            seen.add(key)
    return deduped


def pick_main_container(soup: BeautifulSoup) -> Tag:
    for sel in ["main", "article", '[role="main"]', ".content", ".article", ".markdown"]:
        node = soup.select_one(sel)
        if node:
            return node
    return soup.body or soup


def remove_noise(root: Tag) -> None:
    for tag_name in ["script", "style", "nav", "footer", "header", "aside", "form", "noscript"]:
        for node in root.find_all(tag_name):
            node.decompose()

    for cls in ["cookie", "breadcrumb", "sidebar", "toc", "feedback"]:
        for node in root.find_all(class_=re.compile(cls, re.I)):
            try:
                node.decompose()
            except Exception:
                pass


def inline_text(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        return unescape(str(node))

    pieces: List[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(unescape(str(child)))
        elif isinstance(child, Tag):
            if child.name == "a":
                text = child.get_text(" ", strip=True)
                href = child.get("href", "").strip()
                pieces.append(f"[{text}]({href})" if href and text else text)
            elif child.name in {"strong", "b"}:
                pieces.append(f"**{child.get_text(' ', strip=True)}**")
            elif child.name in {"em", "i"}:
                pieces.append(f"*{child.get_text(' ', strip=True)}*")
            else:
                pieces.append(child.get_text(" ", strip=True))
    return re.sub(r"\s+", " ", "".join(pieces)).strip()


def node_to_markdown(node: Tag | NavigableString) -> str:
    out: List[str] = []

    def walk(n: Tag | NavigableString):
        if isinstance(n, NavigableString):
            txt = unescape(str(n)).strip()
            if txt:
                out.append(txt)
            return
        if not isinstance(n, Tag):
            return

        name = n.name.lower()

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(name[1])
            text = n.get_text(" ", strip=True)
            if text:
                out.append(f"{'#' * level} {text}")
                out.append("")
            return

        if name == "p":
            text = inline_text(n)
            if text:
                out.append(text)
                out.append("")
            return

        if name in {"ul", "ol"}:
            for li in n.find_all("li", recursive=False):
                li_text = inline_text(li)
                if li_text:
                    out.append(f"- {li_text}")
            out.append("")
            return

        if name == "pre":
            code = n.get_text("\n", strip=False).rstrip()
            out.append("```")
            out.append(code)
            out.append("```")
            out.append("")
            return

        if name == "table":
            rows = []
            for tr in n.find_all("tr"):
                cells = [inline_text(td) for td in tr.find_all(["th", "td"])]
                if any(cells):
                    rows.append(cells)
            if rows:
                header = rows[0]
                out.append("| " + " | ".join(header) + " |")
                out.append("| " + " | ".join(["---"] * len(header)) + " |")
                for row in rows[1:]:
                    padded = row + [""] * (len(header) - len(row))
                    out.append("| " + " | ".join(padded) + " |")
                out.append("")
            return

        for child in n.children:
            walk(child)

    walk(node)
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md + "\n"


def split_by_h2(main: Tag) -> List[Tuple[str, str]]:
    children = list(main.children)
    sections: List[Tuple[str, str]] = []

    current_title = "main"
    buffer: List[str] = []

    def flush():
        nonlocal buffer, current_title
        html = "".join(buffer).strip()
        if html:
            sections.append((current_title, html))
        buffer = []

    for child in children:
        if isinstance(child, NavigableString):
            if str(child).strip():
                buffer.append(str(child))
            continue

        if not isinstance(child, Tag):
            continue

        if child.name == "h2":
            flush()
            current_title = child.get_text(" ", strip=True) or "section"
            buffer.append(str(child))
        else:
            buffer.append(str(child))

    flush()
    return sections


# ----------------------------------------------------------------------------
# Metadata inference
# ----------------------------------------------------------------------------

def infer_category_from_url_or_breadcrumbs(url: str, breadcrumbs: List[str]) -> str:
    for crumb in breadcrumbs:
        k = slugify(crumb)
        if k in CATEGORY_MAP:
            return CATEGORY_MAP[k]

    path = urlparse(url).path.lower()
    if "tutorial" in path:
        return "tutorials"
    if "release" in path or "version" in path or "notes" in path:
        return "release-notes"
    if "guide" in path:
        return "guides"
    if "reference" in path or "/api" in path:
        return "reference"
    # Paginas conceituais de governanca/privacidade/consentimento sao guias.
    if "consent" in path or "privacy" in path or "governance" in path:
        return "guides"
    # /home e /overview sao visoes gerais.
    return "overview" if path.endswith(("/home", "/home-page", "/overview", "/guide-overview")) else "other"


def infer_topic_path(url: str, breadcrumbs: List[str], title: str) -> str:
    crumbs = [slugify(c) for c in breadcrumbs if slugify(c) not in GENERIC_TOPICS]
    if len(crumbs) >= 2:
        return "/".join(crumbs[:4])

    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    try:
        idx = parts.index("journey-optimizer-b2b")
        tail = parts[idx + 1 :]
    except ValueError:
        tail = parts

    tail = [slugify(p) for p in tail if p and p not in {"en", "docs", "journey-optimizer-b2b"}]
    if tail:
        return "/".join(tail[:4])

    return slugify(title)


# ----------------------------------------------------------------------------
# Page extraction / saving
# ----------------------------------------------------------------------------

def extract_page(url: str, html: str, split_h2_enabled: bool = False) -> List[Page]:
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    breadcrumbs = extract_breadcrumbs(soup)
    category = infer_category_from_url_or_breadcrumbs(url, breadcrumbs)

    main = pick_main_container(soup)
    remove_noise(main)

    pages: List[Page] = []

    if split_h2_enabled:
        sections = split_by_h2(main)
        if len(sections) > 1:
            for section_title, section_html in sections:
                section_soup = BeautifulSoup(section_html, "html.parser")
                md = node_to_markdown(section_soup)
                pages.append(
                    Page(
                        url=url,
                        title=title,
                        category=category,
                        topic_path=infer_topic_path(url, breadcrumbs, title),
                        content_md=md,
                        breadcrumbs=breadcrumbs,
                        section_slug=slugify(section_title),
                    )
                )
            return pages

    md = node_to_markdown(main)
    pages.append(
        Page(
            url=url,
            title=title,
            category=category,
            topic_path=infer_topic_path(url, breadcrumbs, title),
            content_md=md,
            breadcrumbs=breadcrumbs,
            section_slug=None,
        )
    )
    return pages


def friendly_filename(title: str, section_slug: Optional[str] = None) -> str:
    base = slugify(section_slug or title)
    if base == "untitled":
        base = "page"
    return base


def save_page(page: Page, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    base = friendly_filename(page.title, page.section_slug)
    target = output_dir / f"{base}.md"

    n = 2
    while target.exists():
        target = output_dir / f"{base}-{n}.md"
        n += 1

    front_matter = [
        "---",
        f'title: "{page.title}"',
        f'url: "{page.url}"',
        f'category: "{page.category}"',
        f'topic: "{page.topic_path}"',
        f'created_at: "{datetime.now(timezone.utc).isoformat()}"',
        "---",
        "",
    ]

    body = ""
    if page.breadcrumbs:
        body += "Breadcrumbs: " + " > ".join(page.breadcrumbs) + "\n\n"
    body += page.content_md.strip() + "\n"

    target.write_text("\n".join(front_matter) + body, encoding="utf-8")
    return target


# ----------------------------------------------------------------------------
# Crawling / indexing
# ----------------------------------------------------------------------------

def extract_links_with_context(soup: BeautifulSoup, base_url: str) -> List[Tuple[str, str]]:
    result: List[Tuple[str, str]] = []
    current_section = ""

    for node in soup.find_all(["h2", "h3", "a"]):
        if node.name in {"h2", "h3"}:
            current_section = node.get_text(" ", strip=True)
            continue

        if node.name == "a":
            href = node.get("href")
            url = normalize_url(base_url, href or "")
            if url and is_doc_url(url):
                result.append((url, current_section))

    deduped = []
    seen = set()
    for url, ctx in result:
        if url not in seen:
            deduped.append((url, ctx))
            seen.add(url)
    return deduped


def category_from_section_context(section_context: str) -> Optional[str]:
    key = slugify(section_context)
    return CATEGORY_MAP.get(key)


def build_readme(output_dir: Path, manifest: List[dict]) -> None:
    lines: List[str] = []
    lines.append("# Journey Optimizer B2B Knowledge Index")
    lines.append("")
    lines.append("Gerado a partir da documentacao do Adobe Journey Optimizer B2B Edition.")
    lines.append("")
    lines.append("## Files")
    lines.append("")

    for item in manifest:
        if item.get("status") != "saved":
            continue
        filename = Path(item["saved_path"]).name
        lines.append(f"- {filename} - {item['url']}")

    (output_dir / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def crawl(
    start_urls: List[str],
    output_dir: Path,
    max_pages: int = 300,
    split_h2_enabled: bool = False,
    delay_s: float = 0.0,
    only_categories: Optional[List[str]] = None,
) -> None:
    session = requests.Session()
    queue = deque((url, None) for url in start_urls)
    visited = set()
    manifest: List[dict] = []
    saved_count = 0

    allowed = set(only_categories) if only_categories else None

    while queue and saved_count < max_pages:
        url, forced_category = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            html = fetch(url, session, delay_s=delay_s)
        except Exception as e:
            manifest.append({"url": url, "status": "error", "error": str(e)})
            continue

        pages = extract_page(url, html, split_h2_enabled=split_h2_enabled)

        for page in pages:
            if forced_category:
                page.category = forced_category

            if allowed is not None and page.category not in allowed:
                continue

            saved_path = save_page(page, output_dir)
            manifest.append(
                {
                    "url": page.url,
                    "title": page.title,
                    "category": page.category,
                    "topic_path": page.topic_path,
                    "section_slug": page.section_slug,
                    "saved_path": str(saved_path),
                    "status": "saved",
                }
            )
            saved_count += 1
            if saved_count >= max_pages:
                break

        soup = BeautifulSoup(html, "html.parser")
        main = pick_main_container(soup)
        remove_noise(main)
        main_links = extract_links_with_context(main, url)
        queued_urls = {item[0] for item in queue}
        for link_url, section_ctx in main_links:
            if link_url in visited or link_url in queued_urls:
                continue
            category = category_from_section_context(section_ctx)
            queue.append((link_url, category))
            queued_urls.add(link_url)

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    build_readme(output_dir, manifest)


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawler do Adobe Journey Optimizer B2B para Markdown organizado por topico"
    )
    parser.add_argument(
        "--start-urls",
        nargs="*",
        default=DEFAULT_START_URLS,
        help="URLs iniciais do recorte",
    )
    parser.add_argument(
        "--output-dir",
        default="./ajob2b_guides",
        help="Diretorio de saida",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=300,
        help="Maximo de paginas/arquivos Markdown",
    )
    parser.add_argument(
        "--split-h2",
        action="store_true",
        help="Divide paginas longas em arquivos por H2",
    )
    parser.add_argument(
        "--delay-s",
        type=float,
        default=0.0,
        help="Delay entre requisicoes",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Opcional: mantem apenas categorias especificas",
    )

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawl(
        start_urls=args.start_urls or DEFAULT_START_URLS,
        output_dir=output_dir,
        max_pages=args.max_pages,
        split_h2_enabled=args.split_h2,
        delay_s=args.delay_s,
        only_categories=args.only,
    )


if __name__ == "__main__":
    main()
