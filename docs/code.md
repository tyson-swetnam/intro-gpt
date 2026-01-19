# Understanding Code Generation with LLMs

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Introduction: From Generation to Execution

Large Language Models (LLMs) have fundamentally changed how we write and interact with code. Beyond simply generating code snippets, modern AI tools can now **execute** code, analyze data, and produce results in real-time. This capability manifests in multiple forms:

- **Code Interpreters** that operate in secure, sandboxed environments
- **Code Execution Frameworks** that integrate directly into your local development environment
- **Agentic AI Systems** that can autonomously plan, code, test, and iterate on complex software projects

This evolution from simple code completion to autonomous coding agents represents a paradigm shift in software development. This lesson explores the spectrum of code generation and execution tools, from sandboxed interpreters to sophisticated [agentic AI systems](agentic.md) that leverage [Model Context Protocol (MCP)](mcp.md) for deep integration with your development environment.

This sets the foundation for understanding "[Vibe Coding](vibe.md)"—the emerging practice of collaborative, conversational development where AI acts as an autonomous pair programmer within your IDE.

---

## 1. Code Interpreters: Your Sandboxed AI Analyst

A Code Interpreter is a tool, typically within a chat-based interface, that can write and execute code in a secure, isolated environment. You provide instructions and data in natural language, and the AI handles the coding, execution, and interpretation of results.

**Key Characteristics:**

- **Sandboxed Execution**: Code runs in an isolated environment with no access to your local files or network
- **Data Upload**: Upload datasets, documents, or files for analysis
- **Instant Results**: See code execution output, visualizations, and analyses in real-time
- **No Setup Required**: No need to install programming languages or libraries locally
- **Session-Based**: Work is temporary; files and state typically reset between sessions

**Ideal Use Cases:**

- **Data Analysis & Visualization**: Process datasets and create charts without writing code
- **File Conversions**: Transform file formats (CSV to JSON, image format conversions)
- **Mathematical Computations**: Solve complex equations and perform statistical analyses
- **Prototyping**: Quickly test algorithms or data processing workflows
- **Learning**: Experiment with programming concepts in a safe environment

Code Interpreters are perfect for exploratory data analysis, one-off computations, and tasks where you want AI assistance without giving it access to your local system. For deeper integration with your development workflow, see [Code Execution Frameworks](#2-code-execution-frameworks-your-ai-pair-programmer) and [Vibe Coding](vibe.md).

### Recommended Platforms

#### :simple-google: Google Gemini

**Platform**: [gemini.google.com](https://gemini.google.com/){target=_blank}

Google's Gemini integrates powerful code interpretation capabilities directly within its chat interface. With its multimodal capabilities, you can:

- Upload files (PDFs, spreadsheets, images) and ask for analysis
- Perform complex data analysis and generate visualizations
- Solve programming problems with step-by-step explanations
- Leverage integration with Google Workspace and Google Cloud Platform

**Best for**: Users in the Google ecosystem, multimodal data analysis, and document processing.

#### :simple-anthropic: Anthropic's Claude

**Platform**: [claude.ai](https://claude.ai/){target=_blank}

Claude offers robust Code Interpreter functionality through its **Artifacts** feature, which provides a live preview panel for code execution. Key features include:

- Upload documents, spreadsheets, and code files (up to 5 files, 10MB each)
- Write and execute Python code in a secure sandbox
- Create interactive data visualizations and charts
- Generate and iterate on code with real-time execution feedback
- Extended context window (200K tokens) for analyzing large codebases

**Best for**: Statistical analysis, data cleaning, document processing, and iterative code development.

#### :fontawesome-brands-openai: OpenAI ChatGPT Plus/Team

**Platform**: [chat.openai.com](https://chat.openai.com){target=_blank}

ChatGPT's **Advanced Data Analysis** (formerly Code Interpreter) is available to Plus and Team subscribers:

- Upload and analyze data files in various formats
- Generate sophisticated visualizations using matplotlib and seaborn
- Perform file conversions and data transformations
- Solve mathematical problems with symbolic computation
- Create animated visualizations and GIFs

**Best for**: Data science workflows, exploratory data analysis, and creating publication-ready visualizations.

#### :material-brain: Perplexity Pro

**Platform**: [perplexity.ai](https://www.perplexity.ai/){target=_blank}

Perplexity Pro includes code execution capabilities alongside its powerful search features:

- Execute Python code in a sandboxed environment
- Combine web search results with data analysis
- Generate visualizations based on real-time data
- Verify calculations and computations with source citations

**Best for**: Research tasks requiring both web search and data analysis.

!!! example "Data Analysis with a Code Interpreter"

    Imagine you are a researcher with a dataset of student performance metrics. You could upload a CSV to Gemini or Claude and prompt:

    ```
    Analyze the CSV https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv
    
    1.  Load the dataset into a Pandas DataFrame.
    2.  Clean the data by handling any missing values.
    3.  Generate a scatter plot to visualize the relationship between key variables.
    4.  Calculate the Pearson correlation coefficient between these two variables.
    5.  Interpret the results and provide a brief summary.
    ```

    The Code Interpreter would then write and run Python code to perform these steps, showing you the code, the output, and the final analysis.

---

## 2. Code Execution Frameworks: Your AI Pair Programmer

While sandboxed interpreters are powerful for isolated tasks, the real transformation in software development comes from **Code Execution Frameworks**—tools that integrate AI assistance directly into your Integrated Development Environment (IDE). These frameworks bridge the gap between simple autocomplete and full [**agentic AI systems**](agentic.md) capable of autonomous development.

**Key Characteristics:**

- **IDE Integration**: Work directly within VS Code, JetBrains IDEs, or standalone editors
- **Local Execution**: Run code on your machine with access to your file system
- **Multi-File Awareness**: Understand context across your entire project
- **Tool Use**: Execute terminal commands, run tests, interact with Git
- **Iterative Development**: Debug, fix errors, and refine code autonomously
- **Context Protocol Support**: Leverage [MCP](mcp.md) for deep integration with local tools and services

**Evolution of Capabilities:**

1. **Code Completion** (2021-2022): Simple autocomplete and snippet generation
2. **Code Generation** (2022-2023): Generate functions and classes from descriptions
3. **Conversational Coding** (2023-2024): Chat-based assistance with code editing
4. **Agentic Coding** (2024-present): Autonomous multi-file editing, testing, and debugging

These tools form the foundation of [**Vibe Coding**](vibe.md)—a fluid, conversational approach to development where AI acts as an autonomous pair programmer, not just a suggestion engine.

### Recommended Platforms & Tools

The landscape of AI-assisted development tools has exploded, ranging from simple completion tools to sophisticated [agentic systems](agentic.md). Below is a categorized overview; see our comprehensive [**Vibe Coding guide**](vibe.md) for detailed comparisons and setup instructions.

#### Desktop IDEs & Standalone Editors

**[:material-cursor-default-click: Cursor](vibe.md#cursor)**
:material-apple: :material-microsoft-windows: :simple-linux:

A popular standalone fork of VS Code with powerful agentic features. Cursor excels at multi-file editing, codebase understanding, and autonomous debugging. Uses a flat-fee pricing model with support for multiple LLM providers.

**Best for**: Developers wanting a turnkey solution with stable, production-ready features.

**[:material-surfing: Windsurf](vibe.md#windsurf)**
:material-apple: :material-microsoft-windows: :simple-linux:

Standalone editor focused on "just works" usability with agentic and inline features. Similar capabilities to Cursor with a different UX philosophy.

**Best for**: Developers who prefer Windsurf's interaction model over Cursor's approach.

**[:simple-anthropic: Claude Desktop](https://claude.ai/download)**
:material-apple: :material-microsoft-windows: :simple-linux:

Native desktop application with built-in [**Model Context Protocol (MCP)**](mcp.md) support. Connect to local filesystem servers, GitHub repositories, databases, and custom tools for context-aware assistance.

**Best for**: Users wanting MCP integration and native OS features without IDE lock-in.

#### VS Code Extensions

**[:simple-anthropic: Claude Code](vibe.md#claude-code-vs-code-extension)**
:material-microsoft-visual-studio-code:

Official Anthropic VS Code extension featuring multi-file editing, debugging, and terminal integration. Provides agentic coding capabilities directly in VS Code.

**Best for**: VS Code users wanting official Claude integration with strong agentic features.

**[:material-robot: Cline](vibe.md#cline)**
:material-microsoft-visual-studio-code: :material-open-source-initiative:

Open-source, model-agnostic VS Code extension pioneering "bring your own model" (BYOM). Supports multiple LLM providers including local models via Ollama.

**Best for**: Users wanting flexibility, open-source transparency, and control over model selection.

**[:material-kangaroo: Roo Code](vibe.md#roo-code)**
:material-microsoft-visual-studio-code: :material-open-source-initiative:

Fork of Cline focused on rapid feature development and customization. Serves users interested in experimental capabilities.

**Best for**: Early adopters wanting cutting-edge features and customization options.

**[:octicons-copilot-16: GitHub Copilot](vibe.md#github-copilot)**
:material-microsoft-visual-studio-code: :octicons-codespaces-16:

Microsoft's AI pair programmer with deep GitHub integration. Provides inline completion, chat assistance, and agentic features through Copilot Workspace.

**Best for**: GitHub-centric workflows and organizations with enterprise GitHub licenses.

**[:simple-google: Gemini Code Assist](vibe.md#gemini-code-assist)**
:material-microsoft-visual-studio-code:

Google's VS Code extension powered by Gemini models, offering code completion, generation, and chat assistance with Google Cloud integration.

**Best for**: Google Cloud Platform users and those in the Google ecosystem.

#### Command Line Interface (CLI) Tools

**[:simple-anthropic: Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)**
:simple-gnubash:

Official Anthropic command-line interface enabling AI-assisted development from the terminal with [MCP server support](mcp.md).

**Best for**: Terminal-first developers and automation workflows.

**[:octicons-command-palette-16: Aider](https://aider.chat/)**
:simple-gnubash: :material-open-source-initiative:

Popular open-source command-line tool for AI-driven coding. Works with local or remote LLMs and integrates well with Git workflows.

**Best for**: Developers who prefer command-line workflows and want model flexibility.

#### Browser-Based Development

**[:simple-anthropic: Claude Code for Web](https://claude.ai/code)**
:material-web:

Browser-based version providing AI pair programming through the web with multi-file editing and debugging capabilities.

**Best for**: Quick coding sessions without local installation or Chromebook users.

**[:simple-firebase: Firebase IDX](https://idx.dev/)**
:material-web:

Google's cloud-based IDE with built-in Gemini assistance, providing VS Code-like editing experience in the browser.

**Best for**: Cloud-based development with Google Cloud Platform integration.

**[:material-web: OpenWebUI](https://openwebui.com)**
:material-web: :material-open-source-initiative:

Self-hostable web interface supporting multiple LLM providers with built-in code execution and function calling.

**Best for**: Self-hosting enthusiasts and teams wanting full control over their AI infrastructure.

#### API & Console Environments

**[:simple-google: Google AI Studio](https://aistudio.google.com/app/prompts/new_chat)**
:material-web:

Browser-based environment for experimenting with Gemini models, prototyping prompts, and generating code snippets.

**Best for**: Prototyping with Gemini models and testing prompt strategies.

**[:fontawesome-brands-openai: OpenAI Playground](https://platform.openai.com/playground)**
:material-web:

Console environment for experimenting with OpenAI models, fine-tuning prompts, and developing code functions.

**Best for**: API developers prototyping with OpenAI models.

!!! tip "From Console to IDE: The Vibe Coding Evolution"

    While console-based tools are excellent for prototyping, the real power of AI-assisted development comes from direct IDE integration. Modern tools leverage [**Model Context Protocol (MCP)**](mcp.md) to access your local environment, enabling [**agentic behaviors**](agentic.md) like:

    - Autonomous multi-file refactoring
    - Running tests and fixing failures iteratively
    - Executing terminal commands and analyzing output
    - Interacting with Git for version control
    - Accessing databases and external APIs

    Explore our [**Vibe Coding guide**](vibe.md) to discover how these tools transform your editor into a collaborative coding environment where AI agents work alongside you.

---

## 3. Best Practices & Ethical Considerations

Whether using a sandboxed interpreter, a code execution framework, or an [agentic AI system](agentic.md), following best practices ensures effective, secure, and responsible use of AI coding tools.

### Effective Prompting Strategies

**Start with Clear Intent**
- Describe what you want to accomplish, not just how to do it
- Provide context about your project, language, and frameworks
- Specify constraints (performance, security, compatibility)

**Break Down Complex Tasks**
- Don't ask AI to build an entire application in one go
- Decompose problems into smaller, testable steps
- Let the AI iterate on solutions rather than attempting everything at once
- This is especially important for [agentic systems](agentic.md) that benefit from clear subtask boundaries

**Provide Rich Context**
- Share relevant code snippets, error messages, and documentation
- Use [MCP](mcp.md)-enabled tools to automatically provide file and project context
- Explain your reasoning and decision-making process
- Include examples of desired output or style

### Code Review & Verification

**Never Trust Generated Code Blindly**
- **Always review** for correctness, efficiency, and maintainability
- **Test thoroughly** with unit tests, integration tests, and edge cases
- **Check for security vulnerabilities** (SQL injection, XSS, authentication issues)
- **Verify adherence** to your project's coding standards and best practices

**Understand Before Using**
- If you don't understand the generated code, ask the AI to explain it
- Research unfamiliar libraries or patterns before adopting them
- Consider maintainability—will you be able to debug this code in 6 months?

**Iterative Refinement**
- Start with a basic implementation and refine iteratively
- Test at each stage before adding complexity
- Use the AI to help debug and improve, not just generate initially

### Security Considerations

!!! danger "Local Execution Risks"
    [Agentic AI systems](agentic.md) and [vibe coding tools](vibe.md) that execute on your machine have significant access:

    - **File System Access**: Can read, modify, and delete files
    - **Network Access**: Can make API calls and external connections
    - **Terminal Access**: Can execute arbitrary shell commands
    - **Environment Variables**: May access sensitive credentials

    **Security Best Practices:**

    - Review commands before AI executes them (most tools prompt for approval)
    - Use project-specific virtual environments
    - Never store secrets in code—use environment variables and secret managers
    - Be cautious with `sudo` or administrator privileges
    - Monitor AI actions, especially when learning a new tool
    - Follow your institution's security and privacy policies
    - Consider using sandboxed development environments for sensitive work

**Institutional Policies**
Many universities and organizations have policies about AI code execution. Check with your IT security team about:

- Approved AI tools and services
- Data classification restrictions
- Code review requirements for AI-generated code
- Network access policies for AI services

See our [Vibe Coding security warnings](vibe.md) for more detailed guidance.

### Bias, Licensing, and Intellectual Property

**Training Data Considerations**

AI models are trained on public code repositories, which may contain:

  - **Biased implementations** (non-inclusive variable names, accessibility issues)
  - **Licensed code** that may not be suitable for your use case
  - **Outdated patterns** or deprecated approaches
  - **Security vulnerabilities** from historical code

**Best Practices:**

- Review generated code for inclusive language and accessibility
- Check license compatibility for suggested libraries
- Validate that patterns are current and recommended
- Don't assume AI-generated code is "best practice"

**Intellectual Property**

- Most AI providers claim no copyright on generated output
- However, generated code might inadvertently replicate existing licensed code
- Your organization may have policies about AI-generated code ownership
- Document when and how AI tools were used in development

### Privacy and Data Handling

**What Data Gets Sent to AI Services?**

- Your prompts and code snippets
- File contents (with MCP or when explicitly shared)
- Error messages and terminal output
- Project structure and metadata

**Privacy Best Practices:**

- Don't share sensitive data, credentials, or personal information in prompts
- Review your organization's data classification policies
- Use local/self-hosted models for sensitive code when possible
- Be aware of data retention policies for AI services you use
- Consider anonymizing data before sharing with AI tools

**Tools with Enhanced Privacy:**

- [Cline](vibe.md#cline) and [Roo Code](vibe.md#roo-code): Can use local models via Ollama
- [Aider](https://aider.chat/) and [OpenCode.ai](https://opencode.ai): Supports local LLMs
- Claude Desktop with [MCP](mcp.md): Data processing happens locally before being sent to API

### Accessibility and Inclusive Development

**Use AI to Improve Accessibility**

- Ask AI to review code for WCAG compliance
- Generate accessible alternatives for visual content
- Check color contrast and screen reader compatibility
- Implement keyboard navigation

**Avoid Perpetuating Bias**

- Review generated variable names and comments for inclusive language
- Ask AI to suggest alternatives if you spot problematic patterns
- Consider diverse user needs when prompting for UI/UX implementations

### Environmental Considerations

**AI Compute Costs**

- LLM inference requires significant energy
- Be mindful of unnecessary requests
- Use appropriate model sizes (don't use GPT-4 for simple autocomplete)
- Cache results when possible
- Consider carbon-aware computing practices

### Continuous Learning

**Stay Updated**

- AI coding tools evolve rapidly
- Follow release notes and changelogs
- Experiment with new features in safe environments
- Join communities and share learnings
- Read our [Vibe Coding guide](vibe.md) regularly for updates

**Develop AI Literacy**

- Understand how LLMs work and their limitations
- Learn about prompt engineering techniques
- Recognize when AI is appropriate vs. when human expertise is needed
- Share knowledge with your team

!!! tip "The Human-AI Partnership"

    The goal isn't to replace developers with AI—it's to augment human capabilities. The best results come from combining AI's pattern recognition and code generation with human creativity, domain expertise, and critical thinking. Use AI as a powerful tool, but keep your judgment and expertise at the center of development decisions.

---

## 4. Choosing the Right Tool for Your Workflow

With dozens of AI coding tools available, selecting the right one depends on your needs, environment, and workflow preferences.

### Decision Framework


**Exploratory Data Analysis**
→ [Code Interpreters](#1-code-interpreters-your-sandboxed-ai-analyst): Claude, Gemini, ChatGPT Plus

**Learning to Code**
→ [Code Interpreters](#1-code-interpreters-your-sandboxed-ai-analyst) or [Browser-Based Tools](vibe.md#browser-based-vibe-coding)

**Professional Software Development**
→ [Agentic IDE Tools](vibe.md): Cursor, Windsurf, Claude Code, Cline

**Need MCP Integration**
→ [Claude Desktop](mcp.md) or [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)

**Enterprise/Team Development**
→ [GitHub Copilot](vibe.md#github-copilot) or [Cursor](vibe.md#cursor) Team

**Privacy-Sensitive Projects**
→ [Cline](vibe.md#cline) or [Aider](https://aider.chat/) with local models

**Multi-Language Projects**
→ [Claude Code](vibe.md#claude-code-vs-code-extension) or [Cursor](vibe.md#cursor) (excellent multi-language support)

**Terminal-First Workflow**
→ [Aider](https://aider.chat/) or [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)

### Integration with Your Workflow

**For Researchers:**

- Start with [Code Interpreters](#1-code-interpreters-your-sandboxed-ai-analyst) for data analysis
- Progress to [Claude Desktop with MCP](mcp.md) for accessing research databases
- Use [Vibe Coding tools](vibe.md) for reproducible research code

**For Students:**

- Begin with [sandboxed interpreters](#1-code-interpreters-your-sandboxed-ai-analyst) to learn safely
- Experiment with [browser-based tools](vibe.md#browser-based-vibe-coding) for homework
- Transition to [IDE extensions](vibe.md#vs-code-extensions) as skills develop

**For Professional Developers:**

- Choose [agentic tools](vibe.md) based on your IDE preference
- Leverage [MCP](mcp.md) for project-specific integrations
- Follow [security best practices](#security-considerations) rigorously

**For Teams:**

- Standardize on [enterprise tools](vibe.md#github-copilot) with centralized billing
- Establish code review processes for AI-generated code
- Document policies on AI tool usage and data sharing

---

## 5. The Path Forward: Vibe Coding and Beyond

This lesson introduced the landscape of AI-powered code generation and execution. You've learned about:

- **[Code Interpreters](#1-code-interpreters-your-sandboxed-ai-analyst)** for safe, sandboxed analysis
- **[Code Execution Frameworks](#2-code-execution-frameworks-your-ai-pair-programmer)** for IDE integration
- **[Best practices](#3-best-practices--ethical-considerations)** for security, privacy, and responsible use
- **[Tool selection](#4-choosing-the-right-tool-for-your-workflow)** based on your needs

### Next Steps

!!! success "Ready to Start Vibe Coding?"

    Now that you understand the foundations, dive deeper into hands-on AI-assisted development:

    **:material-arrow-right: [Explore Vibe Coding](vibe.md)**
    Learn how to set up and use modern agentic coding tools in your preferred development environment.

    **:material-arrow-right: [Understand Model Context Protocol (MCP)](mcp.md)**
    Discover how MCP enables deep integration between AI and your development tools, enabling sophisticated agentic behaviors.

    **:material-arrow-right: [Learn About Agentic AI](agentic.md)**
    Understand the principles behind autonomous AI systems and how they're transforming software development.

### Recommended Learning Path

1. **Experiment with Code Interpreters** (30 minutes)
   - Try Claude, Gemini, or ChatGPT Plus
   - Upload a dataset and perform analysis
   - Get comfortable with natural language coding

2. **Install a Vibe Coding Tool** (1 hour)
   - Follow our [Vibe Coding setup guide](vibe.md)
   - Start with Claude Code or Cursor
   - Try basic code generation and editing

3. **Explore MCP Integration** (1-2 hours)
   - Set up [Claude Desktop with MCP](mcp.md)
   - Connect to filesystem and GitHub servers
   - Experience context-aware assistance

4. **Practice Best Practices** (Ongoing)
   - Review all AI-generated code
   - Develop your prompting skills
   - Learn from successes and failures

5. **Build Real Projects** (Weeks to months)
   - Apply AI assistance to actual work
   - Develop your AI collaboration style
   - Share learnings with your community

### Staying Current

The AI coding landscape evolves rapidly. Stay informed:

- Follow tool announcements and changelogs
- Join developer communities (Discord, Reddit, forums)
- Experiment with new features in safe environments
- Read our [Vibe Coding guide](vibe.md) for regular updates
- Check [MCP documentation](mcp.md) for new server integrations

---

## Assessment

??? question "What is the primary difference between a sandboxed Code Interpreter (like in ChatGPT) and a Code Execution Framework (like GitHub Copilot in VS Code)?"
    
    ??? success "Answer"
        A sandboxed Code Interpreter runs code in a secure, isolated environment provided by the service, disconnected from your local machine. A Code Execution Framework integrates into your local IDE and can read, modify, and execute files directly on your computer.

??? question "True or False: Code generated by an AI assistant is guaranteed to be secure and free of errors."

    ??? failure "False"
        AI-generated code can contain bugs, security vulnerabilities, and biases from its training data. It is crucial to always review, test, and validate any code before using it in a production environment.

??? question "Which of the following tasks is best suited for a sandboxed Code Interpreter?"

    1. Refactoring a large, existing codebase in your project.
    2. Quickly analyzing a CSV file you upload to generate a plot.
    3. Building and running a web server on your local machine.
    4. Continuously providing autocompletions as you type in your IDE.

    ??? success "Correct Answer: 2"
        Sandboxed interpreters excel at self-contained tasks involving data you can upload, like analyzing a file. The other tasks are better suited for AI tools integrated directly into a local IDE.

??? question "True or False: Using an open-source Code Execution Framework like Cline or Aider allows you to use locally-run LLMs (e.g., via Ollama) instead of relying on cloud-based APIs."

    ??? success "True"
        One of the key advantages of many open-source tools is flexibility. They often allow you to connect to various LLM backends, including models running on your own hardware, giving you more control over privacy and cost.

??? question "Which technology enables AI agents to access your local file system, run terminal commands, and interact with external tools?"

    1. Code Interpreters
    2. Model Context Protocol (MCP)
    3. Function calling
    4. Extended context windows

    ??? success "Correct Answer: 2"
        Model Context Protocol (MCP) is the standardized communication framework that allows AI agents to interact with local tools, file systems, databases, and external services. While function calling is related, MCP provides the comprehensive protocol for deep integration.

??? question "What is the main security concern when using agentic AI systems that execute code locally?"

    ??? success "Answer"
        Agentic AI systems with local execution have access to your file system, network, terminal, and environment variables. They can read, modify, or delete files, execute arbitrary commands, and potentially access sensitive credentials. Always review commands before execution, follow your organization's security policies, and avoid storing secrets in code.

??? question "Which workflow would be BEST suited for a sandboxed Code Interpreter rather than an agentic IDE tool?"

    1. Refactoring a large codebase with coordinated changes across multiple files
    2. Analyzing a CSV dataset you upload to generate statistical plots
    3. Setting up automated testing and CI/CD for a project
    4. Debugging a complex application with multiple service dependencies

    ??? success "Correct Answer: 2"
        Sandboxed Code Interpreters excel at self-contained tasks with uploaded data, like analyzing a dataset. The other tasks require multi-file awareness, local tool integration, and persistent development workflows—all better suited for agentic IDE tools.

??? question "True or False: AI-generated code should always be considered "best practice" since models are trained on vast amounts of code from expert developers."

    ??? failure "False"
        AI models are trained on public code repositories that may contain outdated patterns, security vulnerabilities, biased implementations, and code that violates best practices. Always review AI-generated code critically, test thoroughly, and verify it meets current standards and your specific requirements.
