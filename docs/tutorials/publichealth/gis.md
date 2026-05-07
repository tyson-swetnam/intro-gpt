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

### Step 0 — Set up agent rules

Agent rules act as a "pre-prompt" that shapes every response your AI coding agent gives in this session — think of them as standing instructions the model re-reads before each turn. For this 90-minute lab we'll use a tight, minimal ruleset so you can focus on the GIS work. The full, more rigorous **EigenPrompt** (the prompt that comes before all others) is collapsed below for after-class study.

!!! Tip "Why agent rules?"

    Different agents read different files: **Cline** picks up `.clinerules/` in your workspace, **Claude Code** reads `CLAUDE.md` at the project root, and most other coding agents (Cursor, Aider, Codex, etc.) read `AGENTS.md`. Drop the same content into whichever file your tool expects.

??? Clipboard "Copy/Paste — Minimal rules (use this for the lab)"

    ```markdown
    # Workshop agent rules

    - Use Python 3.10+ for all scripts; for the web preview, use plain HTML/CSS/JS with no build tools or bundlers.
    - Surface failures with clear, specific error messages. Never fabricate or hallucinate sample data — if a fetch fails, say so and stop.
    - Log every prompt and response to `prompts/NNN_<topic>.md` using zero-padded sequential numbering (e.g., `001_setup.md`, `002_fetch_data.md`).
    - Confirm with me before any destructive action: deleting files, overwriting existing files, or running `git push`.
    - To preview HTML locally, run `python -m http.server <port>` on a high random port (e.g., 8723, 9412) to avoid collisions.
    - For any data fetch, cite the source URL in a code comment immediately above the fetch call.
    ```

??? Tip "Full EigenPrompt (advanced — for after the workshop)"

    These are sometimes called an EigenPrompt — because they come before any other prompts. We are using Cline on VS Code, so we will create a unique Workspace Rules file; these are located in the `.clinerules` folder — clicking on the :material-scales: icon will take you to Cline Rules.

    ??? Clipboard "Copy/Paste"

        ```markdown
        **Eigenprompt: Rigorous Code Generation & Automated Validation**

        **Objective:** Generate [code for a specific function/module/class | architectural outline] for [project/feature description] with a focus on correctness, testability, maintainability, and automated verification via Cline Workspace Rules.

        **I. Code Generation Specifications:**

        1. **Functionality:**  
          - Clearly define input(s), output(s), and the intended behavior.
          
        2. **Language/Framework:**  
          - Specify the programming language and version clearly (e.g., Python 3.10, JavaScript ES2022, Go 1.18).

        3. **Dependencies:**  
          - Explicitly list external libraries or modules required.

        4. **Error Handling:**  
          - Define expected errors explicitly with handling methods (exceptions, error codes, fallbacks).

        5. **Performance Constraints (Optional):**  
          - Describe any important time or memory constraints clearly.

        6. **Code Style:**  
          - Follow defined style guides (e.g., PEP 8, Google Java Style).  
          - Clearly document non-obvious or complex logic concisely, specifying reasons ("why") and behavior ("what").

        **II. Testing & Validation Requirements:**

        1. **Unit Tests:**  
          - Specify testing framework explicitly (e.g., unittest, Jest, Mocha).  
          - List and implement critical test cases clearly:
            - Typical valid inputs.
            - Edge cases.
            - Invalid inputs and related error-handling tests.
          - Indicate desired code coverage clearly [% of coverage as applicable].

        2. **Validation Criteria:**  
          - Clearly describe measurable criteria for successful test results.  
          - Specify validation datasets, criteria, or methods if needed.

        **III. Automated Execution, Validation, and Bug-Fixing Workflow (Cline Workspace Rules):**

        1. **Terminal Execution Validation:**
          - After execution of generated code or tests via ChatGPT API in VS Code Terminal, automatically inspect the outputs.
          - Verify explicitly that the commands have exited without errors or warnings.

        2. **Error & Warning Inspection:**
          - Check VS Code's "Problems" pane for reported errors, warnings, or alerts promptly after running code or tests.

        3. **Automated Re-examination on Errors:**
          - In case of any detected terminal output issues or problems pane alerts:
            - Automatically re-inspect the relevant code and identify root causes clearly.
            - Promptly propose corrected or improved code, addressing identified issues directly.
            - Re-run tests and terminal commands, verifying fixes iteratively until no critical issues persist.

        4. **Final Confirmation:**
          - Explicitly confirm successful execution (no persistent errors or warnings) before finishing the task.

        **IV. Project Structure & Documentation (Initialize/Update):**

        1. **`README.md`:**
          - **Project Title:**
          - **Description:** Succinct description.
          - **Setup Instructions:** Clearly outlined installation and execution steps.
          - **Usage:** Simple demonstration or examples.
          - **Testing Instructions:** Exact commands to run provided unit tests.

        2. **`prompts/` directory:**
          - Log initial eigenprompt clearly as `prompts/001_initial_eigenprompt.md`.
          - Log ChatGPT API's full responses (code, documentation, README) as `prompts/001_response.md`.
          - Future interactions follow sequential convention (e.g., `002_refinement_prompt.md`, `002_response.md`).

        **V. Output Format (Concise & Complete):**

        - Clearly named source code files according to module criteria (e.g., `module_name.py`).
        - Clearly named unit test files aligned with testing framework (e.g., `test_module_name.py`).
        - Complete and concise README.md file content.
        - Confirmation that automated validation via Cline Workspace Rules has executed successfully or corrections documented explicitly.
        - Confirmation of structured prompt logging.

        ---

        **Illustrative Usage Example:**

        **Objective:** Generate efficient Python code for calculating Fibonacci numbers with memoization, fully tested and automatically validated via Cline Workspace Rules.

        - **Code Specifications:**
          - Input: non-negative integer `n`; Output: nth Fibonacci number.
          - Use memoization for efficiency, with clear descriptive comments.
          - Error Handling: Raise explicit `ValueError` on negative input.
          - Python version: 3.10; Adhere strictly to PEP 8 style.

        - **Unit Testing:**
          - Framework: `unittest`.
          - Test cases: `fib(0)`→`0`, `fib(1)`→`1`, `fib(10)`→`55`, `fib(20)`→`6765`; negative inputs raise `ValueError`.

        - **Automated Validation (Cline Workflow):**
          - Upon running tests in terminal through ChatGPT API integration with VS Code, check terminal output immediately.
          - Automatically examine the "Problems" pane for errors or warnings.
          - If issues detected, automatically re-inspect code, clearly identify and implement fixes, and iteratively rerun validation steps until no problems remain.

        - **Project Structure & Logs:**
          - Create README.md, `prompts/` structure and log prompts/responses precisely as described.

        - **Final Output:**
          - Files: `fibonacci.py`, `test_fibonacci.py`, `README.md`.
          - Explicit confirmation that code and tests execute without errors or warnings and validation is automated successfully.
        ```

Want to go deeper? See [Writing Prompts](../../prompts.md) and [Vibe Coding](../../vibe.md) for more on shaping agent behavior.

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
