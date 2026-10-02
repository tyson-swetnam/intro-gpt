---
type: Setup Guide
title: Anthropic Claude
description: >-
  How to access Anthropic Claude via claude.ai, Claude Code, the desktop app,
  and the API, plus MCP setup, September 2026 plan pricing, and model tiers.
resource: https://tyson-swetnam.github.io/intro-gpt/claude/
tags: [setup, anthropic, pricing, mcp]
sources:
  - resource: https://platform.claude.com/docs/en/about-claude/models/overview
    title: Claude models overview
  - resource: https://claude.com/pricing
    title: Claude pricing
  - resource: https://docs.claude.com/
    title: Claude Documentation
  - resource: https://modelcontextprotocol.io
    title: Model Context Protocol
  - resource: https://claude.ai/
    title: Claude.ai
  - resource: https://code.claude.com/docs/en/overview
    title: Claude Code Documentation
  - resource: https://github.com/anthropics/anthropic-cookbook
    title: Anthropic Cookbook
  - resource: https://claude.com/solutions/education
    title: Claude for Education
generated:
  by: human:tswetnam
  at: "2026-09-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2026-05-09T19:43:45Z"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# :simple-claude: Anthropic Claude

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Ways to Access Claude

There are multiple ways to access Claude:

**1. Claude Chat Interface (claude.ai):**

   *   **Go to:** [https://claude.ai/](https://claude.ai/){target=_blank}
   *   **Sign up:** Create an account using your email address or with a Google account
   *   **Log in:** If you already have an account, log in with your credentials

**2. Claude Code (terminal, VS Code/JetBrains, desktop app, and web):**

   *   **Install:** `curl -fsSL https://claude.ai/install.sh | bash` (recommended) or `npm install -g @anthropic-ai/claude-code`, then run `claude` in your project folder; also available as a VS Code / JetBrains extension, in the Claude desktop app, and on the web at [claude.ai/code](https://claude.ai/code){target=_blank}. Docs: [code.claude.com/docs](https://code.claude.com/docs/en/overview){target=_blank}
   *   **Features:** Agentic pair programming — reads your codebase, writes and refactors code across files, runs commands, and manages Git
   *   **Authentication:** Included with Pro, Max, Team, and Enterprise plans, or use an API key

**3. Claude Desktop App:**

   *   **Download:** Available for macOS and Windows at [claude.ai/download](https://claude.ai/download){target=_blank}
   *   **Features:** Native desktop experience with keyboard shortcuts, file handling, and system integration
   *   **Model Context Protocol:** Built-in MCP support for connecting to local tools and services

**4. Anthropic API (for Developers):**

   *   **Sign Up:** Go to [https://console.anthropic.com/](https://console.anthropic.com/){target=_blank} to create an account
   *   **API Key:** Generate an API key from your console dashboard
   *   **Documentation:** [https://docs.claude.com/](https://docs.claude.com/){target=_blank}

!!! Warning "**Treat your API key like a password**" 
    Do not share it publicly or commit it to version control platforms (like GitHub).


## Model Context Protocol (MCP)

The Model Context Protocol is an open standard that enables Claude to interact with external tools and data sources:

**What is MCP?**

*   **Purpose:** Allows Claude to connect to databases, APIs, files, and other tools on your computer
*   **Security:** Runs locally with your explicit permission for each connection
*   **Open Standard:** Developed by Anthropic and available as open-source

**Installing MCP:**

1. **For Claude Desktop:**

   - MCP support is built into Claude Desktop
   - Configure servers in Settings → Developer → Model Context Protocol
   - Add server configurations in JSON format

2. **Example MCP Configuration:**

   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
       },
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
         }
       }
     }
   }
   ```

3. **Popular MCP Servers:**
   - **Filesystem:** Access local files and directories
   - **GitHub:** Interact with GitHub repositories
   - **PostgreSQL:** Query databases
   - **Slack:** Read Slack messages
   - **Google Drive:** Access Google Drive files

**Learn More:** [modelcontextprotocol.io](https://modelcontextprotocol.io){target=_blank}

!!! info "Subscription Plans and Pricing (as of September 2026 — check [claude.com/pricing](https://claude.com/pricing){target=_blank} for current rates)"

    *   **Claude Free ($0):** Access to the current Sonnet-tier model with usage limits
    *   **Claude Pro ($20/month, or $17/month annual):**
        - 5x more usage vs free tier
        - Includes Claude Code, Claude in Chrome, Claude Science, and Projects
        - Access to the Opus tier
        - Priority access during high-traffic periods
        - Early access to new features
    *   **Claude Max ($100/month, 5x Pro; $200/month, 20x Pro):**
        - Extended usage limits
        - Priority access to newest models
    *   **Claude Team Standard ($25/seat/month, or $20/seat/month annual):**
        - Everything in Pro, **including Claude Code**
        - SAML SSO and admin controls
        - Central billing and administration
        - Team collaboration features
    *   **Claude Team Premium ($125/seat/month, or $100/seat/month annual):**
        - 5x Team Standard usage
    *   **Claude Enterprise ($20/seat/month billed annually, plus usage at API rates):** contact sales
    *   **Claude for Education:** institutional plans with learning mode, Claude Code, and API access; there is no individual student discount — see [claude.com/solutions/education](https://claude.com/solutions/education){target=_blank}
    *   **For researchers:**
        - [Anthropic AI for Science](https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program){target=_blank}: up to $20,000 in API credits for 6 months
        - [Team plan for scientists](https://claude.com/programs/team-plan-for-scientists){target=_blank}: PIs get free Team Standard seats and Premium seats at $15/seat for 12 months
    *   **API Pricing (per million tokens, as of September 2026 — check the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview){target=_blank} for current rates):**
        - Claude Fable 5.1 (`claude-fable-5-1`, frontier): $10 input / $50 output
        - Claude Opus 5.5 (`claude-opus-5-5`, released Sept 22, 2026): $4 input / $20 output
        - Claude Sonnet 5.5 (`claude-sonnet-5-5`, released Sept 28, 2026): $2 input / $10 output
        - Claude Haiku 4.5 (`claude-haiku-4-5`, fast & cost-efficient): $1 input / $5 output
        - Context window: 1M tokens on Fable, Opus, and Sonnet; 200K on Haiku 4.5
        - Prompt caching: cache reads cost 10% of the input price (5% on Opus 5.5, 2.5% on Fable 5.1); cache writes 1.25x (5 min) or 2x (1 hr)
        - Batch API: 50% off input and output
        - Also available on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry

    **Compare with other AI platforms:** See [Choosing the Right AI Platform](choose.md) for detailed comparisons with ChatGPT, Gemini, and more.

## Using Claude

**Web Chat Interface (claude.ai):**

*   **Prompting:** Type your requests or questions into the chat box. Be clear and specific in your prompts
*   **Conversation History:** Claude remembers the context of your conversation within the current chat
*   **Projects:** Organize chats into projects with custom instructions and shared knowledge
*   **Artifacts:** Claude can create and edit code, documents, and diagrams in a dedicated panel
*   **File Uploads:** Upload images, PDFs, and text files (up to 5 files, 10MB each)

**Claude Code (terminal, VS Code/JetBrains, desktop app, and web):**

*   **Installation:**
    1. Run `curl -fsSL https://claude.ai/install.sh | bash` (recommended) or `npm install -g @anthropic-ai/claude-code`
    2. Open a terminal in your project folder and run `claude`
    3. Optionally install the "Claude Code" extension for VS Code or JetBrains, or use it from the Claude desktop app or [claude.ai/code](https://claude.ai/code){target=_blank}
    4. Sign in with your Claude account (Pro, Max, Team, or Enterprise) or an API key
*   **Features:**
    - Agentic coding: reads, writes, and refactors code across multiple files
    - Runs tests and shell commands and manages Git through conversation
    - Chat panel and inline edits in VS Code and JetBrains
    - Multi-file context awareness
    - Full walkthrough: [Claude Code tutorial](claude-code.md) and [code.claude.com/docs](https://code.claude.com/docs/en/overview){target=_blank}

**Claude Desktop App:**

*   **Installation:**
    - **macOS:** Download from [claude.ai/download](https://claude.ai/download){target=_blank} and drag to Applications
    - **Windows:** Download installer and follow setup wizard
*   **Features:**
    - Native OS integration
    - Global keyboard shortcuts
    - MCP server connections
    - Local file access (with permission)
    - Offline viewing of past conversations

**Anthropic API:**

*   **Quick Start (Python):**
    ```python
    from anthropic import Anthropic
    
    client = Anthropic(api_key="your-api-key")
    
    response = client.messages.create(
        model="claude-sonnet-5-5",  # current IDs: https://platform.claude.com/docs/en/about-claude/models/overview
        max_tokens=1000,
        messages=[
            {"role": "user", "content": "Hello, Claude!"}
        ]
    )
    print(response.content[0].text)
    ```
*   **SDKs Available:** Python, TypeScript/JavaScript, Go, and community SDKs
*   **Use Cases:** Chatbots, content generation, code assistance, data analysis

## Tips for Using Claude

*   **Be Specific:** Provide clear instructions and context in your prompts.
*   **Iterate:** Refine your prompts based on Claude's responses to improve the results.
*   **Use System Prompts:** For complex or multi-step tasks, consider using system prompts to provide overall instructions to guide Claude's behavior.
*   **Experiment:** Try different prompting techniques and model settings to find what works best for your use case.

## About Claude

Claude is a family of large language models (LLMs) developed by Anthropic, a company focused on AI safety and research. Claude is known for:

*   **Helpful and Honest Responses:** Designed with Constitutional AI for safer, more aligned outputs
*   **Advanced Reasoning:** Excels at complex analysis, math, and multi-step problem-solving
*   **Strong Coding Abilities:** Excellent for software development, debugging, and code review
*   **Large Context Window:** 1M tokens (about 750,000 words) on current models
*   **Vision Capabilities:** Can analyze images, charts, diagrams, and screenshots

## Claude Model Family

Anthropic publishes Claude in tiers. As of September 2026 the current lineup is **Fable 5.1**, **Opus 5.5**, **Sonnet 5.5**, and **Haiku 4.5**. For an authoritative, up-to-date list of model IDs, see the [Claude models overview](https://platform.claude.com/docs/en/about-claude/models/overview){target=_blank}.

*   **Fable (Claude Fable 5.1):**
    - Frontier tier — Anthropic's most capable model, for the hardest reasoning and long-running agentic tasks
    - Model ID: `claude-fable-5-1`

*   **Opus (Claude Opus 5.5):**
    - Flagship tier — complex reasoning and advanced coding at a lower price than Fable
    - Model ID: `claude-opus-5-5`

*   **Sonnet (Claude Sonnet 5.5):**
    - Balanced tier — best for everyday coding, analysis, and creative tasks, with an excellent performance-to-cost ratio
    - Model ID: `claude-sonnet-5-5`

*   **Haiku (Claude Haiku 4.5):**
    - Fast, cost-effective tier — great for simple tasks and high-volume applications
    - Model ID: `claude-haiku-4-5`

!!! note "Model Selection"
    The Sonnet tier is recommended for most use cases as it offers the best combination of capability, speed, and cost. Use Opus or Fable for tasks requiring maximum intelligence and reasoning, and Haiku for high-volume, simple tasks.


## Further Resources

*   **Anthropic Website:** [https://www.anthropic.com/](https://www.anthropic.com/){target=_blank}
*   **Claude Documentation:** [https://docs.claude.com/](https://docs.claude.com/){target=_blank}
*   **API Reference:** [https://docs.claude.com/en/api/](https://docs.claude.com/en/api/){target=_blank}
*   **Prompt Engineering Guide:** [https://docs.claude.com/en/docs/build-with-claude/prompt-engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering){target=_blank}
*   **Claude Code Documentation:** [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview){target=_blank}
*   **Pricing:** [https://claude.com/pricing](https://claude.com/pricing){target=_blank}
*   **Model Context Protocol:** [https://modelcontextprotocol.io](https://modelcontextprotocol.io){target=_blank}
*   **Anthropic Cookbook:** [https://github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook){target=_blank}
*   **Community Discord:** [https://discord.gg/anthropic](https://discord.gg/anthropic){target=_blank}

!!! tip "Getting Started Recommendations"
    1. Start with the free tier at [claude.ai](https://claude.ai) to explore Claude's capabilities
    2. For developers, try Claude Code in your terminal or VS Code for an enhanced coding experience
    3. Install Claude Desktop if you want MCP integration and native OS features
    4. Experiment with different models to find the right balance of capability and cost for your needs