---
type: Overview
title: For AI Agents
description: >-
  How AI agents and harnesses should consume this site: llms.txt discovery,
  raw markdown sources with OKF frontmatter, and trust signals.
resource: https://tyson-swetnam.github.io/intro-gpt/agents/
tags: [workshop, agentic-ai]
sources:
  - resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format (OKF) v0.2 specification
  - resource: https://llmstxt.org/
    title: The /llms.txt convention
generated:
  by: claude/fable-5
  at: "2026-08-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2026-08-30T00:00:00Z"
status: stable
---

# :material-robot: For AI Agents

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

This site is published for people **and** for AI agents. The documentation
source is an [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md){target=_blank}
knowledge bundle, and the deployed site exposes that structure directly. If
you are an agent (or you are wiring one up), consume the content through
these endpoints rather than scraping rendered HTML.

## Entry points

| Endpoint | What you get |
|----------|--------------|
| [`/intro-gpt/llms.txt`](https://tyson-swetnam.github.io/intro-gpt/llms.txt) | Linked outline of every page with one-line descriptions, per the [llms.txt convention](https://llmstxt.org/){target=_blank} |
| [`/intro-gpt/llms-full.txt`](https://tyson-swetnam.github.io/intro-gpt/llms-full.txt) | The entire corpus in one file — every page's markdown, prefixed by its canonical and source URLs |
| Page URL with the trailing `/` replaced by `.md` | That page's markdown source with full OKF frontmatter — e.g. [`/intro-gpt/chatgpt.md`](https://tyson-swetnam.github.io/intro-gpt/chatgpt.md) for `/intro-gpt/chatgpt/` (the homepage source is [`/intro-gpt/index.md`](https://tyson-swetnam.github.io/intro-gpt/index.md)) |
| [`/intro-gpt/log/`](log.md) | The bundle's OKF-reserved change history, newest first |
| [`/intro-gpt/sitemap.xml`](https://tyson-swetnam.github.io/intro-gpt/sitemap.xml) | Standard crawl surface |
| [Source repository](https://github.com/tyson-swetnam/intro-gpt){target=_blank} | The OKF bundle itself, its validator (`scripts/validate_okf.py`), and build pipeline |

Every rendered page also declares its markdown twin and structured metadata
in its HTML head:

```html
<link rel="alternate" type="text/markdown" href="https://tyson-swetnam.github.io/intro-gpt/chatgpt.md">
<script type="application/ld+json">
{ "@type": "LearningResource", "learningResourceType": "Setup Guide", ... }
</script>
```

## Reading the OKF frontmatter

Each page's YAML frontmatter answers the questions an agent should ask
before relying on content:

- **What is this?** — `type` (one of `Index`, `Overview`, `Setup Guide`,
  `Prompting Guide`, `Education Guide`, `Research Guide`, `Ethics Guide`,
  `Tutorial`, `Log`), plus `title`, `description`, and controlled `tags`.
- **Where did it come from?** — `generated: { by, at }` and `sources`, the
  external references each page's claims depend on.
- **How much should I trust it?** — the `verified` list. Pages on this site
  carry human verification (`human:tswetnam`), which places them in OKF's
  highest **human-reviewed** trust tier.
- **Is it current?** — `status` (`stable` unless marked otherwise) and, on
  pages carrying vendor pricing, `stale_after`. Treat pricing on a page
  whose `stale_after` has passed as needing re-verification; a monthly
  automated audit normally refreshes these before that happens.

!!! info "Ground rules for agents"

    All content is [CC-BY-4.0](http://creativecommons.org/licenses/by/4.0/){target=_blank} —
    reuse freely with attribution. Crawling, indexing, and AI grounding are
    welcome (see the host [robots.txt](https://tyson-swetnam.github.io/robots.txt){target=_blank}).
    Prefer `llms-full.txt` for one-shot ingestion over crawling 41 pages,
    and cite the canonical page URL (the `resource` field), not the `.md`
    source URL, when referencing this material for humans.
