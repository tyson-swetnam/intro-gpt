# Vibe coding a Public Health Map

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! Example "What you'll build (90 min)"
    A scrolling Leaflet story-map of the 1850 London cholera outbreak,
    served locally at http://localhost:51234. By minute 60 you should
    see the Broad Street pump and the death-density choropleth on screen.

??? Info "Setup (click to expand if you haven't installed tools yet)"

    Pick whichever agent surface you have access to — the prompts in this lab are platform-neutral and work with any modern AI coding agent. You'll want **at least one** from each row below.

    !!! Success "Desktop LLM apps"

        - **Claude Desktop** (:material-microsoft-windows: Windows, :material-apple: Mac OS) — [claude.ai/download](https://claude.ai/download){target=_blank}
        - **Codex Desktop** (ChatGPT) — [chat.openai.com/codex](https://chat.openai.com/codex){target=_blank}
        - **Perplexity Computer** (Comet) — [perplexity.ai/comet](https://www.perplexity.ai/comet){target=_blank}

    !!! Success "CLI agents"

        - **Claude Code** — [claude.ai/code](https://claude.ai/code){target=_blank}
        - **Codex CLI** — [github.com/openai/codex](https://github.com/openai/codex){target=_blank}
        - **Gemini CLI** — [geminicli.com](https://geminicli.com/){target=_blank}

    !!! Success "AI-native IDEs"

        - **VS Code** (:material-microsoft-windows: Windows, :material-apple: Mac OS, :simple-linux: Linux) — [code.visualstudio.com/download](https://code.visualstudio.com/download){target=_blank}
        - **Cursor** — [cursor.com](https://cursor.com/){target=_blank}
        - **Antigravity** (Google) — [antigravity.google](https://antigravity.google/){target=_blank}

## Prompt Engineering & Vibe Coding

> The goal of this lab is to guide your AI coding agent (Claude Code, Codex, Gemini CLI, Cursor, etc.) through a reproducible workflow that turns open geospatial data into an interactive **story map**.  
> Copy-and-paste the prompts below in order. Adjust ONLY the bracketed values (`<…>`) to match your environment.  

### Prerequisites (checklist)

| ✔︎ | Requirement | Notes |
|---|-------------|-------|
|   | Frontier-class LLM access | Claude, GPT, Gemini Pro, or equivalent |
|   | One agent surface from the Setup list above | Desktop, CLI, or AI-native IDE — pick what you know |
|   | [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) running | Gives the agent read/write access. **Without this, Step 1 will fail silently.** |
|   | Git & GitHub account (optional but recommended) | For version control & sharing |

---

### Step 0 — Set up agent context files

Modern AI coding agents read project-level context files at the start of each session. The exact filename varies by platform — `CLAUDE.md` for Claude Code, `AGENTS.md` for Codex / Cursor / most others, `GEMINI.md` for Gemini CLI — but the content is identical. Three files cover the workspace:

| File | Purpose |
|------|---------|
| `CLAUDE.md` (or `AGENTS.md`, `GEMINI.md`, `CODEX.md`) | Workspace rules and conventions |
| `Skills.md` | Reusable, named playbooks the agent can invoke |
| `Memory.md` | Persistent project facts that survive across sessions |

Drop the same content into whichever filename your agent expects. Create all three at the project root before running Step 1.

??? Clipboard "CLAUDE.md / AGENTS.md / GEMINI.md — workspace rules"

    ```markdown
    # Project: Public Health Map Lab

    ## Stack
    - Python 3.10+ for scripts
    - Plain HTML / CSS / JS for the web map (no bundlers, no frameworks)
    - Leaflet for mapping

    ## Conventions
    - Save scripts to `code/`, raw data to `data/`, maps to `map/`
    - Log every prompt and response to `prompts/NNN_<topic>.md`
    - Cite source URLs in code comments for any data fetch

    ## Guardrails
    - Confirm before destructive actions (delete, overwrite, `git push`)
    - Never fabricate sample data — surface failures clearly and stop
    - Run a local web server on a high random port for HTML preview
    ```

??? Clipboard "Skills.md — reusable playbooks"

    ```markdown
    # Skills available in this workspace

    ## /scaffold
    Create the `data/`, `map/`, `code/`, `prompts/` folder structure at the project root.

    ## /fetch-snow
    Download <https://geodacenter.github.io/data-and-lab/data/snow.zip> into `data/`,
    unzip, and move every `*.geojson` into `map/`.

    ## /storymap
    Generate `map/snow_storymap.html` using Leaflet with scrolly layout, choropleth
    on `deaths` and `deathdens`, and per-layer narrative captions.

    ## /critique
    Open the current storymap, identify up to three improvements
    (colors, fonts, scroll feel), wait for approval, then apply in place.
    ```

??? Clipboard "Memory.md — persistent project facts"

    ```markdown
    # Project memory

    - Deliverable: `map/snow_storymap.html`, served at http://localhost:51234.
    - GeoJSON field names: `deaths` (count), `deathdens` (density per polygon area).
    - Death-count labels go on polygon layers only — NOT on point layers.
    - The PI prefers per-layer narrative captions over a single overview block.
    - Story context: 1850 London cholera outbreak; the Broad Street pump is the central feature.
    ```

Want to learn how skills, subagents, and memory work? See [Agentic AI](../../agentic.md) and [Claude Code Workflow](../../claude-code.md).

---

### Step 1 — Scaffold project + fetch data

We'll combine folder creation, dataset download, and GeoJSON sorting into a single prompt. **Open the folder you want to work in before running this prompt** — the agent creates everything relative to your current workspace.

```text
TASK
1. Create folders: data/, map/, code/, prompts/
2. Download https://geodacenter.github.io/data-and-lab/data/snow.zip into data/
3. Unzip in place, delete the .zip
4. Move every *.geojson file from the unzipped folder into map/. Ignore __MACOSX and non-geojson files.
5. Save the script as code/setup.py and confirm each step.
```

!!! Warning "If the download fails"
    Grab the zip from the instructor share, or download it via your browser and drop it into `data/` manually before re-running the script.

---

### Step 2 — Build the storymap

This is the centerpiece. The agent will write the HTML/CSS/JS and serve it locally.

```text
TASK
Create map/snow_storymap.html using Leaflet (HTML/CSS/JS).

Layout:
  - Scrolly story-map, mobile + desktop
  - Each GeoJSON layer in map/ appears on scroll, disappears when past
  - Short narrative caption per layer (1850 cholera context)

Data styling:
  - Choropleth on 'deaths' and 'deathdens'
  - Death-count labels on polygons only (NOT points)

Serve:
  - Run `python -m http.server 51234` and open in browser
```

!!! Warning "If the agent stalls or the map renders blank"
    Skip ahead to Step 4 (one-shot) and let the agent rebuild from scratch. If port 51234 is already in use, ask the agent to pick another 5-digit port.

!!! Tip "If a field is missing"
    If `deathdens` isn't in the GeoJSON, ask the agent to compute it from `deaths` divided by polygon area.

---

### Step 3 — Iterate aesthetics

Critique the agent's output and ask for targeted improvements. Time-box this loop to 10 minutes.

```text
TASK
Open map/snow_storymap.html. Critique colors, fonts, and scroll feel.
Propose up to 3 improvements. Wait for my approval, then apply them in place.
```

!!! Tip "Running short on time?"
    Step 3 is the most cuttable; skip straight to Step 4 if you need to.

---

### Step 4 — One-shot reveal

Now open a fresh chat and paste the single prompt below. The pedagogical point is seeing the same workflow you just walked compressed into one prompt — that's the 2026 agent superpower.

!!! Note "Yes, the prompt has typos"
    The numbering jumps (two `6.`s) and "chloropleth" is misspelled. Both are preserved from the original 2025 lab on purpose — modern agents handle messy real-world prompts surprisingly well, and it's worth seeing that for yourself.

```text
The goal for this project is to create a story map that tells the story of 1850's the cholera outbreak in London. We will use HTML, JS, CSS, and Python for the code. 


First task,

1. Download https://geodacenter.github.io/data-and-lab/data/snow.zip into a new folder called `data/`  
2. Unzip the .zip file in place, then delete the .zip  
3. Write a short summary in MarkDown of the steps to this in the `data/` folder.

Second task,

4. In the unzipped dataset, locate every *.geojson file.  
5. Move the .geojson files into a new `map/` folder. Ignore the data in the __MACOSX folder. Ignore all other file types.

Third task,

6. Summarize accompanying PDFs in the `data/` folder and save the summaries in a new MarkDown file.

Final task,

6. Build a scrolling story telling map. Using Leaflet, HTML, CSS, and JavaScript, create a `map/snow_storymap.html` which will read the GeoJSON files we got earlier.

Requirements:
  • The HTML must scroll like a Story Map that is effective both on mobile and desktop
  • the layers should appear when scrolled over and disappear when they are scrolled past
  • Use the summarized text to explain the relevance and meaning of each data set in the context of the larger story
  • Use chloropleth colors for presence or absence of observations, such as 'deaths' and 'deathdens' for deaths and death density
  • add the death count to polygons as labels, but to the not point layers
```

Compare this output to what you built across Steps 1–3. Where did the agent do better with all-at-once context? Where did it cut corners?

---

## Optional Homework

Each link below extends a step we trimmed from the live lab — pick whichever interests you and run it on your own.

### Sharpen your prompts

- [Writing Prompts](../../prompts.md) — extends Step 0 with the structure behind well-engineered prompts.
- [Vibe Coding](../../vibe.md) — deeper patterns for the iterate-with-the-agent loop you used in Step 3.

### Bring documents into the workflow

- [Text Mining](../../text_mining.md) — replaces the cut PDF-summary step with a richer document workflow.
- [RAG](../../rag.md) — extends the storymap with retrieval over the cholera PDFs and other primary sources.

### Automate the workflow

- [Claude Code Workflow](../../claude-code.md) — covers the prompt-logging and session-automation step we skipped.
- [Agentic AI](../../agentic.md) — frames the agent loop you just used.

### Ship and extend the map

- [VS Code & AI Tools](../../vscode.md) — covers the git commit/push step and IDE ergonomics.
- [MCP](../../mcp.md) — required reading before trying QGISMCP for richer layer styling.
- [Public Health AI Lab](./casestudy.md) — applies prompt-engineering techniques to SMS triage, outbreak synthesis, and chart abstraction.

## Next Steps

- Modify the prompts to use [QGISMCP](https://github.com/jjsantos01/qgis_mcp) and build the layers there.
- Deploy the code and map via [GitHub Pages](https://pages.github.com/).
