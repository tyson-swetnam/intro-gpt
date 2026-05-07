# Vibe coding a Public Health Map

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! Example "What you'll build (90 min)"
    A scrolling Leaflet story-map of the 1850 London cholera outbreak,
    served locally at http://localhost:51234. By minute 60 you should
    see the Broad Street pump and the death-density choropleth on screen.

??? Info "Setup (click to expand if you haven't installed tools yet)"

    **Minimum path for this lab:** VS Code + Cline extension + the [Filesystem MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem). Everything else below is alternative or optional.

    !!! Success "Desktop LLM Apps"
        
        !!! Success "Claude Desktop"

            (:material-microsoft-windows: Windows, :material-apple: Mac OS)

            Connects automatically to Anthropic Claude. 

            [:simple-claude: Claude Desktop https://claude.ai/download](https://claude.ai/download){target=_blank} 
            
        !!! Success "AnythingLLM Desktop"

            (:material-microsoft-windows: Windows, :material-apple: Mac OS, :simple-linux: Linux)

            [:material-infinity: AnythingLLM https://anythingllm.com/desktop](https://anythingllm.com/desktop){target=_blank} 

    !!! Success "Integrated Development Environment (IDE) Desktops"
    
        !!! Success ":material-microsoft-visual-studio-code: VS Code"

            (:material-microsoft-windows: Windows, :material-apple: Mac OS, :simple-linux: Linux)
            
            [:material-microsoft-visual-studio-code: https://code.visualstudio.com/download](https://code.visualstudio.com/download){target=_blank}

        !!! Success "Positron"

            [:simple-posit: https://positron.posit.co/](https://positron.posit.co/){target=_blank} 

        !!! Success "API Access"

            [:simple-claude: https://console.anthropic.com/](https://console.anthropic.com/){target=_blank}

    **Cline (:material-microsoft-visual-studio-code: VS Code Extension)** [:material-robot: https://cline.bot/](https://cline.bot/){target=_blank}

    **Optional: :simple-qgis: QGIS** [https://qgis.org/download/](https://qgis.org/download/){target=_blank}

    **:simple-qgis: QGISMCP** [:material-github: https://github.com/jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp){target=_blank}

## Prompt Engineering & Vibe Coding

> The goal of this lab is to guide your LLM agent (Claude, Cline, etc.) through a reproducible workflow that turns open geospatial data into an interactive **story map**.  
> Copy-and-paste the prompts below in order. Adjust ONLY the bracketed values (`<…>`) to match your environment.  

### Prerequisites (checklist)

| ✔︎ | Requirement | Notes |
|---|-------------|-------|
|   | Frontier-class LLM access (API or Desktop) | Claude 4, GPT-4.5, Gemini 2.5 Pro, etc. |
|   | IDE with Cline or Roo Code extension **or** Claude Desktop | Enables local tool use & file ops |
|   | [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) running | Gives the agent read/write access. **Without this, Step 1 will fail silently.** |
|   | Git & GitHub account (optional but recommended) | For version control & sharing |

---

### Step 0 — Skills & subagents

!!! Tip "Skills and subagents replace the old EigenPrompt"
    Earlier versions of this lab opened with a 120-line "EigenPrompt" workspace-rules file. Modern agentic IDEs (Claude Code, Cursor, Codex, Cline) replace that pattern with two composable extension surfaces:

    - **Skills** — reusable, model-invokable playbooks (e.g., `/review`, `/simplify`, `/init`) that activate only when relevant to the task at hand.
    - **Subagents** — focused helpers the main agent spawns to handle a discrete task (research, drafting, review) and report back.

    Both scale better than a single giant pre-prompt because they're scoped, named, and only fire when needed. For this 90-minute lab, lean on your agent's defaults and skip the custom rules file.

    Want to learn how to build your own? See [Agentic AI](../../agentic.md) and [Claude Code Workflow](../../claude-code.md).

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
- [Public Health Case Study](./casestudy.md) — applies the same agent skills to a different public-health problem.

## Next Steps

- Modify the prompts to use [QGISMCP](https://github.com/jjsantos01/qgis_mcp) and build the layers there.
- Deploy the code and map via [GitHub Pages](https://pages.github.com/).
