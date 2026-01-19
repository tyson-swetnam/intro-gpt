# Vibe Coding

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

"**Vibe coding**" refers to using an LLM to generate and edit code directly within your IDE (e.g., VS Code). This approach allows for a more fluid and interactive coding experience, where the LLM acts as a collaborative partner.

??? Info "Who coined the term 'vibe coding'?"

    The term "vibe coding" originated with a tweet by Andrej Karpathy in February 2025,

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">There&#39;s a new kind of coding I call &quot;vibe coding&quot;, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It&#39;s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. I just mass chat, mass accept, skip to errors,…</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://twitter.com/karpathy/status/1886192184808149383?ref_src=twsrc%5Etfw">February 2, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    

!!! Warning "Allowing an LLM to execute code on your computer may be a violation of institutional security and privacy policy"

    Desktop applications like Claude Desktop or OpenAI's ChatGPT Desktop give you the option to allow 'execution' of code on your computer (laptop or PC). 

    You must understand the implications of giving these AI assistants the authority to execute code on your computer and access to the network it is running upon.

    !!! Danger "Malicious code lives on the internet, and your Vibing AI assistant might install something bad while you're not paying attention"

        Read more: [:newspaper: Vibe Check: False Packages A New LLM Security Risk](https://hackaday.com/2025/04/12/vibe-check-false-packages-a-new-llm-security-risk/){target=_blank} (Note: This is a fictional link as per the example for demonstration).

## Available Platforms

| Emoji | Meaning |
|-------|---------|
| :material-microsoft-visual-studio-code: | VS Code |
| :octicons-codespaces-16: | GitHub CodeSpace |
| :material-apple: | Apple OS |
| :material-microsoft-windows: | Windows |
| :simple-linux: | Linux |
| :simple-gnubash: | Command Line Interface |
| :material-open-source-initiative: | Open Source |
| :material-license: | Licensed |
| :material-api: | API based |

### Desktop IDEs and Standalone Editors

#### [:simple-anthropic: Claude Desktop](https://claude.ai/download){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-api:

An easy-to-install desktop platform that connects to Anthropic's powerful LLM API, and allows you to connect to MCP servers.

#### [:material-microsoft-visual-studio-code: VS Code](https://code.visualstudio.com/){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-open-source-initiative:

Microsoft's popular open-source code editor with extensive extension ecosystem, including numerous AI coding assistants (see VS Code Extensions section below).

#### [:material-cursor-default-click: Cursor](https://www.cursor.com/en){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-license: :material-api:

A popular standalone fork of VS Code, focused on integrating new models with stability and offering a flat-fee pricing model.

#### [:simple-posit: Positron](https://github.com/posit-dev/positron){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-open-source-initiative:

A next-generation data science IDE built on VS Code, developed by Posit (formerly RStudio), with native support for Python, R, and AI-assisted coding.

#### [:simple-firebase: Firebase Studio](https://firebase.google.com/products/app-hosting){target=_blank}

:material-web: :material-license: :material-api:

Firebase's integrated development environment for building and deploying Firebase apps with AI-powered code generation and assistance.

#### [:simple-google: Google Antigravity](https://antigravity.google/){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-license: :material-api:

Google's experimental AI-powered standalone IDE with advanced Gemini integration for next-generation development workflows.

#### [:material-surfing: Windsurf](https://windsurf.com/editor){target=_blank}

:material-apple: :material-microsoft-windows: :simple-linux: :material-license: :material-api:

Standalone editor offering similar agentic and inline features with tiered pricing and a "just works" usability orientation.

### VS Code Extensions

#### [:simple-anthropic: Claude Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code){target=_blank}

:material-microsoft-visual-studio-code: :material-license: :material-api:

Official Anthropic VS Code extension providing AI pair programming with Claude 4.5 models, featuring multi-file editing, debugging, and terminal integration.

#### [:simple-google: Gemini CLI Companion](https://marketplace.visualstudio.com/items?itemName=Google.gemini-cli-vscode-ide-companion){target=_blank}

:material-microsoft-visual-studio-code: :material-license: :material-api:

Google's VS Code extension powered by Gemini models, offering code completion, generation, and chat assistance with Google Cloud integration.

#### [:fontawesome-brands-openai: OpenAI Codex](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt){target=_blank}

:material-microsoft-visual-studio-code: :octicons-codespaces-16: :material-license: :material-api:

Codex is integrated as an extension in VS Code

#### [:octicons-copilot-16: GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot){target=_blank}
:material-microsoft-visual-studio-code: :octicons-codespaces-16: :material-license: :material-api:

Integrated with VS Code and GitHub CodeSpaces, provides agentic coding with periodic performance fluctuations and tiered pricing.

#### [:material-robot: Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev){target=_blank}

:material-microsoft-visual-studio-code: :material-open-source-initiative: :material-api:

VS Code extension that's open-source and model-agnostic, pioneering features like "bring your own model" (BYOM) and operating on a per-request billing structure.

#### [:material-kangaroo: Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline){target=_blank}

:material-microsoft-visual-studio-code: :material-open-source-initiative: :material-api:

VS Code extension derived from Cline, prioritizes rapid feature development and customization, serving users interested in experimental capabilities.

### Command Line Interface (CLI) Tools

#### [:octicons-command-palette-16: Aider](https://aider.chat/){target=_blank}

:simple-gnubash: :material-open-source-initiative:

A popular command-line tool for AI-driven coding, often used with local or remote LLMs.

#### [:simple-anthropic: Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code){target=_blank}

:simple-gnubash: :material-license: :material-api:

Official Anthropic command-line interface for Claude, enabling AI-assisted development directly from the terminal with support for MCP servers.

#### [:fontawesome-brands-openai: OpenAI Codex CLI](https://github.com/features/copilot){target=_blank}

:simple-gnubash: :material-license: :material-api:

Command-line access to OpenAI's Codex models, integrated with GitHub Copilot for terminal-based AI assistance.

#### [:simple-google: Google Gemini CLI](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python){target=_blank}

:simple-gnubash: :material-license: :material-api:

Google's command-line interface for Gemini models, providing AI coding assistance and integration with Google Cloud services.

#### [:material-code-braces: OpenCode.ai](https://opencode.ai/){target=_blank}

:simple-gnubash: :material-open-source-initiative: :material-api:

Open-source CLI tool supporting multiple AI models for code generation, analysis, and refactoring from the command line.

### Browser-based Vibe Coding

#### [:simple-anthropic: Claude Code](https://claude.ai/code){target=_blank}

:material-web: :material-license: :material-api:

Browser-based version of Claude Code providing AI pair programming capabilities through the web, featuring multi-file editing, code generation, and debugging without requiring a desktop installation.

#### [:fontawesome-brands-openai: ChatGPT](https://chat.openai.com){target=_blank}

:material-web: :material-license: :material-api:

OpenAI's ChatGPT Plus and Team tiers include Code Interpreter (Advanced Data Analysis) for executing Python code, analyzing data, and generating visualizations directly in the browser.

#### [:simple-google: Google Gemini](https://gemini.google.com){target=_blank}

:material-web: :material-license: :material-api:

Google Gemini's web interface features code execution capabilities, allowing you to run Python code and see results inline with AI-generated explanations.

#### [:material-web: OpenWebUI](https://openwebui.com){target=_blank}

:material-web: :material-open-source-initiative:

Self-hostable, open-source web interface supporting multiple LLM providers (OpenAI, Anthropic, Ollama) with built-in code execution, function calling, and customizable workflows.

---

# Model Context Protocol (MCP)

[:link: Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction){target=_blank} is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools. This ensures interoperability and allows developers to more easily swap out models or context sources without re-engineering their entire application.

---
