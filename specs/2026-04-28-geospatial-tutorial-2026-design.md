# Geospatial Tutorial 2026 — Design

**Status:** Draft for review
**Date:** 2026-04-28
**Author:** Tyson Swetnam (with Claude)
**Workshop slot:** Public Health & AI Summer School 2026 — Tue June 9, 10:30 AM, AI Fluency track, 90 minutes
**Predecessor:** `docs/tutorials/publichealth/gis.md` (the 2025 lab — kept as historical artifact, renamed)

---

## 1. Goal

Replace the 2025 "Vibe coding a Public Health Map" lab with a 2026 version that:

1. Demonstrates what is *technically new* about driving an AI agent through geospatial work in 2026 vs 2025 (the AI Fluency promise — leave knowing how to drive an agent, not just how to type a prompt).
2. Lets students choose one of four public-health stories to work on, each exercising a different "new in 2026" capability.
3. Reuses the instructor's existing MCP servers (`envirofacts-mcp`, `aqs-mcp`) and web app (`wind-html`) so the tutorial is grounded in current research outputs that DUST Center attendees will already recognize.
4. Keeps the 2025 lab visible as the "look how much changed in a year" reference point.

**Non-goals:**
- Teaching tool/IDE setup. The broader `intro-gpt/` workshop covers Claude Code, Claude Desktop, Codex CLI, Cursor, Gemini Antigravity, Codespaces, and CyVerse. This tutorial assumes that work is done.
- Producing real epidemiological findings. Outputs are demonstrations.
- Teaching students to write their own MCP server. We use existing ones; "you could write one too" is a gesture, not a lesson.
- Privacy-sensitive data. All datasets are public-aggregated.
- Continuous deployment. One-shot push to `gh-pages` only.
- Auto-grading or assessment.

---

## 2. Audience & assumptions

- **Track:** AI Fluency (advanced, ready to build/deploy).
- **Cap on time:** 90 minutes, hard.
- **Pre-arrival state we can require:**
  - Python 3.11+, Node 20+, Git, GitHub account (personal — no workshop org).
  - One agent surface ready. Two tiers:
    - **Demoed by instructor (live):** Claude Code, Claude Desktop.
    - **Supported alternates with full MCP parity:** Codex CLI, Cursor, Gemini Antigravity. The five together — Claude Code, Claude Desktop, Codex CLI, Cursor, Gemini Antigravity — are what the per-tool prompt tabs and MCP-config snippets cover.
    - **Light support:** ChatGPT Desktop (Custom GPT / Agent Mode / Code Interpreter). Prompts still work, but MCP config and on-disk project layout don't apply the same way; track pages note "if you're on ChatGPT Desktop, use Code Interpreter and skip the MCP cells."
  - AI-VERDE API key issued by the workshop.
  - CyVerse account (workshop-provisioned).
- **Pre-arrival state we provide:**
  - CyVerse environment image with all five tools, MCPs, and pre-cached fallback datasets installed.
  - AI-VERDE-routed key for Anthropic / OpenAI / Google models.
  - Setup pages updated to 2026 standard in the broader `intro-gpt/` workshop site.

---

## 3. Pacing (90 minutes)

| Minutes | Phase | Mode | Output by end of phase |
|---|---|---|---|
| 0–10 | Warm-up Phase 1: "Hello, Arizona" baseline map | Synchronous, instructor-led | Every student has a working Maplibre+OSM map of AZ counties + a `~/ph-ai-2026/` project repo |
| 10–30 | Warm-up Phase 2: Discovery agent → data plan | Synchronous, students drive their own agent on their chosen track topic | Every student has `notebooks/<track>_data_plan.ipynb` with top-three sources for their track |
| 30–75 | Track work | Independent, instructor + helpers float | Every student has a published storymap + a track-specific notebook + (Toxic Dust only) a forked web app |
| 75–87 | Show-and-tell | 4 volunteers × ~3 min, one per track | Audience sees one example from each track |
| 87–90 | Closer | Instructor side-by-side of 2025 storymap vs a 2026 student's storymap | Workshop ends with the comparison narrative |

The 30/45/15 split is chosen because the 30-min shared section surfaces tooling problems before students are isolated in track work, and produces a non-trivial first deliverable that the track section *extends* rather than starts from.

---

## 4. File & nav layout

### New files
```
docs/tutorials/publichealth/maps/
├── index.md            # Parent: framing, prereqs, 30-min warm-up, "pick a track" router, closer
├── heat.md             # Track 1
├── smoke.md            # Track 2
├── toxic-dust.md       # Track 3
└── snow-2026.md        # Track 4
```

### Modified files
- `docs/tutorials/publichealth/gis.md` → renamed to `gis-2025.md`. Top of the file gets a banner admonition pointing to the new 2026 tutorial as the current canonical lab and framing this file as a historical artifact.
- `zensical.toml` nav under `Tutorials` updated:
  ```
  Tutorials = [
    { "Claude Code Workflow" = "claude-code.md" },
    { "Public Health" = "tutorials/publichealth/casestudy.md" },
    { "Mapping (2026)" = "tutorials/publichealth/maps/index.md" },
    { "Mapping (2025, archive)" = "tutorials/publichealth/gis-2025.md" },
  ]
  ```

### Style conventions
- Follow the existing `gis.md` admonition style (`!!! Info`, `!!! Success`, `!!! Tip`, `??? Clipboard "Copy/Paste"`, etc.) so the new pages feel native to the site.
- Use `pymdownx.tabbed` for any "if you're using Claude Code vs Claude Desktop vs Codex vs Cursor vs Antigravity" prompt variants — one tabbed block per multi-tool prompt.
- Use Mermaid for any sequence diagrams (the parent page may want one for the overall flow).

---

## 5. Tracks

All four tracks share the same "spine" (agentic workflow driven from one of the supported tools) but each exercises a different new capability.

### 5.1 Track 1 — Heat (`heat.md`)

| Field | Value |
|---|---|
| Story | "Where in Arizona is heat risk highest, and who is socially vulnerable to it?" |
| New-in-2026 superpower | Cloud-native geospatial: STAC catalog search and Cloud-Optimized GeoTIFF (COG) windowed reads, all driven by an agent that has never seen these specific datasets before. |
| Data sources | NWS HeatRisk API (current/forecast), PRISM or Daymet temperature via Microsoft Planetary Computer STAC, CDC/ATSDR Social Vulnerability Index (SVI), ACS demographics via Census API, AZ tract boundaries (TIGER). |
| Tools / MCPs | filesystem MCP, github MCP, fetch MCP. Python: `pystac-client`, `rioxarray`, `xarray-spatial`, `geopandas`. |
| Per-track artifact (on top of shared storymap + notebook) | A bivariate-color map (heat × SVI) at AZ tract resolution; notebook documents STAC search → COG window-read → zonal stats. |

### 5.2 Track 2 — Smoke (`smoke.md`)

| Field | Value |
|---|---|
| Story | "How does wildfire smoke move across Arizona in real time, and who is most exposed?" |
| New-in-2026 superpower | Live APIs + auto-refresh. The agent writes a small Python poller and a front-end that updates as new data arrives. |
| Data sources | AirNow API, PurpleAir API, NOAA HMS smoke polygons, OpenAQ. |
| Tools / MCPs | filesystem MCP, github MCP, fetch MCP. Python: `requests`, `pandas`, `folium`/`maplibre`. |
| Per-track artifact | Time-animated map with `setInterval` refresh; notebook with API exploration + a tract-level exposure calc. |

### 5.3 Track 3 — Toxic Dust (`toxic-dust.md`)

| Field | Value |
|---|---|
| Story | "What's in the dust over Arizona — Superfund tailings, mining disturbance, Valley Fever spores — where does the wind take it, and who breathes it?" |
| New-in-2026 superpower | Multi-MCP orchestration: agent uses *specialty scientific* MCP servers (the instructor's own) plus filesystem/github, then forks an existing web app and customizes it. The lesson: "you can write your own MCPs to turn agency APIs into agent tools, then remix existing visualizations." |
| Default demo region | **Morenci, AZ** (Greenlee County). Morenci Mine is one of the largest North-American open-pit copper operations and a real-world Superfund + dust source. Students may swap to another AZ region; the prompt has a bracketed `<region>` placeholder. |
| Data sources | EPA Envirofacts (Superfund + facility + violations) via `envirofacts-mcp`. EPA AQS PM2.5 / PM10 monitor timeseries via `aqs-mcp`. NOAA GFS wind via `wind-html` upstream. Optional: ADHS Valley Fever county CSV. |
| Tools / MCPs | `envirofacts-mcp`, `aqs-mcp`, filesystem MCP, github MCP, fetch MCP. The two custom MCPs are pre-installed on the CyVerse image and pre-configured in the supported agent tools' settings files. |
| Per-track artifact | A forked `wind-html`-style site, **rebased on Maplibre + OSM tiles** (no Mapbox token), centered on the chosen region, with a Superfund layer (from `envirofacts-mcp`), AZ AQS PM2.5/PM10 layer (from `aqs-mcp`), wind animation, and an optional Valley Fever county overlay. Deployed to `gh-pages` on the student's personal GitHub. |
| Upstream-flexibility plan | Track page never hard-codes filenames or class names from `wind-html`. The agent's prompt says "fetch the current README and source from `https://github.com/tyson-swetnam/wind-html` and adapt to whatever's there." A "Plan B" cell tells the agent to build a from-scratch Maplibre page using the two MCPs if the upstream repo has changed substantially. |
| Mapbox-token security note | Track page calls out *why* we swap to Maplibre+OSM (token leak risk in a public fork) so students learn the lesson, not just the swap. |

### 5.4 Track 4 — John Snow 2026 (`snow-2026.md`)

| Field | Value |
|---|---|
| Story | "What does a 2026 agent do with the same data we used in 2025? What's actually different?" |
| New-in-2026 superpower | Agentic comparison: one shot vs. nine prompts. The student watches the agent's plan-mode trace and writes an honest critique. |
| Data sources | Same `snow.zip` from the 2025 lab (https://geodacenter.github.io/data-and-lab/data/snow.zip). |
| Tools / MCPs | filesystem MCP only. Deliberately minimal — the point is the agent's reasoning, not its tool kit. |
| Per-track artifact | Side-by-side page: 2025 lab's nine-step output rendered in iframe vs 2026 one-shot output rendered in iframe. Notebook contains the agent's plan-mode trace and an honest critique noting where the 2026 agent did better, where it made the same mistakes, and where it made *new* mistakes a 2025 agent wouldn't have. |

### 5.5 Per-track page skeleton (every track follows this shape)

1. **Why this story** — 3–5 sentences of public-health framing.
2. **What you'll have at minute 75** — screenshot + bullet list of artifacts.
3. **Pre-flight check** — 3 bullets confirming "you have X, Y, Z from the warm-up."
4. **The track's "wow" prompt** — a single, well-engineered prompt with bracketed `<…>` values as the only edit points. Wrapped in `pymdownx.tabbed` blocks for the five tool variants.
5. **Iteration prompts** — 3–5 follow-up prompts to refine (error handling, styling, deploy).
6. **Show-and-tell prep** — 1 sentence on what to demo.
7. **If you finish early** — stretch goal (usually swap region or add a layer).
8. **Caveats & honest limits** — what the agent will get wrong, what to sanity-check. (This section is largest in Toxic Dust because EPA-data interpretation is hallucination-prone.)

---

## 6. Common scaffolding

### 6.1 The 30-min warm-up on `index.md`

#### Phase 1 (0–10): "Hello, Arizona" baseline

Single prompt, identical across all five tools:

> Initialize a new project at `~/ph-ai-2026/` with subfolders `data/`, `code/`, `notebooks/`, `outputs/`, `prompts/`. Then build a Maplibre + OSM HTML page (`outputs/hello-az.html`) showing Arizona county boundaries fetched from the U.S. Census TIGER cartographic boundary file (state FIPS 04). Serve it on `localhost:51234` with Python's `http.server`. Save the prompt and a brief plan to `prompts/001_hello_az.md`. Confirm when the page renders.

Outcome at min 10: every student has a project repo + a working AZ counties map + their tooling proven good.

#### Phase 2 (10–30): Discovery agent → data plan

Student picks a track topic and runs:

> Survey the data sources we could use to tell a `<heat | smoke | toxic-dust | john-snow-2026>` public-health story for Arizona. For each candidate source: name, URL, license, geographic granularity, temporal range, access method (REST, STAC, MCP, CSV download), and one risk. Write the result to `notebooks/<track>_data_plan.ipynb` with a final-cell summary table and a recommended top-three sources. Don't download anything yet — this is the plan, not the execution.

Outcome at min 30: every student has a per-track data plan their track page picks up.

### 6.2 Project template (created in Phase 1)

```
~/ph-ai-2026/
├── README.md             # student name, track, region of interest
├── AGENTS.md             # shared agent rules — see §6.3
├── CLAUDE.md             # symlink (or copy on Windows) of AGENTS.md
├── .clinerules           # mirror of AGENTS.md (Cline reads this name)
├── data/                 # raw inputs (gitignored if big)
├── code/                 # scripts (download, ETL)
├── notebooks/            # analysis + the data plan
├── outputs/              # storymap HTML, screenshots, exported maps
├── prompts/              # numbered prompt log (001_*.md, 002_*.md, …)
└── .env.example          # AI-VERDE endpoint + key, AirNow key, etc.
```

### 6.3 Single agent rules file (`AGENTS.md`)

Track-agnostic core conventions:

- Directory layout discipline.
- Prompt-logging requirement: every user/assistant turn is appended to `prompts/NNN_<topic>.md`.
- "Summarize the plan before executing" — the agent must propose a plan before running tools.
- Uncertainty-flagging: agent must use the phrase "I am not certain about X" when guessing API behavior, dataset semantics, or tool availability.
- "Don't fabricate data — flag if a fetch fails." The agent must never make up plausible-looking sample rows.
- "Always cite the source URL in code comments" for every API call.
- "Before calling a tool, list the tools you have access to and confirm the one you're about to use exists" — guards against hallucinated MCP tool names.
- "Output is a demonstration, not an analytical finding. Never imply causation." (Public-health framing safety.)

The same content lives at three filenames so all five tools see it without per-tool divergence:
- `AGENTS.md` — Codex CLI, Cursor, ChatGPT Desktop's Project rules, Gemini Antigravity.
- `CLAUDE.md` — Claude Code (CLI) and Claude Desktop's Project knowledge.
- `.clinerules` — Cline (VS Code extension).

### 6.4 MCP roster

| MCP | Used by | Notes |
|---|---|---|
| filesystem (official) | all tracks, warm-up | Default. |
| github (official) | all tracks (deploy step) | For pushing to `gh-pages`. |
| fetch (official) | all tracks | URL → content; lighter than browser. |
| `envirofacts-mcp` (Tyson's) | Toxic Dust | Superfund + facility + violations lookups. |
| `aqs-mcp` (Tyson's) | Toxic Dust + (optional) Smoke | EPA AQS PM2.5/PM10 timeseries. |
| QGIS-MCP | optional, advanced, any track | Mentioned in `index.md`, not required. |

`index.md` provides per-tool MCP configuration snippets (Claude Desktop's `claude_desktop_config.json`, Claude Code's `~/.claude/settings.json`, Codex equivalent, Cursor equivalent, Gemini Antigravity equivalent) listing only the MCPs needed for the picked track. Default snippet (filesystem + github + fetch) covers Heat / Smoke / Snow; Toxic Dust adds the two custom MCPs.

### 6.5 AI-VERDE & CyVerse callouts

Top of `index.md`:

> We assume you've completed the broader [intro-gpt/](../../../) setup. If not, here are the three pages you need: [Claude Code setup], [Claude Desktop + MCPs], [CyVerse environment]. The CyVerse image already has Python, Node, the MCPs, and pre-cached fallback datasets ready.

Code samples that hit an LLM API directly (rare in this lab — most calls go through the IDE/CLI agent) use the AI-VERDE endpoint as default with a comment showing how to swap to Anthropic / OpenAI direct.

---

## 7. Show-and-tell (75–87) and closer (87–90)

- 4 volunteers, one per track, ~3 minutes each. Each shows:
  1. Their published map / forked site (live).
  2. One notebook cell that captures something the agent figured out.
  3. One thing the agent got wrong that they had to correct.
- 3-min closer: instructor pulls up the 2025 `gis-2025.md` storymap next to a 2026 student's storymap and narrates the difference — "the workflow is fundamentally different," not "the maps look better."
- Not recorded.
- Optional Slack/Discord channel collects everyone's GitHub Pages URLs after the session.

---

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| API rate limits hit mid-warm-up | AI-VERDE caches/proxies where possible; warm-up uses Census TIGER only (no key, no rate limit); each track page has a "if rate-limited" cell with a pre-cached fallback dataset baked into the workshop CyVerse image. |
| Wifi flaky in the room | CyVerse fallback = browser-only, server-side network; pre-cached datasets cover all four tracks even fully offline. |
| Agent hallucinates a STAC/MCP tool that doesn't exist | `AGENTS.md` rule + discovery prompt require the agent to list tools and confirm. |
| Toxic Dust MCP install pain | First track-page cell is "verify both MCPs are connected" with a one-line ping per MCP. Failure path = "Plan B" using EPA APIs over plain HTTP via fetch MCP. |
| `wind-html` upstream changes between now and June 9 | Track 3 prompt fetches the current repo state and adapts. Page never hard-codes upstream filenames or class names. We smoke-test the track page in the week before the workshop. |
| Confident-nonsense from the agent on EPA data | `AGENTS.md` requires citing record IDs and an "I am not certain about X" admission. |
| Show-and-tell runs over | Hard-stop signal at 87 min. |
| Student finishes early | Each track page has an "If you finish early" stretch — usually swap region or add a discovered layer. |
| 2025 archive page becomes confusing | Top-banner admonition + nav label "Mapping (2025, archive)". |
| Mapbox token leak in a forked `wind-html` | Maplibre+OSM swap is part of the prompt; track page calls out the security reason for the swap. |

---

## 9. Decisions resolved

- Tracks: 4 (Heat, Smoke, Toxic Dust, John Snow 2026), choose-your-own.
- Tools: Claude Code + Claude Desktop are demoed; Codex CLI, ChatGPT Desktop, Cursor, Gemini Antigravity supported.
- Doc structure: parent `index.md` + 4 track pages under `docs/tutorials/publichealth/maps/`.
- Old `gis.md`: renamed to `gis-2025.md` with banner pointing forward.
- Pacing: 30 / 45 / 15.
- Pre-prep: students arrive with prereqs done; CyVerse + AI-VERDE provided as fallback.
- Warm-up: 10-min "Hello, Arizona" + 20-min discovery agent → data plan.
- Per-track form: shared storymap + notebook; Toxic Dust adds a forked `wind-html`-style site.
- Toxic Dust default region: Morenci, AZ (Greenlee County).
- Web-mapping stack for the lab: Maplibre + OSM (no Mapbox token).
- GitHub: students publish to personal accounts; no workshop org.
- No track pre-registration; no recording.

---

## 10. Open follow-ups (not blocking implementation)

- Smoke test the Toxic Dust track in the week before June 9 against the then-current `wind-html` upstream and against live EPA Envirofacts + AQS endpoints. If `wind-html` has changed substantially, refresh the prompt's expectations.
- Confirm with workshop registrar whether Slack or Discord is the preferred post-session channel for sharing GitHub Pages URLs.
- Review the `intro-gpt/` setup pages (Claude Code, Claude Desktop, Codex, Antigravity, Cursor, Codespaces, CyVerse) and update them to 2026 standard before this tutorial goes out — this is the larger-effort prompt-engineering update Tyson flagged as a separate work item.

---

## 11. Implementation outline (for the plan that follows this spec)

The implementation plan that succeeds this spec should produce, in order:

1. Rename `docs/tutorials/publichealth/gis.md` → `gis-2025.md` and add the top-of-file banner.
2. Update `zensical.toml` nav.
3. Create `docs/tutorials/publichealth/maps/index.md` (parent page: framing + 30-min warm-up + router + closer).
4. Create the four track pages:
   - `heat.md`
   - `smoke.md`
   - `toxic-dust.md`
   - `snow-2026.md`
5. Verify `zensical serve` builds without errors and all internal links resolve.
6. Smoke-test each track's "wow" prompt against the supported tools before the workshop (this can be a separate task closer to June 9).

The implementation work is documentation, not code. No Python or JS is shipped in the repo. The prompts in the docs *will* produce code when students run them, but that code lives in students' own repos.
