#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://www.copilot3d.org/"
TOOL_URL = "https://www.copilot3d.org/"
PRICING_URL = "https://www.copilot3d.org/pricing"
SHOWCASE_URL = "https://www.copilot3d.org/showcase"
EMAIL = "support@copilot3d.org"
KEYWORD = "copilot 3d ai 3d model generator"


BLUE_STYLE = """
      @page {
        size: A4;
        margin: 0;
      }

      :root {
        --ink: #10233f;
        --muted: #5c6f8a;
        --line: #d6dfea;
        --brand: #0066ff;
        --brand-deep: #0f3ea8;
        --panel: #f4f8ff;
        --panel-strong: #e8f0ff;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: var(--ink);
        background: #fff;
      }

      a {
        color: var(--brand-deep);
        text-decoration: none;
      }

      .page {
        width: 210mm;
        min-height: 297mm;
        padding: 16mm 14mm 18mm;
        page-break-after: always;
        position: relative;
        overflow: hidden;
      }

      .page:last-child {
        page-break-after: auto;
      }

      .hero {
        background:
          radial-gradient(circle at top right, rgba(0, 102, 255, 0.16), transparent 34%),
          linear-gradient(145deg, #f6f9ff 0%, #eaf1ff 48%, #ffffff 100%);
      }

      .eyebrow {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: rgba(0, 102, 255, 0.1);
        color: var(--brand-deep);
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }

      h1, h2, h3 {
        margin: 0;
      }

      h1 {
        margin-top: 18px;
        font-size: 34px;
        line-height: 1.08;
        max-width: 150mm;
      }

      h2 {
        font-size: 22px;
        line-height: 1.15;
        margin-bottom: 10px;
      }

      h3 {
        font-size: 15px;
        line-height: 1.3;
        margin-bottom: 8px;
      }

      p, li {
        font-size: 12.5px;
        line-height: 1.65;
        color: var(--muted);
        margin: 0;
      }

      ul, ol {
        margin: 10px 0 0;
        padding-left: 18px;
      }

      .hero-grid,
      .grid-2,
      .grid-3 {
        display: grid;
        gap: 12px;
      }

      .hero-grid,
      .grid-2 {
        grid-template-columns: 1.1fr 0.9fr;
      }

      .grid-3 {
        grid-template-columns: repeat(3, 1fr);
      }

      .lead {
        margin-top: 16px;
        max-width: 150mm;
        font-size: 14px;
        line-height: 1.72;
        color: #334766;
      }

      .hero-card,
      .card,
      .metric,
      .faq {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: #fff;
      }

      .hero-card,
      .card,
      .faq {
        padding: 14px;
      }

      .metric {
        padding: 12px 14px;
        background: var(--panel);
      }

      .metric strong {
        display: block;
        margin-top: 8px;
        font-size: 15px;
        line-height: 1.35;
        color: var(--ink);
      }

      .hero-links {
        margin-top: 16px;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
      }

      .hero-link {
        display: block;
        padding: 12px;
        border-radius: 16px;
        background: var(--panel-strong);
        border: 1px solid #c9d8f5;
      }

      .hero-link strong,
      .contact-list strong {
        display: block;
        color: var(--ink);
        font-size: 13px;
        margin-bottom: 4px;
      }

      .hero-link span,
      .contact-list span {
        display: block;
        font-size: 11.5px;
        color: var(--muted);
        line-height: 1.55;
      }

      .mini-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
        margin-top: 12px;
      }

      .mini-grid div {
        border: 1px solid var(--line);
        border-radius: 12px;
        background: var(--panel);
        padding: 12px;
      }

      .mini-grid strong {
        display: block;
        font-size: 12px;
        color: var(--ink);
        margin-bottom: 4px;
      }

      .mini-grid span {
        display: block;
        font-size: 11px;
        line-height: 1.5;
        color: var(--muted);
      }

      .section-head {
        margin-bottom: 14px;
      }

      .section-head p {
        margin-top: 8px;
        max-width: 155mm;
      }

      .stack {
        display: grid;
        gap: 12px;
      }

      .feature-list li,
      .faq p {
        color: #445878;
      }

      .steps li {
        margin-bottom: 8px;
      }

      .faq-list {
        display: grid;
        gap: 10px;
      }

      .page-footer {
        position: absolute;
        left: 14mm;
        right: 14mm;
        bottom: 8mm;
        display: flex;
        justify-content: space-between;
        font-size: 10.5px;
        color: #71829c;
      }

      .contact-list {
        display: grid;
        gap: 10px;
      }
"""


LANDING_STYLE = """
      :root {
        --bg: #f4f7fc;
        --ink: #10233f;
        --muted: #5e718b;
        --brand: #0059ff;
        --line: #d5deea;
        --card: #ffffff;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background:
          radial-gradient(circle at top right, rgba(0, 89, 255, 0.14), transparent 32%),
          linear-gradient(180deg, #eef4ff 0%, var(--bg) 100%);
        color: var(--ink);
      }

      main {
        max-width: 920px;
        margin: 0 auto;
        padding: 72px 24px;
      }

      .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 24px 60px rgba(16, 35, 63, 0.08);
      }

      .eyebrow {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(0, 89, 255, 0.1);
        color: var(--brand);
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }

      h1 {
        margin: 16px 0 12px;
        font-size: 44px;
        line-height: 1.05;
      }

      p {
        margin: 0;
        font-size: 17px;
        line-height: 1.7;
        color: var(--muted);
      }

      .actions,
      .links {
        display: grid;
        gap: 12px;
      }

      .actions {
        margin-top: 28px;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      }

      a.button,
      .links a {
        display: block;
        text-decoration: none;
      }

      a.button {
        padding: 16px 18px;
        border-radius: 16px;
        font-weight: 700;
      }

      a.primary {
        background: var(--brand);
        color: #fff;
      }

      a.secondary {
        background: #edf3ff;
        color: var(--ink);
        border: 1px solid #cad8f6;
      }

      .links {
        margin-top: 26px;
      }

      .links a {
        padding: 16px 18px;
        border-radius: 16px;
        border: 1px solid var(--line);
        background: #f9fbff;
        color: var(--ink);
      }

      .links strong {
        display: block;
        margin-bottom: 6px;
        font-size: 15px;
      }

      .links span {
        color: var(--muted);
        font-size: 14px;
        line-height: 1.6;
      }
"""


VARIANTS = [
    {
        "dir": ROOT,
        "slug": "main",
        "label": "main",
        "pdf_name": "copilot-3d-ai-3d-model-generator-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator PDF Guide",
        "landing_desc": "Download the Copilot 3D AI 3D model generator guide PDF with official links to the homepage, pricing, showcase, and product pages.",
        "hero_eyebrow": "Official Product Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Guide, Pricing, Features, and Official Pages",
        "hero_lead": "This PDF is a search-facing guide for the copilot 3d ai 3d model generator at www.copilot3d.org. It explains what the tool does, where the key pages live, which users it fits best, and where to click next for pricing, showcase examples, and the official product workflow.",
        "main_use_case": "AI 3D generation for text-to-3d and image-to-3d workflows",
        "variant_focus": "Best all-purpose PDF for branded and mixed-intent search traffic",
        "what_for": "Use this as the default PDF external link when a new site launches. It mirrors a strong landing page, keeps the keyword in the title and opening copy, and routes users to the official product pages.",
        "mini_points": [
            ("Keyword-first H1", "Lead with the core search term instead of generic product-guide wording."),
            ("Official page routing", "Always link the homepage, pricing, showcase, and tool entry inside the PDF."),
            ("SEO-style structure", "Keep sections for features, use cases, FAQs, and CTA links."),
            ("Search-friendly copy", "Write plain descriptive sentences that match how users search."),
        ],
        "page_map_intro": "This main PDF covers the full intent mix: product discovery, pricing validation, showcase browsing, and tool-entry navigation.",
        "use_cases_intro": "This version is built for general product discovery. It should convert readers who search for the product name or broad AI 3D generator terms.",
        "faq_extra_q": "Why should the H1 include copilot 3d ai 3d model generator?",
        "faq_extra_a": "Because the PDF title and opening section should clearly match the main keyword instead of using a vague document label.",
        "cta_title": "Visit the official Copilot 3D AI 3D model generator pages",
        "cta_copy": "Open www.copilot3d.org to review the official product, compare plans, check examples, and enter the tool directly.",
        "landing_heading": "Copilot 3D AI 3D Model Generator PDF Guide",
        "landing_copy": "This hosted PDF explains the copilot 3d ai 3d model generator like a search-facing landing page. It includes official links, product positioning, pricing references, showcase references, and clear CTAs back to the real website.",
        "landing_eyebrow": "PDF External Link",
    },
    {
        "dir": ROOT / "variants" / "vercel",
        "slug": "vercel",
        "label": "vercel-hosted",
        "pdf_name": "copilot-3d-ai-3d-model-generator-vercel-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Vercel PDF Guide",
        "landing_desc": "Vercel-hosted PDF external link for the Copilot 3D AI 3D model generator with official product links and SEO-focused copy.",
        "hero_eyebrow": "Vercel PDF External Link",
        "hero_title": "Copilot 3D AI 3D Model Generator Vercel PDF Guide and Official Page Directory",
        "hero_lead": "This Vercel-ready PDF version keeps the same blue template and keyword-first structure for the copilot 3d ai 3d model generator. Use it when the PDF landing page is deployed on Vercel and still needs to route users back to the official product pages.",
        "main_use_case": "Vercel-hosted PDF external link for branded and commercial-intent traffic",
        "variant_focus": "Use when publishing the PDF external-link page on Vercel",
        "what_for": "This version is for the same search intent as the main PDF, but the landing page copy explicitly fits a Vercel deployment so future publishing is cleaner and consistent.",
        "mini_points": [
            ("Blue template reuse", "Keep the visual style consistent across hosts."),
            ("Keyword continuity", "The keyword stays in the title, lead, and section headings."),
            ("Official links only", "The PDF still points back to the real product pages."),
            ("Host-specific deploy", "This folder is ready for Vercel static hosting."),
        ],
        "page_map_intro": "The page map stays the same because host changes should not change user routing intent.",
        "use_cases_intro": "Use this when the PDF file and landing page are deployed through Vercel but the SEO target remains the same.",
        "faq_extra_q": "Why keep a separate Vercel version?",
        "faq_extra_a": "Because separate host folders make deployment, rollback, and link management easier without changing the PDF strategy.",
        "cta_title": "Open the official Copilot 3D AI 3D model generator site",
        "cta_copy": "Use the official site links in this PDF to move from a hosted PDF landing page back into the real product flow.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Vercel PDF Guide",
        "landing_copy": "This Vercel-ready PDF external link package uses the same blue template and SEO structure as the main version, with links back to the homepage, pricing, showcase, and product pages.",
        "landing_eyebrow": "Vercel PDF Link",
    },
    {
        "dir": ROOT / "variants" / "github-pages",
        "slug": "github-pages",
        "label": "github-pages-hosted",
        "pdf_name": "copilot-3d-ai-3d-model-generator-github-pages-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator GitHub Pages PDF Guide",
        "landing_desc": "GitHub Pages version of the Copilot 3D AI 3D model generator PDF external link, optimized for search-facing discovery and click-through.",
        "hero_eyebrow": "GitHub Pages PDF External Link",
        "hero_title": "Copilot 3D AI 3D Model Generator GitHub Pages PDF Guide and Official Links",
        "hero_lead": "This GitHub Pages variant is the same blue-template PDF strategy adapted for a static repo deployment. The goal remains the same: rank a clean PDF asset around the copilot 3d ai 3d model generator keyword and send users back to the official site.",
        "main_use_case": "GitHub Pages-hosted PDF external link for branded and research-intent traffic",
        "variant_focus": "Use when publishing the PDF external-link page through GitHub Pages",
        "what_for": "Keep this folder separate for GitHub Pages deployments. It avoids mixing .nojekyll and repo-specific publishing needs into the main folder.",
        "mini_points": [
            ("GitHub Pages ready", "Publish this folder into the target repo root."),
            ("Keyword-first title", "Do not use a weak generic H1."),
            ("Search-facing intro", "The first paragraph should restate the keyword and site purpose."),
            ("Official route-back", "Every PDF should still drive clicks to the official site."),
        ],
        "page_map_intro": "Even on GitHub Pages, the page map should stay focused on the official commercial site, not the repo host.",
        "use_cases_intro": "Use this when you want a repo-hosted PDF landing page that can still capture branded or navigational search intent.",
        "faq_extra_q": "Why keep .nojekyll for this version?",
        "faq_extra_a": "Because GitHub Pages should publish the static files exactly as they are, without Jekyll processing side effects.",
        "cta_title": "Use the official Copilot 3D AI 3D model generator pages",
        "cta_copy": "The PDF may be hosted on GitHub Pages, but the conversion path should always return readers to the official website.",
        "landing_heading": "Copilot 3D AI 3D Model Generator GitHub Pages PDF Guide",
        "landing_copy": "This GitHub Pages package hosts the same blue PDF external-link format with official Copilot 3D page links and SEO-focused copy built around the copilot 3d ai 3d model generator keyword.",
        "landing_eyebrow": "GitHub Pages PDF Link",
    },
    {
        "dir": ROOT / "variants" / "pricing-guide",
        "slug": "pricing-guide",
        "label": "pricing-intent",
        "pdf_name": "copilot-3d-ai-3d-model-generator-pricing-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Pricing Guide PDF",
        "landing_desc": "Pricing-focused PDF guide for the Copilot 3D AI 3D model generator with links to plans, credits, and official product pages.",
        "hero_eyebrow": "Pricing Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Pricing Guide, Plans, Credits, and Official Links",
        "hero_lead": "This pricing-focused PDF targets users who search for the copilot 3d ai 3d model generator price, plan details, credit usage, or upgrade path. It explains the product at a high level and then pushes readers toward the official pricing and product pages.",
        "main_use_case": "Commercial-intent users comparing plans, credits, and upgrade value",
        "variant_focus": "Best for pricing, cost, plan, and credit-related searches",
        "what_for": "Use this variant for users closer to payment intent. The copy should emphasize pricing evaluation, plan comparison, and decision support without inventing unsupported numbers.",
        "mini_points": [
            ("Commercial intent", "Cover pricing, plans, credits, and value questions."),
            ("No fake numbers", "Do not invent exact prices unless the official page shows them."),
            ("Link to pricing page", "Pricing CTA should be highly visible."),
            ("Qualification copy", "Explain who should review pricing before generating."),
        ],
        "page_map_intro": "The pricing page becomes the primary route, while the homepage, showcase, and tool page stay as supporting navigation.",
        "use_cases_intro": "This variant is for users who are already evaluating whether the product is worth using or paying for.",
        "faq_extra_q": "How should pricing copy be written for SEO?",
        "faq_extra_a": "Use natural phrases like pricing, plans, credits, and upgrade path, then send readers to the official pricing page for exact current details.",
        "cta_title": "Review Copilot 3D AI 3D model generator pricing",
        "cta_copy": "Open the official pricing page to check the current plan structure, credits, and upgrade options before using the tool.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Pricing Guide PDF",
        "landing_copy": "This PDF focuses on Copilot 3D pricing intent. It explains what the tool is, who should compare plans, and where to open the official pricing, showcase, and product pages next.",
        "landing_eyebrow": "Pricing PDF Link",
    },
    {
        "dir": ROOT / "variants" / "tool-page-guide",
        "slug": "tool-page-guide",
        "label": "tool-intent",
        "pdf_name": "copilot-3d-ai-3d-model-generator-tool-page-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Tool Page Guide PDF",
        "landing_desc": "Tool-page-focused PDF for users who want to reach the Copilot 3D AI 3D model generator workflow directly.",
        "hero_eyebrow": "Tool Page Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Tool Page Guide and Workflow Entry PDF",
        "hero_lead": "This variant is built for users searching for the copilot 3d ai 3d model generator tool page, login path, or direct generator workflow. The copy moves quickly from product explanation into workflow steps and the official tool entry link.",
        "main_use_case": "Users ready to enter the generator workflow directly",
        "variant_focus": "Best for tool page, app entry, and direct-use intent",
        "what_for": "Use this when search intent is closer to action than research. The PDF should clarify what the tool does and then route users into the official workflow with minimal detours.",
        "mini_points": [
            ("Action-led copy", "Reduce generic branding and move faster toward workflow steps."),
            ("Tool-page CTA", "The tool link should feel like the main destination."),
            ("Workflow framing", "Explain text-to-3d and image-to-3d entry points clearly."),
            ("Intent match", "Match users who search for tool page, app, or generator access."),
        ],
        "page_map_intro": "The tool page becomes the lead destination because this variant is for direct workflow intent.",
        "use_cases_intro": "This version should convert readers who are already looking for the actual generator entry point instead of broad product research.",
        "faq_extra_q": "What should the strongest CTA be in this variant?",
        "faq_extra_a": "The strongest CTA should be the official product page because that is the clearest next step for action-led search intent.",
        "cta_title": "Open the Copilot 3D AI 3D model generator tool page",
        "cta_copy": "Use the official product page to start the real text-to-3d or image-to-3d workflow directly.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Tool Page Guide PDF",
        "landing_copy": "This PDF is optimized for readers who want the Copilot 3D product page quickly. It explains the workflow briefly, then points users to the official generator, pricing, and showcase pages.",
        "landing_eyebrow": "Tool Page PDF Link",
    },
    {
        "dir": ROOT / "variants" / "showcase-guide",
        "slug": "showcase-guide",
        "label": "showcase-intent",
        "pdf_name": "copilot-3d-ai-3d-model-generator-showcase-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Showcase Guide PDF",
        "landing_desc": "Showcase-focused PDF guide for users evaluating Copilot 3D AI 3D model generator examples and output quality.",
        "hero_eyebrow": "Showcase Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Showcase Guide, Examples, and Official Links",
        "hero_lead": "This showcase-focused PDF targets users who want to inspect copilot 3d ai 3d model generator examples, output style, output quality, and creative references before trying the product. It keeps the showcase page prominent while still linking the official site and tool flow.",
        "main_use_case": "Users validating visual quality and example output before trying the tool",
        "variant_focus": "Best for example, gallery, output-quality, and showcase searches",
        "what_for": "Use this version when example quality is the main conversion driver. The copy should emphasize visual proof, reference browsing, and output expectations.",
        "mini_points": [
            ("Proof-first copy", "Lead with examples, visual quality, and motion references."),
            ("Showcase CTA", "The showcase link should be near the top."),
            ("Expectation setting", "Explain what examples help readers evaluate."),
            ("Conversion support", "Use proof content to move readers toward the tool page."),
        ],
        "page_map_intro": "The showcase page becomes the primary evaluation page, with the tool and pricing pages supporting the conversion path.",
        "use_cases_intro": "This variant is strong for users who believe examples more than claims and want to assess the output before clicking into the tool.",
        "faq_extra_q": "Why build a showcase-specific PDF?",
        "faq_extra_a": "Because many users search for examples or outputs first, and a showcase-led PDF matches that intent better than a generic brand guide.",
        "cta_title": "Browse Copilot 3D AI 3D model generator examples",
        "cta_copy": "Use the official showcase page to review examples, compare output direction, and then continue into the product.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Showcase Guide PDF",
        "landing_copy": "This PDF focuses on Copilot 3D examples, output quality, and visual proof. It guides readers from showcase intent into the official tool and pricing pages.",
        "landing_eyebrow": "Showcase PDF Link",
    },
    {
        "dir": ROOT / "variants" / "text-to-3d-guide",
        "slug": "text-to-3d-guide",
        "label": "text-to-3d-intent",
        "pdf_name": "copilot-3d-ai-3d-model-generator-text-to-3d-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Text to 3D Guide PDF",
        "landing_desc": "Text-to-3D-focused PDF for users researching prompt-led 3D generation with the Copilot 3D AI 3D model generator.",
        "hero_eyebrow": "Text to 3D Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Text to 3D Guide and Prompt Workflow PDF",
        "hero_lead": "This PDF targets text-to-3d intent around the copilot 3d ai 3d model generator keyword. It focuses on prompt-led workflow, concept-to-3D use cases, and the official pages users should visit when they want to generate 3D models from text descriptions.",
        "main_use_case": "Prompt-led generation for creators, marketers, and concept teams",
        "variant_focus": "Best for text-to-3d and prompt-based generation searches",
        "what_for": "Use this version when the page or query is specifically about prompt-led 3D generation. The copy should repeatedly clarify that users can start from text and then refine with the official tool flow.",
        "mini_points": [
            ("Prompt-led intent", "Use phrases like text to 3d, prompt workflow, and prompt-led 3D generation."),
            ("Idea-to-motion framing", "Explain how text prompts become 3D asset."),
            ("Tool-entry support", "Link prompt intent to the official product page."),
            ("Clear scope", "Keep the message centered on text-to-3d instead of all features equally."),
        ],
        "page_map_intro": "The product page and showcase page matter most here because users want to see and try prompt-led output quickly.",
        "use_cases_intro": "This PDF works when users search for text-to-3d workflow terms rather than broad branded queries.",
        "faq_extra_q": "How should text-to-3d copy be framed?",
        "faq_extra_a": "Describe prompt-led 3D generation in plain language and show readers where to test it on the official product page.",
        "cta_title": "Start a Copilot 3D AI 3D model generator text-to-3d workflow",
        "cta_copy": "Open the official site to move from prompt idea to generated 3D output.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Text to 3D Guide PDF",
        "landing_copy": "This PDF is for prompt-led text-to-3d intent. It explains how Copilot 3D fits ideation and 3D asset workflows, then links to the official product pages.",
        "landing_eyebrow": "Text to Video PDF Link",
    },
    {
        "dir": ROOT / "variants" / "image-to-3d-guide",
        "slug": "image-to-3d-guide",
        "label": "image-to-3d-intent",
        "pdf_name": "copilot-3d-ai-3d-model-generator-image-to-3d-guide.pdf",
        "landing_title": "Copilot 3D AI 3D Model Generator Image to 3D Guide PDF",
        "landing_desc": "Image-to-3D-focused PDF for users exploring reference-led 3D generation with the Copilot 3D AI 3D model generator.",
        "hero_eyebrow": "Image to 3D Guide PDF",
        "hero_title": "Copilot 3D AI 3D Model Generator Image to 3D Guide and Reference Workflow PDF",
        "hero_lead": "This variant focuses on image-to-3d intent around the copilot 3d ai 3d model generator keyword. It explains how users can start from a reference image, keep stronger art direction, and use the official product pages to enter the generator workflow.",
        "main_use_case": "Reference-led 3D generation for art direction, consistency, and visual control",
        "variant_focus": "Best for image-to-3d and reference-image workflow searches",
        "what_for": "Use this version when users are more likely to arrive from reference-image, 3D generation, or image-to-3d queries. The copy should emphasize visual control and reference-led motion.",
        "mini_points": [
            ("Reference-led angle", "Use phrases like image to 3d, reference image, and motion from stills."),
            ("Control framing", "Highlight stronger art direction and consistency."),
            ("Showcase support", "Use examples to prove image-led quality."),
            ("Workflow route", "Send users from explanation to the official product page."),
        ],
        "page_map_intro": "The product and showcase pages do the most work for this intent because users want proof and a direct way to try reference-led motion.",
        "use_cases_intro": "This version is best for users who already have images or concept frames and want to animate them online.",
        "faq_extra_q": "Why separate image-to-3d from the general guide?",
        "faq_extra_a": "Because image-to-3d search intent is more specific, and a focused PDF matches that wording and use case better.",
        "cta_title": "Start a Copilot 3D AI 3D model generator image-to-3d workflow",
        "cta_copy": "Open the official site, review examples, and use the product page to animate a reference image into a 3D model.",
        "landing_heading": "Copilot 3D AI 3D Model Generator Image to 3D Guide PDF",
        "landing_copy": "This PDF focuses on reference-led image-to-3d intent. It explains the workflow, highlights visual-control use cases, and links readers to the official product pages.",
        "landing_eyebrow": "Image to Video PDF Link",
    },
]


def render_pdf_page(item: dict) -> str:
    faq_extra_q = item["faq_extra_q"]
    faq_extra_a = item["faq_extra_a"]
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{item["hero_title"]}</title>
    <style>
{BLUE_STYLE}
    </style>
  </head>
  <body>
    <section class="page hero">
      <span class="eyebrow">{item["hero_eyebrow"]}</span>
      <h1>{item["hero_title"]}</h1>
      <p class="lead">{item["hero_lead"]}</p>

      <div class="hero-grid" style="margin-top: 18px;">
        <div class="stack">
          <div class="metric">
            <span>Primary website</span>
            <strong><a href="{SITE_URL}">{SITE_URL}</a></strong>
          </div>
          <div class="metric">
            <span>Main use case</span>
            <strong>{item["main_use_case"]}</strong>
          </div>
          <div class="metric">
            <span>Variant focus</span>
            <strong>{item["variant_focus"]}</strong>
          </div>

          <div class="hero-links">
            <a class="hero-link" href="{TOOL_URL}">
              <strong>Homepage</strong>
              <span>Open the main Copilot 3D website.</span>
            </a>
            <a class="hero-link" href="{PRICING_URL}">
              <strong>Pricing</strong>
              <span>Review plans, credits, and upgrade paths.</span>
            </a>
            <a class="hero-link" href="{SHOWCASE_URL}">
              <strong>Showcase</strong>
              <span>Browse examples and quality references.</span>
            </a>
            <a class="hero-link" href="{SITE_URL}">
              <strong>Official Site</strong>
              <span>Enter the Copilot 3D generator.</span>
            </a>
          </div>
        </div>

        <div class="hero-card">
          <h3>What this PDF is for</h3>
          <p>{item["what_for"]}</p>
          <div class="mini-grid">
            {render_mini_points(item["mini_points"])}
          </div>
        </div>
      </div>

      <div class="page-footer">
        <span>{item["hero_title"]}</span>
        <span><a href="{SITE_URL}">www.copilot3d.org</a></span>
      </div>
    </section>

    <section class="page">
      <div class="section-head">
        <span class="eyebrow">Keyword Match</span>
        <h2>Why users search for the copilot 3d ai 3d model generator</h2>
        <p>
          Users search for the {KEYWORD} when they want a clear browser-based workflow for text-to-3d,
          image-to-3d, pricing review, output examples, or the direct tool-entry path. This PDF should
          describe the product in plain English and keep those intents visible in the section headings.
        </p>
      </div>

      <div class="grid-3">
        <article class="card">
          <h3>Text to 3D</h3>
          <p>Start from a written prompt and generate 3D asset with style, subject, lighting, and camera direction.</p>
        </article>
        <article class="card">
          <h3>Image to 3D</h3>
          <p>Upload a reference image and turn a static frame into a 3D model with stronger art direction control.</p>
        </article>
        <article class="card">
          <h3>Browser workflow</h3>
          <p>Use the product directly in a browser without needing a heavyweight editing setup.</p>
        </article>
        <article class="card">
          <h3>Pricing validation</h3>
          <p>Commercial-intent users often want plan context before they commit time or credits.</p>
        </article>
        <article class="card">
          <h3>Showcase proof</h3>
          <p>Example-driven users want to inspect quality, motion style, and creative fit before clicking deeper.</p>
        </article>
        <article class="card">
          <h3>Official route-back</h3>
          <p>The goal of this guide is to route readers to www.copilot3d.org and its key pages.</p>
        </article>
      </div>

      <div class="section-head" style="margin-top: 18px;">
        <span class="eyebrow">Core Features</span>
        <h2>What to include in a SEO-friendly blue-template PDF</h2>
      </div>

      <div class="grid-2">
        <article class="card">
          <h3>Required content blocks</h3>
          <ul class="feature-list">
            <li>Keyword-first H1 that names the product and the core search phrase</li>
            <li>Short opening paragraph that explains the product and intent match</li>
            <li>Homepage, pricing, showcase, and official site links near the top</li>
            <li>Feature summary with text-to-3d and image-to-3d wording</li>
            <li>Use cases that match creator, marketing, and production workflows</li>
            <li>FAQ answers written in descriptive, indexable language</li>
          </ul>
        </article>
        <article class="card">
          <h3>SEO copy rules</h3>
          <ul class="feature-list">
            <li>Put the main keyword in the title, H1, opening paragraph, and at least one subheading.</li>
            <li>Use natural wording around pricing, examples, text to 3d, and image to 3d.</li>
            <li>Do not stuff keywords into empty lists; use readable explanatory sentences.</li>
            <li>Link to the official product pages using descriptive anchor text.</li>
          </ul>
        </article>
      </div>

      <div class="page-footer">
        <span>Keyword Match and SEO Structure</span>
        <span><a href="{SITE_URL}">www.copilot3d.org</a></span>
      </div>
    </section>

    <section class="page">
      <div class="section-head">
        <span class="eyebrow">Page Map</span>
        <h2>Important official pages readers should know</h2>
        <p>{item["page_map_intro"]}</p>
      </div>

      <div class="stack">
        <article class="card">
          <h3>Homepage</h3>
          <p><a href="{SITE_URL}">{SITE_URL}</a></p>
          <p>The main orientation page for the product, brand, and top-level navigation.</p>
        </article>
        <article class="card">
          <h3>Official Site</h3>
          <p><a href="{TOOL_URL}">{TOOL_URL}</a></p>
          <p>The fastest route for users who already know what they want and want to try the generator.</p>
        </article>
        <article class="card">
          <h3>Pricing page</h3>
          <p><a href="{PRICING_URL}">{PRICING_URL}</a></p>
          <p>Useful for plan, credits, feature access, and upgrade evaluation.</p>
        </article>
        <article class="card">
          <h3>Showcase page</h3>
          <p><a href="{SHOWCASE_URL}">{SHOWCASE_URL}</a></p>
          <p>The page to inspect visual examples, motion references, and output direction.</p>
        </article>
      </div>

      <div class="section-head" style="margin-top: 18px;">
        <span class="eyebrow">Workflow</span>
        <h2>Typical user flow from search to click-through</h2>
      </div>

      <article class="card">
        <ol class="steps">
          <li><strong>Match the keyword:</strong> Make the title and opening paragraph clearly about the {KEYWORD}.</li>
          <li><strong>Explain the product:</strong> Describe text-to-3d and image-to-3d in simple, human language.</li>
          <li><strong>Route by intent:</strong> Surface pricing, showcase, homepage, and tool links based on what readers want next.</li>
          <li><strong>Send users back:</strong> Use the PDF as an SEO asset that returns readers to the official site.</li>
        </ol>
      </article>

      <div class="page-footer">
        <span>Page Map and Workflow</span>
        <span><a href="{SITE_URL}">www.copilot3d.org</a></span>
      </div>
    </section>

    <section class="page">
      <div class="section-head">
        <span class="eyebrow">Use Cases</span>
        <h2>Where this PDF fits in search and conversion workflows</h2>
        <p>{item["use_cases_intro"]}</p>
      </div>

      <div class="grid-2">
        <article class="card">
          <h3>Brand discovery</h3>
          <p>Use the PDF to capture readers who search for the product name and need a stronger explanation than a short directory listing.</p>
        </article>
        <article class="card">
          <h3>Commercial research</h3>
          <p>Guide users toward pricing, plan comparison, and tool-fit evaluation without losing the official click path.</p>
        </article>
        <article class="card">
          <h3>Example-led validation</h3>
          <p>Support users who need visual proof through the showcase page before they trust a new AI 3D tool.</p>
        </article>
        <article class="card">
          <h3>Workflow entry</h3>
          <p>Move ready-to-use readers from explanation into the official generator page with minimal friction.</p>
        </article>
      </div>

      <div class="section-head" style="margin-top: 18px;">
        <span class="eyebrow">FAQ</span>
        <h2>Questions this PDF should answer clearly</h2>
      </div>

      <div class="faq-list">
        <article class="faq">
          <h3>What is the copilot 3d ai 3d model generator?</h3>
          <p>It is a browser-based AI 3D generation workflow designed for prompt-led creation and reference-led 3D generation.</p>
        </article>
        <article class="faq">
          <h3>Why should the PDF link multiple official pages?</h3>
          <p>Because readers may arrive with pricing, example, or direct-tool intent, so the PDF should route them to the right official page instead of forcing one path.</p>
        </article>
        <article class="faq">
          <h3>{faq_extra_q}</h3>
          <p>{faq_extra_a}</p>
        </article>
        <article class="faq">
          <h3>Can this PDF help Google index the topic?</h3>
          <p>Yes, if the PDF has a descriptive title, readable body copy, strong headings, and clear links to the official site instead of thin or duplicate filler text.</p>
        </article>
      </div>

      <div class="page-footer">
        <span>Use Cases and FAQ</span>
        <span><a href="{SITE_URL}">www.copilot3d.org</a></span>
      </div>
    </section>

    <section class="page">
      <div class="section-head">
        <span class="eyebrow">Official Links</span>
        <h2>Where to go next</h2>
        <p>
          The website remains the main destination for action. This PDF should explain the product,
          match search intent, and then route readers to the correct official page.
        </p>
      </div>

      <div class="contact-list">
        <div class="card">
          <strong>Main website</strong>
          <span><a href="{SITE_URL}">{SITE_URL}</a></span>
        </div>
        <div class="card">
          <strong>Homepage</strong>
          <span><a href="{TOOL_URL}">{TOOL_URL}</a></span>
        </div>
        <div class="card">
          <strong>Pricing</strong>
          <span><a href="{PRICING_URL}">{PRICING_URL}</a></span>
        </div>
        <div class="card">
          <strong>Showcase</strong>
          <span><a href="{SHOWCASE_URL}">{SHOWCASE_URL}</a></span>
        </div>
        <div class="card">
          <strong>Email</strong>
          <span><a href="mailto:{EMAIL}">{EMAIL}</a></span>
        </div>
      </div>

      <div class="section-head" style="margin-top: 18px;">
        <span class="eyebrow">CTA</span>
        <h2>{item["cta_title"]}</h2>
        <p>{item["cta_copy"]}</p>
      </div>

      <div class="page-footer">
        <span>{item["cta_title"]}</span>
        <span><a href="{SITE_URL}">www.copilot3d.org</a></span>
      </div>
    </section>
  </body>
</html>
"""


def render_mini_points(points: list[tuple[str, str]]) -> str:
    return "\n            ".join(
        f"<div><strong>{title}</strong><span>{copy}</span></div>" for title, copy in points
    )


def render_landing_page(item: dict) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{item["landing_title"]}</title>
    <meta name="description" content="{item["landing_desc"]}" />
    <style>
{LANDING_STYLE}
    </style>
  </head>
  <body>
    <main>
      <section class="card">
        <span class="eyebrow">{item["landing_eyebrow"]}</span>
        <h1>{item["landing_heading"]}</h1>
        <p>{item["landing_copy"]}</p>

        <div class="actions">
          <a class="button primary" href="./{item["pdf_name"]}">Open PDF</a>
          <a class="button secondary" href="{SITE_URL}">Visit copilot3d.org</a>
        </div>

        <div class="links">
          <a href="{SITE_URL}">
            <strong>Main Website</strong>
            <span>{SITE_URL}</span>
          </a>
          <a href="{TOOL_URL}">
            <strong>Homepage</strong>
            <span>{TOOL_URL}</span>
          </a>
          <a href="{PRICING_URL}">
            <strong>Pricing</strong>
            <span>{PRICING_URL}</span>
          </a>
          <a href="{SHOWCASE_URL}">
            <strong>Showcase</strong>
            <span>{SHOWCASE_URL}</span>
          </a>
        </div>
      </section>
    </main>
  </body>
</html>
"""


def write_variant(item: dict) -> None:
    item["dir"].mkdir(parents=True, exist_ok=True)
    (item["dir"] / "guide-source.html").write_text(render_pdf_page(item), encoding="utf-8")
    (item["dir"] / "index.html").write_text(render_landing_page(item), encoding="utf-8")
    if item["slug"] == "github-pages":
        (item["dir"] / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    for item in VARIANTS:
        write_variant(item)


if __name__ == "__main__":
    main()
