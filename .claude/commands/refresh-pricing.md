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

Dispatch **7 parallel `webcrawler` sub-agents** — one per vendor cluster. Each agent must:
- Try the official pricing page first.
- Fall back to WebSearch for recent (current-year) third-party pricing trackers and vendor blog announcements when the official page returns a 403/JS-only shell.
- Output a structured report per plan: `Price / Source URL / Fetched / Confidence (high|medium|low) / Notes`.
- End with a `Change summary` listing matches-vs-changes against the existing docs.

**Vendor clusters** (mirror what the May 2026 refresh used; adjust if vendors have come or gone):

1. **Anthropic** — claude.ai consumer plans (Free/Pro/Max/Team Standard/Team Premium/Enterprise) + API per-1M-token rates for Opus/Sonnet/Haiku tiers + caching/batch discounts. Sources: `anthropic.com/pricing`, `claude.com/pricing`, `docs.claude.com`.
2. **OpenAI** — ChatGPT consumer plans (Free/Go/Plus/Pro variants/Team/Enterprise/Edu) + OpenAI API per-1M-token rates + Sora bundling/credits. Sources: `openai.com/chatgpt/pricing`, `openai.com/api/pricing`, `platform.openai.com/docs/pricing`.
3. **Google** — Google AI Plus/Pro/Ultra/Ultra Lite consumer plans + Gemini API rates + Veo per-second + NotebookLM. Sources: `gemini.google/subscriptions`, `ai.google.dev/pricing`, `notebooklm.google/plans`.
4. **Microsoft + GitHub** — GitHub Copilot Free/Pro/Pro+/Business/Enterprise + Microsoft 365 Copilot Pro/Business/Enterprise + Azure-hosted OpenAI offering's current branding. Sources: `github.com/features/copilot/plans`, `microsoft.com/en-us/microsoft-365-copilot/pricing*`, Microsoft product-terms pages.
5. **Multi-AI access** — Perplexity, You.com, Poe, HuggingFace, NotebookLM Plus, DeepSeek, Grok/xAI, Mistral. Sources: each vendor's `/pricing` page; cross-check with third-party trackers.
6. **Coding tools** — Cursor, Windsurf (formerly Codeium), Replit, Phind (verify still active), Tabnine, Aider. Note acquisitions or shutdowns.
7. **Image/video gen** — Midjourney, Adobe Firefly, Runway, Sora, Veo, Imagine with Meta, Craiyon, Stability AI.

Each webcrawler should not edit any files.

## Phase C — Apply updates (parallel general-purpose agents)

Dispatch **4 parallel general-purpose sub-agents** — one per file cluster — and pass each agent the verified pricing data it needs. Tell each agent to:
- Edit in place, do NOT commit/push.
- Use `(verify)` markers inline next to medium-confidence numbers.
- Preserve canonical external identifiers (HuggingFace repo names, paper titles, citation-style refs).

**File clusters:**

1. `docs/choose.md` — heaviest file. Update every vendor row in the comparison tables. Update the two "verified [Month Year]" stamps. Mark any discontinued tools clearly.
2. `docs/chatgpt.md` + `docs/claude.md` + `docs/claude-code.md` — vendor pages with detailed pricing blocks and API rate tables.
3. `docs/gemini.md` + `docs/index.md` + `docs/vscode.md` + `docs/rag.md` — Google subscriptions, homepage subscription summary, Copilot pricing in vscode.md, RAG comparison table.
4. `docs/ai_landscape.md` + `docs/tutoring.md` + `docs/daily-productivity.md` + `docs/admissions.md` + `docs/plagiarism.md` + `docs/teaching.md` + `docs/gradio.md` + any other file with a stale stamp. Update stamps only; add a "not re-verified [Month Year]" caveat for sections with edu/plagiarism/research-tool pricing that this round did not verify.

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
2. Stage only the changed `docs/*.md` files — do not stage anything outside `docs/`.
3. Commit with a message that summarizes:
   - High-confidence price changes applied
   - Medium-confidence items marked `(verify)`
   - Stamps refreshed from old → new
   - Out-of-scope tool categories
4. Push to the target branch with `git push -u origin <branch>`.
5. Ask the user whether to open a PR. Default to opening one, base `main`.

## Notes

- This workflow is the canonical pricing-refresh runbook. It was first executed in May 2026 (commit `3743ab1`). When prices drift again, re-running this command should produce the next month's refresh.
- Out of scope by design: edu tools (Magic School AI, Education Copilot, IXL, Codecademy, Brilliant, MasterClass, Coursera), plagiarism detectors (GPTZero, Originality.AI, Turnitin, Copyleaks, Winston, Scribbr, PaperPal), academic research tools (Elicit, Consensus, Scite, ScholarAI). These have their own update cycles; covering them would multiply the webcrawl fan-out.
- If a vendor is acquired, rebranded, or shut down, mark the row clearly in `choose.md` and add an "alternatives" pointer (the May 2026 pass did this for Phind, Codeium→Windsurf, Azure OpenAI Service→Microsoft Foundry).
- Web access: vendor pricing pages frequently return 403 to `WebFetch` (Cloudflare/JS shells). The webcrawler agents should fall back to WebSearch for 2026-or-later third-party trackers and vendor blog announcements. Mark such items as Medium confidence with `(verify)` in the docs.
