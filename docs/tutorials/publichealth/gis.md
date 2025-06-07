# Vibe coding a Public Health Map

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! Info "Setup"


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

    **:simple-qgis: QGISMCP**

    [:material-github: https://github.com/jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp){target=_blank}

## Prompt Engineering & Vibe Coding

> The goal of this lab is to guide your LLM agent (Claude, Cline, etc.) through a reproducible workflow that turns open geospatial data into an interactive **story map**.  
> Copy-and-paste the prompts below in order. Adjust ONLY the bracketed values (`<…>`) to match your environment.  

### Prerequisites (checklist)

| ✔︎ | Requirement | Notes |
|---|-------------|-------|
|   | Frontier-class LLM access (API or Desktop) | Claude 4, GPT-4.5, Gemini 2.5 Pro, etc. |
|   | IDE with Cline or Roo Code extension **or** Claude Desktop | Enables local tool use & file ops |
|   | Filesystem MCP server running | Gives the AI read/write access |
|   | Git & GitHub account (optional but recommended) | For version control & sharing |

---

### Step 0 – Add a System Instruction or Workspace Rules file.

These are sometimes called an EigenPrompt -- because they come before any other prompts.

??? Tip "EigenPrompts"

    We are using Cline on VS Code, so we will create a unique Workspace Rules file, these are located in the `.clinerules` folder -- clicking on the :material-scales: icon will take you to Cline Rules 

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

---

### Step 1 – Initialize project folders

```text
TASK
Create the following directory structure in the current repo  
  data/  
  map/  
  code/  
  prompts/
Acknowledge when folders exist.
```

---

### Step 2 – Download & unzip “snow” dataset

```text
TASK
1. Download https://geodacenter.github.io/data-and-lab/data/snow.zip into data/  
2. Unzip it in place, then delete the original .zip  
3. Write a brief summary of extracted files 

Use Python scripting; save the script as code/download_data.py
```

---

### Step 3 – Organize GeoJSON layers

```text
TASK
In the unzipped snow dataset, locate every *.geojson file.  
Move the .geojson files into the map/ folder

Ignore all other file types.  

Confirm moves as successful.
```

---

### Step 4 – Summarize accompanying PDFs

```text
TASK
Within data/snow/, there are several PDF documentation files.

1. Extract their plain-text content and generate a markdown summary (≤ 200 words) of key variables & metadata.  
2. Save these markdown text as data/snow_docs_summary.md
```

---

### Step 5 – Build a storytelling Leaflet map

```text
TASK
Using Leaflet HTML, CSS, and JavaScript, create  
  map/snow_storymap.html
Requirements:
  • The HTML must scroll like a Story Map,
  • Layers appear when scrolled to and disappear when they are scrolled past
  • Summarized text explains the relevance and meaning of each data set
  • Use chloropleth colors for presence or absence of observations, such as 'deaths' and 'deathdens' for deaths and death density
  • add the death count to polygons but not point layers
  • Run local python web server on a high random port (e.g., 51234) to avoid conflicts  
```

---

### Step 6 – Iterate for aesthetics

```text
TASK
Open map/snow_storymap.html and critique its look (colors, fonts, layout).  
Suggest up to three improvements.  
Wait for user approval, then implement changes inside the same file.
```

---

### Step 7 – Log every prompt

```text
TASK
Create code/log_prompts.py that appends each user & assistant message  
from this session into prompts/session_<timestamp>.md  
Ensure it runs automatically at the end of each assistant response.
```

---

### Step 8 – Commit & push

```text
TASK
Git add all new/modified files  
Commit with message "Add snow GIS story-map lab"  
Push to <your-GitHub-remote>  
Report the commit URL on success.
```

---

### Step 9 – One Shot Prompt

Now, try a new chat session and let's push everything through at once to see how it turns out:

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

### Next Steps

• Modify the prompts to use **QGISMCP** and build the layers there.

• Deploy the code and map via GitHub Pages.
