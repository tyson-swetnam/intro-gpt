# :simple-claude: Anthropic Claude

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Ways to Access Claude

There are multiple ways to access Claude:

**1. Claude Chat Interface (claude.ai):**

   *   **Go to:** [https://claude.ai/](https://claude.ai/){target=_blank}
   *   **Sign up:** Create an account using your email address or with a Google account
   *   **Log in:** If you already have an account, log in with your credentials

**2. Claude Code (VS Code Extension):**

   *   **Install:** Search for "Claude Code" in VS Code Extensions marketplace or visit [claude.ai/code](https://claude.ai/code){target=_blank}
   *   **Features:** AI pair programming, code generation, debugging, and refactoring directly in VS Code
   *   **Authentication:** Requires Anthropic API key or Claude Pro subscription

**3. Claude Desktop App:**

   *   **Download:** Available for macOS and Windows at [claude.ai/download](https://claude.ai/download){target=_blank}
   *   **Features:** Native desktop experience with keyboard shortcuts, file handling, and system integration
   *   **Model Context Protocol:** Built-in MCP support for connecting to local tools and services

**4. Anthropic API (for Developers):**

   *   **Sign Up:** Go to [https://console.anthropic.com/](https://console.anthropic.com/){target=_blank} to create an account
   *   **API Key:** Generate an API key from your console dashboard
   *   **Documentation:** [https://docs.anthropic.com/](https://docs.anthropic.com/){target=_blank}

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

!!! info "Subscription Plans and Pricing"

    *   **Claude Free:** Access to Claude 4.5 Sonnet with usage limits
    *   **Claude Pro ($20/month):**
        - 5x more usage vs free tier
        - Access to Claude 4.5 Opus and Claude 4.5 Haiku
        - Priority access during high-traffic periods
        - Early access to new features
    *   **Claude Max ($100-200/month):**
        - Extended usage limits
        - Priority access to newest models
    *   **Claude Team ($25-30/user/month, min 5 users):**
        - Everything in Pro
        - Central billing and administration
        - Team collaboration features
    *   **API Pricing (per million tokens, as of January 2026):**
        - Claude 4.5 Sonnet: $3 input / $15 output
        - Claude 4.5 Opus: $15 input / $75 output
        - Claude 4.5 Haiku: $0.25 input / $1.25 output

    **Compare with other AI platforms:** See [Choosing the Right AI Platform](choose.md) for detailed comparisons with ChatGPT, Gemini, and more.

## Using Claude

**Web Chat Interface (claude.ai):**

*   **Prompting:** Type your requests or questions into the chat box. Be clear and specific in your prompts
*   **Conversation History:** Claude remembers the context of your conversation within the current chat
*   **Projects:** Organize chats into projects with custom instructions and shared knowledge
*   **Artifacts:** Claude can create and edit code, documents, and diagrams in a dedicated panel
*   **File Uploads:** Upload images, PDFs, and text files (up to 5 files, 10MB each)

**Claude Code (VS Code Extension):**

*   **Installation:** 
    1. Open VS Code
    2. Go to Extensions (Ctrl/Cmd + Shift + X)
    3. Search for "Claude Code"
    4. Click Install
*   **Features:**
    - Inline code completion
    - Chat interface within VS Code
    - Code explanation and refactoring
    - Multi-file context awareness
    - Terminal command suggestions

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
        model="claude-4-5-sonnet-20260115",
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
*   **Large Context Window:** Up to 200,000 tokens (approximately 150,000 words or 500 pages)
*   **Vision Capabilities:** Can analyze images, charts, diagrams, and screenshots

## Claude Model Family

**Latest Models (January 2026):**

*   **Claude 4.5 Sonnet:**
    - Most capable balanced model
    - Best for coding, analysis, and creative tasks
    - Excellent performance-to-cost ratio
    - Model ID: `claude-4-5-sonnet-20260115`

*   **Claude 4.5 Opus:**
    - Most capable flagship model
    - Best for complex reasoning and advanced tasks
    - Highest intelligence and capability
    - Model ID: `claude-4-5-opus-20251101`

*   **Claude 4.5 Haiku:**
    - Fast and cost-effective
    - Great for simple tasks and high-volume applications
    - Optimized for speed and efficiency
    - Model ID: `claude-4-5-haiku-20260115`

!!! note "Model Selection"
    Claude 4.5 Sonnet is recommended for most use cases as it offers the best combination of capability, speed, and cost. Use Opus for tasks requiring maximum intelligence and reasoning, and Haiku for high-volume, simple tasks.


## Further Resources

*   **Anthropic Website:** [https://www.anthropic.com/](https://www.anthropic.com/){target=_blank}
*   **Claude Documentation:** [https://docs.anthropic.com/](https://docs.anthropic.com/){target=_blank}
*   **API Reference:** [https://docs.anthropic.com/en/api/](https://docs.anthropic.com/en/api/){target=_blank}
*   **Prompt Engineering Guide:** [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering){target=_blank}
*   **Claude Code Documentation:** [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code){target=_blank}
*   **Model Context Protocol:** [https://modelcontextprotocol.io](https://modelcontextprotocol.io){target=_blank}
*   **Anthropic Cookbook:** [https://github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook){target=_blank}
*   **Community Discord:** [https://discord.gg/anthropic](https://discord.gg/anthropic){target=_blank}

!!! tip "Getting Started Recommendations"
    1. Start with the free tier at [claude.ai](https://claude.ai) to explore Claude's capabilities
    2. For developers, try Claude Code in VS Code for an enhanced coding experience
    3. Install Claude Desktop if you want MCP integration and native OS features
    4. Experiment with different models to find the right balance of capability and cost for your needs