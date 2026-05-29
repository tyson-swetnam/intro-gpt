# Presentation Decks

A small library of HTML slide decks authored for the [UA Public Health & AI Summer School](https://keys.arizona.edu/){target=_blank} 2026. Each deck is a self-contained 1920×1080 presentation that pairs with one or more workshop docs lessons.

## How to view

- Click a deck title below to open it. Use your browser's "open in new tab" if you want the slides visible alongside the docs.
- **Keyboard:** Arrow keys, space, Page Up / Page Down to navigate. `Home` / `End` jump to start or end. `f` toggles full-screen.
- **Click navigation:** click the right half of the slide to advance, left half to go back.
- Each deck remembers your last position via `localStorage` and the URL hash (e.g. `#7` for slide 7) — refresh-safe.
- **Print to PDF:** your browser's print dialog produces a 1920×1080 PDF with one slide per page.

## Decks

### [Prompt Engineering Basics](prompt-engineering-basics.html){target=_blank}

The 24-slide introduction: how AI models process prompts, the CRAFT framework, advanced techniques (custom instructions, few-shot learning, prompt chaining, multi-modal inputs, web search), and the four common pitfalls every cohort makes.

**Pairs with:** [Prompt Engineering](../../prompts.md)

### [Prompt Engineering Deep Dive — Agentic Workflows](prompt-engineering-deep-dive.html){target=_blank}

The follow-on deck pushing past single prompts into agentic workflows, multi-step orchestration, and the model–tool boundary.

**Pairs with:** [Prompt Engineering](../../prompts.md), [Vibe Coding](../../vibe.md), and [Agentic AI](../../agentic.md)

### [Ethics & Environmental Impact](ethics-and-environmental-impact.html){target=_blank}

Panel deck covering responsible-use frameworks, the civic-grammar argument from Alondra Nelson, regulatory landscape, and the environmental cost of frontier-model training and inference.

**Pairs with:** [Ethics of AI](../../ethics.md), [Bias & Discrimination](../../bias.md), and [Ethical & Legal Considerations](../../legal.md)

### [Geospatial AI for Public Health](geospatial-ai-public-health.html){target=_blank}

Lab deck for the GIS practical: building an interactive story-map of a public-health dataset using an agentic coding workflow.

**Pairs with:** [Vibe coding a Public Health Map](../publichealth/gis.md)

## About the deck shell

These decks use a small custom element, `<deck-stage>`, served alongside the HTML at [`deck-stage.js`](deck-stage.js). It handles canvas scaling, keyboard and click navigation, the slide counter, URL-hash persistence, and print-to-PDF. The full source is short and editable — fork it freely.

## License

All decks are released under [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/){target=_blank}, the same license as the rest of the workshop. Authored for the UA PH&AI Summer School and the [BIO5 KEYS Research Internship](https://keys.arizona.edu/){target=_blank}.
