---
description: Re-audit AI vendor pricing across the docs and apply verified updates with a current month/year stamp.
argument-hint: "[branch-name]  (defaults to claude/refresh-pricing-<YYYYMM>)"
---

You are running the periodic pricing-refresh workflow for this Zensical docs site. The goal: re-verify current pricing for the **core AI vendors** the site recommends, apply any changes, and refresh "verified [Month Year]" stamps to today's month/year.

## Setup

1. Read `CLAUDE.md` if present.
2. Determine today's month/year (use the date from the system context, not training data).
3. Determine the target branch:
   - If the user passed an argument, use it.
   - Otherwise create `claude/refresh-pricing-YYYYMM` from `main`.
4. Verify the working tree is clean. If not, ask the user before continuing.

## Phase A — Audit (read-only)

Run `rg -n -i --type md '(verified|as of|pricing.*(20[2-9][0-9])|january|february|march|april|may|june|july|august|september|october|november|december).*20[2-9][0-9]|\\$[0-9]+(\\.[0-9]+)?(/M|/k|/million|/thousand| per | / month)?'` from `docs/`.

Then dispatch a single Explore-type agent to produce a structured audit report listing:
- Every "verified [Month Year]" / "as of [Month Year]" stamp with file:line.
- Every pricing table or pricing line that mentions a dollar amount, grouped by file.
- Every vendor row in `docs/choose.md` with its current cost cell.

Cap report at 30 files; long-tail files listed by name only.

## Phase B — Research (parallel webcrawlers)

Dispatch **8 parallel `webcrawler` sub-agents** — one per vendor cluster. Each agent must:
- Try the official pricing page first.
- Fall back to WebSearch for recent (current-year) third-party pricing trackers and vendor blog announcements when the official page returns a 403/JS-only shell.
- Output a structured report per plan: `Price / Source URL / Fetched / Confidence (high|medium|low) / Notes`.
- End with a `Change summary` listing matches-vs-changes against the existing docs.

**Vendor clusters** (mirror what the September 2026 refresh used; adjust if vendors have come or gone):

1. **Anthropic** — claude.ai consumer plans (Free/Pro/Max 5x–20x/Team Standard/Team Premium/Enterprise seat price) + what the Pro bundle includes (Claude Code, Claude in Chrome, Claude Science) + API per-1M-token rates for the current Fable/Opus/Sonnet/Haiku models + caching/batch discounts + Claude for Education, the AI for Science credit program, and the Team plan for scientists + Microsoft Foundry availability. Sources: `claude.com/pricing`, `platform.claude.com/docs/en/about-claude/models/overview`, `claude.com/solutions/education`, `support.claude.com`.
2. **OpenAI** — ChatGPT consumer plans (Free/Go/Plus/Pro $100–$500 tiers/Business Standard–Premium/Enterprise/Edu) + Codex inclusion and student credits + ChatGPT for Teachers + Back to School offers + Prism + OpenAI API per-1M-token rates for the current GPT-6 / GPT-5.x / Codex / GPT Image models + custom-GPT and plugin status. Confirm Sora and ChatGPT Atlas stay discontinued. Sources: `developers.openai.com/api/docs/pricing` (fetches), `help.openai.com` articles (usually 403 — use search snippets), `learn.chatgpt.com/docs/pricing`.
3. **Google** — Google AI Plus/Pro/Ultra (5x and 20x) consumer plans + the student free-year window + Gemini for Education + Gemini API rates (Flash/Flash-Lite/Pro tiers and any promo end dates) + Veo per-second + Gemini Notebook (formerly NotebookLM) bundling + Antigravity/Jules tiers. Sources: `gemini.google/subscriptions`, `ai.google.dev/gemini-api/docs/pricing`, `gemini.google/students`, `jules.google/docs/usage-limits`, `antigravity.google/pricing`.
4. **Microsoft + GitHub** — GitHub Copilot Free/Pro/Pro+/Max/Business/Enterprise/Student (AI Credits per plan, sign-up status, which plans get Opus) + Microsoft 365 Copilot enterprise and Business add-ons, Business Standard/Premium bundles, Copilot for Education ($/user), Copilot Chat free inclusion, Microsoft 365 Premium (consumer) + Microsoft Foundry (formerly Azure AI Studio / Azure OpenAI Service) model catalog. Sources: `github.com/features/copilot/plans`, `docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot`, `github.blog/changelog`, `microsoft.com/en-us/microsoft-365-copilot/pricing`, `microsoft.com/en-us/education/products/copilot-in-education`, `learn.microsoft.com/en-us/azure/foundry/what-is-foundry`.
5. **Multi-AI access** — Perplexity (Free/Pro/Max/Education Pro/Enterprise, Comet, Computer, Sonar API), Poe, HuggingChat Omni + Hugging Face PRO/Team/Enterprise + Inference Providers credits, DeepSeek (current model names, peak/off-peak API rates), Grok/xAI (SuperGrok tiers, API), Mistral Vibe (formerly Le Chat; Free/Pro/student/Team, API free mode), Meta (open weights only — the Llama API shut down July 2026; confirm no revival). You.com is API-only now (Research API). Sources: each vendor's `/pricing` page; cross-check with third-party trackers.
6. **Coding tools** — Cursor (Hobby/Pro/Pro+/Ultra/Teams, student promos), OpenAI Codex, Google Antigravity + Jules, Devin / Devin Desktop (formerly Windsurf), Kiro, Replit, and the open-source agents Cline / OpenCode / Aider. Phind, Continue.dev, and Roo Code are gone — do not re-check them. Note acquisitions or shutdowns.
7. **Image/video gen** — Midjourney (current major version + plans), Adobe Firefly, Runway, Veo (current version + per-second), Kling (current GA version), Nano Banana / GPT Image per-image costs, Stability AI. Sora is discontinued — do not re-check.
8. **Developer gateways and free API tiers** — OpenRouter, Groq, Cerebras, Hugging Face Inference Providers, xAI API, Perplexity Sonar, Together AI, Replicate: free-tier limits, data-use terms, and headline rates. GitHub Models was retired July 2026 — do not re-add it.

Each webcrawler should not edit any files.

## Phase C — Apply updates (parallel general-purpose agents)

Dispatch **4 parallel general-purpose sub-agents** — one per file cluster — and pass each agent the verified pricing data it needs. Tell each agent to:
- Edit in place, do NOT commit/push.
- Use `(verify)` markers inline next to medium-confidence numbers.
- Preserve canonical external identifiers (HuggingFace repo names, paper titles, citation-style refs).

**File clusters:**

1. `docs/choose.md` — heaviest file. Update the "Education & Research Offers" table and the "Free API Tiers" table at the top, then every vendor row in the comparison tables, the agentic-browser rows, and the "API Pricing for Developers" table. Update every "verified [Month Year]" / "not re-verified [Month Year]" stamp. Move any discontinued tool into the Deprecated/Archived box.
2. `docs/chatgpt.md` + `docs/claude.md` + `docs/claude-code.md` + `docs/microsoft.md` + `docs/copilot.md` — vendor pages with detailed pricing blocks, plan tables, and API rate tables.
3. `docs/gemini.md` + `docs/index.md` + `docs/vscode.md` + `docs/rag.md` + `docs/notebooklm.md` — Google subscriptions and the student offer window, homepage subscription summary, Copilot and Cursor pricing in vscode.md, RAG comparison table, Gemini Notebook plans.
4. `docs/ai_landscape.md` + `docs/vibe.md` + `docs/tutoring.md` + `docs/daily-productivity.md` + `docs/admissions.md` + `docs/plagiarism.md` + `docs/teaching.md` + `docs/gradio.md` + any other file with a stale stamp. Update stamps only; add a "not re-verified [Month Year]" caveat for sections with edu/plagiarism/research-tool pricing that this round did not verify.

### OKF metadata maintenance (same pass)

Every page carries OKF v0.2 frontmatter (see `CLAUDE.md`). When a pricing page's body changes in this refresh:
- Bump its `stale_after` to the first of the month six months out (e.g. a November 2026 refresh sets `stale_after: "2027-05-01T00:00:00Z"`), keeping it in step with the new "as of" stamp.
- Update `generated.at` to the current date (ISO-8601, quoted).
- Do **NOT** touch `verified` — verification entries are added only by a human (the merge is the human review).
- Append one `**Update**` line under a new `## YYYY-MM-DD` heading (newest first) in `docs/log.md` summarizing the pricing pass.
- Run `python3 scripts/validate_okf.py docs` before committing.

## Phase D — Commit and push

Once all 4 update agents have reported back:
1. `git diff --stat` — sanity check the file list. Should be roughly the same set of files as the May 2026 refresh.
2. Stage only the changed `docs/*.md` files, plus `zensical.toml` if a nav label changed — do not stage anything else.
3. Run the consistency grep for retired names before committing (`rg -n -i 'Gemini Advanced|NotebookLM Plus|Google One AI Premium|Azure OpenAI|Codeium|Le Chat|Copilot Workspace|GitHub Models' docs`) and confirm every hit is a deliberate "(formerly …)" or history mention.
4. Commit with a message that summarizes:
   - High-confidence price changes applied
   - Medium-confidence items marked `(verify)`
   - Stamps refreshed from old → new
   - Out-of-scope tool categories
5. Push to the target branch with `git push -u origin <branch>`.
6. Ask the user whether to open a PR. Default to opening one, base `main`.

## Notes

- This workflow is the canonical pricing-refresh runbook. It was first executed in May 2026 (commit `3743ab1`) and re-run with a platform overhaul in September 2026. When prices drift again, re-running this command should produce the next month's refresh.
- Out of scope by design: edu tools (Magic School AI, Education Copilot, IXL, Codecademy, Brilliant, MasterClass, Coursera) and plagiarism detectors (GPTZero, Originality.AI, Turnitin, Copyleaks, Winston, Scribbr, PaperPal). These have their own update cycles; covering them would multiply the webcrawl fan-out. Academic research tools (Elicit, Consensus, Scite, Undermind, SciSpace, Ai2 Asta, Edison Scientific, OpenAI Prism) were verified in the September 2026 pass; re-check them only when a human asks, and keep their `(verify)` markers otherwise.
- If a vendor is acquired, rebranded, or shut down, mark the row clearly in `choose.md` and add an "alternatives" pointer (the September 2026 pass did this for Sora, ChatGPT Atlas, the Llama API, GitHub Models, Phind, Continue.dev, Roo Code, Windsurf→Devin Desktop, NotebookLM→Gemini Notebook, Le Chat→Mistral Vibe, Azure AI Studio→Microsoft Foundry, FutureHouse→Edison Scientific).
- Web access: vendor pricing pages frequently return 403 to `WebFetch` (Cloudflare/JS shells). The webcrawler agents should fall back to WebSearch for 2026-or-later third-party trackers and vendor blog announcements. Mark such items as Medium confidence with `(verify)` in the docs.
