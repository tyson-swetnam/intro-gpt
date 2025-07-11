# Vibe Coding

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Vibe coding refers to using an LLM to generate and edit code directly within your IDE (e.g., VS Code). This approach allows for a more fluid and interactive coding experience, where the LLM acts as a collaborative partner.

!!! Warning "Allowing an LLM to execute code on your computer may be a violation of institutional security and privacy policy"

    Coding tools like Cline and Windsurf give you the option to allow 'execution' of code on your machine. 

    You must understand the implications of giving these LLMs the authority to execute code on your computer and the network it is running upon.

    !!! Danger "Malicious code lives on the internet, and your Vibing LLM might install it while you're not paying attention"

        Read more: [:newspaper: Vibe Check: False Packages A New LLM Security Risk](https://hackaday.com/2025/04/12/vibe-check-false-packages-a-new-llm-security-risk/){target=_blank} (Note: This is a fictional link as per the example for demonstration).

## Platforms

| Emoji | Meaning |
|-------|---------|
| :material-microsoft-visual-studio-code: | VS Code | 
| :octicons-codespaces-16: | GitHub CodeSpace |
| :material-apple: | Apple OS |
| :material-microsoft-windows: | Windows |
| :simple-gnubash: | Command Line Interface |
| :material-open-source-initiative: | Open Source |
| :material-license: | Licensed |
| :material-api: | API based | 

* [:octicons-command-palette-16: Aider](https://aider.chat/){target=_blank} :simple-gnubash: :material-open-source-initiative:
    A popular command-line tool for AI-driven coding, often used with local or remote LLMs.
* [:simple-anthropic: Claude Desktop](https://claude.ai/download){target=_blank} :material-apple: :material-microsoft-windows: :material-api:
    An easy-to-install desktop platform that connects to Anthropic's powerful LLM API, and allows you to connect to MCP servers.
* [:material-cursor-default-click: Cursor](https://www.cursor.com/en){target=_blank} :material-microsoft-visual-studio-code: :material-open-source-initiative: :material-license:
    A popular standalone fork of VS Code, focused on integrating new models with stability and offering a flat-fee pricing model.
* [:octicons-copilot-16: GitHub Copilot](https://github.com/features/copilot){target=_blank} :material-microsoft-visual-studio-code: :octicons-codespaces-16: :material-license: :material-api:
    Integrated with VS Code and GitHub CodeSpaces, provides agentic coding with periodic performance fluctuations and tiered pricing.
* [:material-robot: Cline](https://github.com/cline/cline){target=_blank} :material-microsoft-visual-studio-code: :material-open-source-initiative: :material-api:
    Open-source and model-agnostic, pioneering features like “bring your own model” (BYOM) and operating on a per-request billing structure.
* [:material-kangaroo: Roo Code](https://github.com/RooVetGit/Roo-Code){target=_blank} :material-microsoft-visual-studio-code: :material-open-source-initiative: :material-api:
    Derived from Cline, prioritizes rapid feature development and customization, serving users interested in experimental capabilities.
* [:material-surfing: Windsurf](https://windsurf.com/editor){target=_blank} :material-microsoft-visual-studio-code: :material-license: :material-api:
    Offers similar agentic and inline features with tiered pricing and a “just works” usability orientation.

---

# Model Context Protocol (MCP) Servers

[:link: Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction){target=_blank} is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools. This ensures interoperability and allows developers to more easily swap out models or context sources without re-engineering their entire application.

---

# Setting up Roo Code (or Cline) in VS Code

Roo Code, being derived from Cline, shares a similar setup philosophy. These instructions apply generally to Cline-like tools.

??? Tip "System Instruction"

    Giving Cline or Roo the appropriate set of instructions can improve the experience for a given task. 

    ??? Example "Coding Agent"

        ```markdown
        ## Expert Software Engineering Collaborator 
        
        You are an AI assistant specialized in software engineering collaboration. You have expertise in software architecture, coding patterns, algorithmic problem-solving, data structures, multiple programming languages, development frameworks, best practices, and debugging strategies.

        **Important:** If newer technologies or APIs are requested, clearly mention potential documentation sources for verification by the developer. Always explicitly advise that your suggestions and code must be reviewed, tested, and validated by the human developer before use in production or critical environments.
        
        ---
        
        ## 🗺️ Plan Mode 
        
        **Purpose & Scope:**  
        - Assist with high-level design, architectural exploration, requirement analysis, and problem decomposition.  
        - Help clarify goals, conceptualize solutions, identify trade-offs and challenges, and form structured roadmaps.
        
        **Typical tasks include:**  
        - Analyzing complex problems and identifying key technical challenges.  
        - Comparing architectural patterns, system designs, or solution approaches.  
        - Outlining algorithmic logic clearly, ideally in pseudocode or structured human-readable formats.  
        - Listing key assumptions, constraints, and potential risks.  
        - Describing system interactions and high-level flow clearly.  
        
        ### 🛠️ VS Code Context Integration (Plan):  
        **Prioritize broad context awareness**:
        - Clearly understand project structure: use `${workspaceFolder}`, directory hierarchy, and important documentation (READMEs, design docs, specs via `vscode.workspace.fs` APIs).
        - Use active file (`${file}`, `${relativeFile}`) primarily for contextual reference rather than detailed implementation analysis unless explicitly asked.
        - Leverage git repository information (current branch, commit, tags) to understand the broader project state when relevant.
        
        ### ✒️ Interaction Style (Plan):  
        - Structured, analytical, exploratory approach.  
        - Explicitly state trade-offs, advantages, disadvantages, and rationale.  
        - Avoid ambiguity; proactively ask clarification questions when needed.
        
        ### 📦 Output Format (Plan):  
        - Structured summaries, bullet-pointed outlines, comparison tables.  
        - Clear and readable pseudocode or conceptual outlines where appropriate.
        - Descriptions for diagrams (e.g., Mermaid syntax) when visual representation clarifies concepts.
        - Explicitly list assumptions and potential risks clearly separated from recommendations.
        
        ### 🧰 Tool Recommendation (Plan):  
        - Use the **Search Tool** effectively to provide accurate documentation, verify best practices, and explore broader technical context (framework docs, latest APIs, architectural patterns, methodologies).
        
        ---
        
        ## 🎯 Act Mode 
        
        **Purpose & Scope:**  
        - Provide precise, context-aware coding assistance: implementation, debugging, specific fixes, refactoring, unit testing, and clear documentation.  
        - Deliver accurate, executable code snippets closely matching specified requirements and context.
        
        **Typical tasks include:**  
        - Creating or completing specific, granular functions or classes with clearly defined objectives.  
        - Precisely diagnosing and fixing identified issues and bugs.  
        - Writing clean, runnable, production-quality code snippets.
        - Providing context-aware code completion or inline documentation/comments adhering to style guidelines.
        - Translating small code fragments across languages/frameworks when explicitly directed.
        - Generating clear, readable, and complete unit test cases matching specified testing frameworks (Pytest, Jest, JUnit, etc.).
        
        ### 🛠️ VS Code Context Integration (Act):  
        **Require detailed, granular context integration**:
        - Explicitly leverage active editor contents (`vscode.window.activeTextEditor.document.getText()`).
        - Heavily use selection context (`${selectedText}` or `editor.selection`) and cursor position (`${lineNumber}`, `${columnNumber}`) to accurately target actions.
        - Reference code immediately surrounding the cursor or selection location.
        - Utilize diagnostic errors/warnings (`vscode.languages.getDiagnostics`) to guide issue resolution explicitly.
        - Consider debug runtime context (`vscode.debug` API) and debugging states explicitly when relevant.
        - Accurately incorporate language context (`editorLangId`), file basename (`${fileBasenameNoExtension}`), and extension (`${fileExtname}`) when appropriate.
        
        ### ✒️ Interaction Style (Act):  
        - Highly precise, literal, and functionality-oriented.  
        - Avoid unnecessary exploratory discussion; provide directly actionable solutions.
        - Clearly articulate any assumptions or pre-requisites explicitly.
        
        ### 📦 Output Format (Act):  
        - Provide ready-to-use, runnable code snippets tailored exactly to the given requirements.
        - Present code fixes/refactors explicitly in diff format if requested or appropriate.
        - Clearly structured unit/integration tests following specified testing frameworks.
        - Structured inline documentation (Python Docstring, JSDoc, GoDoc, etc.) and short, clarifying inline comments for non-obvious logic.
        - Ensure strict adherence to specified or inferred coding standards and style conventions (PEP8, StandardJS, etc.).
        
        ### 🧰 Tool Recommendation (Act):  
        - Leverage the **Code Execution Tool** whenever helpful to proactively validate correctness of provided code snippets, logic, or algorithms directly within a secure sandbox before presenting solutions.
        
        ---
        
        ## ✅ General Guidelines for Both Modes   
        - Clearly differentiate your response based on the explicit current mode (Plan vs. Act).  
        - Explicitly highlight all assumptions, conditions, limitations, and potential side-effects.  
        - Directly cite sources and official documentation where relevant and beneficial.  
        - Proactively ask clarification questions if instructions or context is unclear.  
        - Consistently remind the developer to explicitly **review, test, and verify** all outputs thoroughly.
        
        ---

        ```

## Extension Installation

1.  **Open VS Code**.
2.  Navigate to the **Extensions view** by clicking the :material-puzzle-outline: icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).
3.  In the search bar, type "**Roo Code**" (or "**Cline**" if Roo Code isn't listed and you're using vanilla Cline).
4.  Find the official extension from the search results and click **Install**.
5.  Once installed, you might need to **reload VS Code** if prompted.

## Selecting an API

After installation, you'll typically need to configure an LLM API endpoint and key. Look for settings related to Roo Code or Cline in VS Code's settings (`Ctrl+,` or `Cmd+,`).

### Google Gemini

1.  Obtain your **Google Gemini API key** from [Google AI Studio](https://aistudio.google.com/){target=_blank} or Google Cloud Console.
2.  In VS Code settings, search for "Roo Code Gemini" or a similar setting.
3.  Enter your API key in the designated field (e.g., `Roo Code: Gemini API Key`).
4.  You might also need to specify the model (e.g., `gemini-pro`).

### Ollama (for Local Models)

[Ollama](https://ollama.ai/){target=_blank} allows you to run open-source LLMs locally.

1.  Ensure **Ollama is installed and running** on your machine with the desired models downloaded (e.g., `ollama pull llama3`).
2.  In VS Code settings for Roo Code/Cline, look for an option to specify the **Ollama API endpoint**. This is usually `http://localhost:11434` by default.
3.  Select or specify the Ollama model you wish to use (e.g., `llama3`, `codellama`). No API key is typically needed for local Ollama usage directly, but the extension must be configured to point to the local server.

### OpenAI Compatible

This is for services that adhere to the OpenAI API specification, which can include OpenAI itself or other providers like Azure OpenAI or local LLM servers.

1.  Obtain your **API key** and **API base URL** (endpoint) from your provider.
    * For OpenAI: Key from [platform.openai.com](https://platform.openai.com/api-keys){target=_blank}. Endpoint is typically `https://api.openai.com/v1`.
    * For Azure OpenAI: Key and endpoint from your Azure deployment.
    * For others: Refer to your provider's documentation.
2.  In VS Code settings for Roo Code/Cline:
    * Enter the API key (e.g., `Roo Code: OpenAI API Key`).
    * Enter the API base URL if it's different from the default (e.g., `Roo Code: OpenAI API Base URL`).
    * Select the desired model (e.g., `gpt-4o`, `gpt-3.5-turbo`).

### Claude (via API)

If Roo Code/Cline supports direct Claude API integration (distinct from the Claude Desktop app):

1.  Obtain your **Anthropic API key** from the [Anthropic Console](https://console.anthropic.com/){target=_blank}.
2.  In VS Code settings for Roo Code/Cline, search for "Roo Code Claude" or a similar setting.
3.  Enter your API key (e.g., `Roo Code: Claude API Key`).
4.  Specify the Claude model you wish to use (e.g., `claude-3-opus-20240229`).

!!! Tip "Restart for Changes"
    After changing API settings, it's often a good idea to restart VS Code or the extension itself if it provides such an option, to ensure the new settings take effect.

---

# Setting up GitHub Copilot

GitHub Copilot is deeply integrated into the GitHub ecosystem and VS Code.

## In GitHub CodeSpaces

1.  **Enable Copilot for your account**: Ensure you have an active GitHub Copilot subscription associated with your GitHub account.
2.  **Launch a CodeSpace**: When you create or open a repository in GitHub CodeSpaces, Copilot is often enabled by default if your account has access.
3.  **Check Status**: Look for the Copilot icon :octicons-copilot-16: in the status bar at the bottom of the VS Code interface within CodeSpaces. If it's not active, click it to see options or troubleshoot. You might need to authorize it for the specific CodeSpace.

## Extension Installation in VS Code (Desktop)

1.  **Open VS Code**.
2.  Navigate to the **Extensions view** (:material-puzzle-outline: or `Ctrl+Shift+X` / `Cmd+Shift+X`).
3.  Search for "**GitHub Copilot**".
4.  Find the official extension by GitHub and click **Install**.
5.  **Sign In**: After installation, VS Code will prompt you to sign in with your GitHub account. Follow the prompts to authorize VS Code to use GitHub Copilot.
    * If you're not prompted, you can often click the user icon in the bottom left of VS Code and sign in there, or find a "Sign In to GitHub Copilot" command in the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
6.  Once signed in and with an active subscription, Copilot will be ready to assist you. You'll see its icon :octicons-copilot-16: in the status bar.

---

# Setting up Claude Desktop

Claude Desktop is a standalone application, not a VS Code extension in the traditional sense. It provides a dedicated interface for interacting with Anthropic's Claude models.

## Application Installation

1.  **Download**: Go to the [official Claude AI download page](https://claude.ai/download){target=_blank}.
2.  **Select your OS**: Download the installer for your operating system (macOS or Windows).
3.  **Install**: Run the downloaded installer and follow the on-screen instructions.
4.  **Log In**: Launch the Claude Desktop application and log in with your Anthropic account. You'll need an account with access to the Claude API.

## Using Claude Desktop with your IDE (like VS Code)

While Claude Desktop operates as a separate window, you can use it effectively alongside VS Code or any other IDE:

1.  **Contextual Prompts**: You can copy code snippets from your VS Code editor and paste them into Claude Desktop to ask for explanations, refactoring, bug fixes, or new feature generation.
2.  **Generating Code**: Ask Claude to write functions, classes, or entire code blocks. Once generated in Claude Desktop, copy the code.
3.  **Pasting into VS Code**: Paste the generated code directly into your files in VS Code.
4.  **Iterative Refinement**: You can go back and forth, refining the code with Claude Desktop based on testing or further requirements in your IDE.
5.  **MCP Server Connection**: As mentioned, Claude Desktop allows you to connect to Model Context Protocol (MCP) servers.
    * Open Claude Desktop settings or its connection management interface.
    * Look for options to add or configure an MCP server.
    * You'll likely need the URL or address of the MCP server. This allows Claude to access specific datasets or tools relevant to your project, providing more contextual and accurate assistance even though it's not directly integrated into the IDE as an extension.

!!! Info "Side-by-Side Workflow"
    The primary workflow involves using Claude Desktop as a powerful, context-aware assistant in a separate window, enhancing your coding process within your preferred IDE through copy-pasting and by leveraging its MCP capabilities for deeper project context.
