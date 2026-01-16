# Claude Code: Setup and Usage Tutorial

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Claude Code

This tutorial will guide you through setting up and using **Claude Code**—Anthropic's AI-powered development tool.

Claude Code acts as an intelligent pair programmer that understands context, writes code, creates documentation, and helps you build better software faster.

!!! Tip "What You'll Learn"

    This tutorial covers both the **Claude Code CLI** (command-line interface) and the **Claude Code VS Code Extension**. We'll highlight the differences and help you choose the right tool for your workflow.

    By the end of this tutorial, you'll be able to:

    - Set up Claude Code in Terminal or VS Code Extension
    - Create and manage GitHub repositories using the GitHub `gh` CLI
    - Initialize Claude Code with existing codebases or start new projects
    - Create custom agents for specialized development tasks
    - Build slash commands to automate common workflows
    - Integrate Claude Code with your Git workflow
    - Apply best practices for secure, efficient AI-assisted development
    - Understand AI Sandboxes and their importance for AI Safety

!!! Info "Prerequisites"

    Before starting this tutorial, you should have:

    :material-bash: Basic command-line/terminal experience
    
    :material-git: Familiarity with Git and version control concepts
    
    :simple-github: A GitHub account
    
    :material-microsoft-visual-studio-code: A text editor or IDE (VS Code recommended)
    
    :material-lightbulb-on-10: Willingness to experiment and learn!


---

## 1. What is Claude Code?

**Claude Code** is an AI-powered development assistant built by Anthropic that integrates directly into your development workflow. Unlike simple code completion tools, Claude Code is an [**agentic AI system**](agentic.md) capable of:

- **Understanding entire codebases** through contextual analysis
- **Writing and editing code** across multiple files simultaneously
- **Running commands** in your terminal to test and verify changes
- **Debugging errors** by analyzing stack traces and suggesting fixes
- **Generating documentation** that stays in sync with your code
- **Creating tests** based on your implementation
- **Refactoring** code while maintaining functionality

Claude Code represents the evolution of AI-assisted development—moving beyond autocomplete to truly collaborative coding experiences often called [**"vibe coding"**](vibe.md).

### CLI vs VS Code Extension: Which Should You Use?

Claude Code comes in two primary forms, each suited to different workflows:

| Feature | Claude Code CLI | Claude Code VS Code Extension |
|---------|----------------|------------------------------|
| **Platform** | :simple-gnubash: Terminal/Command Line | :material-microsoft-visual-studio-code: VS Code Editor |
| **Installation** | :simple-gnubash: `npm install -g @anthropic-ai/claude-code` | VS Code Extensions Marketplace |
| **Interface** | Text-based conversations in terminal | Integrated chat panel + inline edits |
| **File Editing** | Creates/modifies files via CLI commands | Direct in-editor modifications |
| **Context Awareness** | Full project directory access | VS Code workspace integration |
| **Terminal Integration** | Native terminal environment | VS Code integrated terminal |
| **Best For** | Terminal-first developers, automation, CI/CD | VS Code users, visual development, GUI preferences |
| **Keyboard Shortcuts** | Standard terminal shortcuts | VS Code keybindings + custom shortcuts |
| **MCP Support** | Yes, via configuration | Yes, via configuration |
| **Multi-Project** | Switch directories manually | Workspace support |

??? tip "Recommendation: Start with Your Comfort Zone"
    If you're primarily a terminal user who lives in vim, emacs, or tmux, start with the **CLI**. If you spend most of your time in VS Code, start with the **Extension**. You can always use both!

### Key Capabilities

Both versions of Claude Code share these powerful capabilities:

**Context Understanding**
- Reads and analyzes your entire project structure
- Understands dependencies, frameworks, and patterns
- Maintains conversation context across sessions
- Integrates with [Model Context Protocol (MCP)](mcp.md) for extended capabilities

**Code Generation & Editing**
- Generates new files, functions, and modules
- Refactors existing code across multiple files
- Applies consistent coding styles and patterns
- Suggests optimizations and improvements

**Tool Integration**
- Executes terminal commands (with your approval)
- Runs tests and interprets results
- Interacts with Git for version control
- Connects to external APIs and databases via MCP

**Customization**
- Create custom agents for specialized tasks
- Define slash commands for repeated workflows
- Configure behavior and preferences
- Integrate with your existing tools

### How Claude Code Differs from Other Tools

Compared to other AI coding assistants:

- **vs. GitHub Copilot**: More conversational, can edit multiple files, stronger at architectural changes
- **vs. Cursor**: Official Anthropic tool, different pricing model, native MCP support
- **vs. ChatGPT/Claude Web**: Direct file system access, runs locally, part of development workflow
- **vs. Cline/Roo Code**: Official Anthropic tool, integrated experience, ongoing support

For a detailed comparison of all vibe coding tools, see our [**Vibe Coding Guide**](vibe.md).

### Integration with the AI Ecosystem

Claude Code is part of a broader AI development ecosystem:

- **Model Context Protocol (MCP)**: Enables Claude Code to connect to databases, APIs, and external services—see our [MCP Documentation](mcp.md)
- **Agentic AI**: Claude Code employs agentic patterns for autonomous problem-solving—learn more in [Agentic AI](agentic.md)
- **Code Interpreters**: Can execute code in sandboxed environments—covered in [Code Generation with LLMs](code.md)

---

## 2. Prerequisites & Account Setup

Before installing Claude Code, you need access to Claude's API. There are two main approaches.

### 2.1 Account Options

#### Option 1: Claude Pro/Team Subscription

**Claude Pro** ($20/month) or **Claude Team** ($25/user/month, minimum 5 users) subscriptions include:

- Access to Claude Code CLI and VS Code Extension
- Extended usage limits (5x more than free tier)
- Priority access during high-traffic periods
- Access to all Claude models (Sonnet, Opus, Haiku)
- Early access to new features

**Best for**: Individual developers, small teams, and frequent users

**Sign up**: [claude.ai](https://claude.ai){target=_blank}

#### Option 2: Anthropic API Key

For programmatic access and integration:

- **Sign up**: [console.anthropic.com](https://console.anthropic.com){target=_blank}
- **Pricing**: Pay-per-use based on tokens (see pricing below)
- **API key management**: Generate keys in console dashboard
- **Usage tracking**: Monitor consumption in real-time

**Best for**: Developers who want fine-grained control, batch processing, or integration with other tools

!!! info "API Pricing (January 2026)"
    Per million tokens:

    - **Claude 4.5 Sonnet**: $3 input / $15 output
    - **Claude 4.5 Opus**: $15 input / $75 output
    - **Claude 4.5 Haiku**: $0.25 input / $1.25 output

    For most coding tasks, Claude 4.5 Sonnet provides the best balance of capability and cost.

!!! warning "Treat Your API Key Like a Password"
    **Never commit API keys to version control!**

    - Store in environment variables
    - Use `.env` files (and add to `.gitignore`)
    - Rotate keys regularly
    - Revoke compromised keys immediately

    See [Security Best Practices](#83-security-privacy) for more details.

#### Comparison: Subscription vs API Key

| Aspect | Pro/Team Subscription | API Key |
|--------|----------------------|---------|
| **Billing** | Flat monthly rate | Usage-based (per token) |
| **Predictability** | Fixed cost | Variable cost |
| **Usage Limits** | Session-based limits | Token-based limits |
| **Best For** | Regular development work | Automation, batch jobs, experimentation |
| **Administration** | Individual or team billing | Developer console management |

### 2.2 System Requirements

#### Operating System

Claude Code supports:

- :material-apple: **macOS** 10.15 (Catalina) or later
- :material-microsoft-windows: **Windows** 10/11 (with WSL2 recommended for CLI)
- :simple-linux: **Linux** (Ubuntu 20.04+, Fedora 35+, or equivalent)

#### Required Software

**Node.js and npm** (for CLI installation):
- Node.js v16.0.0 or later
- npm v7.0.0 or later
- Check versions: `node --version && npm --version`
- Install from [nodejs.org](https://nodejs.org){target=_blank}

**Git**:
- Git v2.20.0 or later
- Check version: `git --version`
- Install from [git-scm.com](https://git-scm.com){target=_blank}

**For VS Code Extension**:
- Visual Studio Code v1.75.0 or later
- Download from [code.visualstudio.com](https://code.visualstudio.com){target=_blank}

#### AI Sandbox Environments (Optional)

For isolated, secure, or team-based development environments, Claude Code works in:

**Docker Containers**
- Run Claude Code in isolated containers
- Useful for reproducible environments
- See [Docker Documentation](https://docs.docker.com){target=_blank} for setup

**Virtual Machines**
- Full OS isolation for security-sensitive work
- Supports all major VM platforms (VirtualBox, VMware, Hyper-V)
- Good for institutional policies requiring sandboxes

**Jupyter Lab**
- Integrate Claude Code into notebook workflows
- See our [Jupyter AI Guide](jupyter.md) for details
- Useful for data science and research contexts

**Cloud Development Environments**
- GitHub Codespaces
- GitPod
- Cloud9 (AWS)
- Replit

??? info "When to Use Sandboxes"
    Consider sandbox environments if you:

    - Work with sensitive or proprietary code
    - Need compliance with institutional security policies
    - Want reproducible development environments
    - Are teaching or conducting workshops
    - Need to test code in isolated environments

---

## 3. Installation Guide

This section covers installing both the Claude Code CLI and the VS Code Extension. You can install one or both depending on your workflow preferences.

### 3.1 Claude Code CLI

#### Installation on macOS/Linux

Open your terminal and run:

```bash
# Install Claude Code globally via npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude-code --version
```

Expected output:
```
claude-code version 1.x.x
```

#### Installation on Windows

**Option 1: Using WSL2 (Recommended)**

Windows Subsystem for Linux provides the best experience:

```bash
# In WSL2 terminal
npm install -g @anthropic-ai/claude-code
claude-code --version
```

**Option 2: PowerShell/Command Prompt**

```powershell
# In PowerShell or CMD
npm install -g @anthropic-ai/claude-code
claude-code --version
```

#### Authentication Setup

After installation, authenticate with your Claude account:

```bash
# Start authentication flow
claude-code auth login
```

This will:

1. Open your browser to authenticate
2. Ask you to authorize Claude Code
3. Save your credentials securely

**For API key users:**

```bash
# Set API key via environment variable
export ANTHROPIC_API_KEY="your-api-key-here"

# Or use config file
claude-code auth set-key
```

!!! tip "Environment Variables"
    Add to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

    ```bash
    export ANTHROPIC_API_KEY="your-api-key-here"
    ```

    Then reload: `source ~/.zshrc`

#### Basic Configuration

Configure Claude Code preferences:

```bash
# Set default model
claude-code config set model claude-4-5-sonnet-20260115

# Set default editor
claude-code config set editor code  # or vim, nano, etc.

# View current configuration
claude-code config list
```

#### Verification

Test your installation:

```bash
# Run a simple command
claude-code --help

# Test authentication
claude-code auth status

# Quick test conversation
claude-code chat "Hello, Claude!"
```

### 3.2 Claude Code VS Code Extension

#### Installing from Marketplace

1. **Open VS Code**

2. **Open Extensions View**
   - Click Extensions icon in sidebar (or `Ctrl/Cmd + Shift + X`)

3. **Search for "Claude Code"**
   - Type "Claude Code" in search box
   - Look for official Anthropic extension

4. **Install**
   - Click "Install" button
   - Wait for installation to complete

5. **Reload VS Code**
   - Click "Reload" if prompted

#### Alternative: Command Line Installation

```bash
code --install-extension anthropic.claude-code
```

#### Initial Setup Wizard

After installation, the setup wizard will guide you through:

1. **Authentication**
   - Sign in with your Claude account
   - Or enter API key

2. **Model Selection**
   - Choose default model (Sonnet recommended)
   - Can change per-conversation

3. **Permissions**
   - File access permissions
   - Terminal access permissions
   - Confirm security settings

4. **Workspace Configuration**
   - Optional: configure per-workspace settings
   - Set up `.claude` directory

#### Authentication

**For Claude Pro/Team users:**

1. Click "Sign in with Claude" in extension
2. Authorize in browser
3. Return to VS Code

**For API key users:**

1. Open VS Code settings (`Cmd/Ctrl + ,`)
2. Search for "Claude Code"
3. Enter API key in settings

Or set via settings.json:

```json
{
  "claude-code.apiKey": "your-api-key-here",
  "claude-code.defaultModel": "claude-4-5-sonnet-20260115"
}
```

#### Extension Settings Overview

Key settings to configure:

- **Default Model**: Which Claude model to use
- **Auto-save**: Whether to save files before running commands
- **Context Window**: How much code to include in context
- **Terminal Integration**: Enable/disable terminal access
- **MCP Servers**: Configure Model Context Protocol connections

Access settings: `Preferences > Settings > Extensions > Claude Code`

#### Verification

Verify the extension is working:

1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Type "Claude Code: Chat"
3. Send a test message
4. Confirm Claude responds

### 3.3 GitHub CLI Setup

The GitHub CLI (`gh`) simplifies repository management and integrates beautifully with Claude Code workflows.

#### Installing gh Client

**macOS:**

```bash
# Using Homebrew
brew install gh

# Verify installation
gh --version
```

**Windows:**

```powershell
# Using winget
winget install --id GitHub.cli

# Or using Chocolatey
choco install gh

# Verify
gh --version
```

**Linux (Ubuntu/Debian):**

```bash
# Add GitHub CLI repository
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y

# Verify
gh --version
```

**Linux (Fedora/CentOS/RHEL):**

```bash
sudo dnf install 'dnf-command(config-manager)'
sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install gh

# Verify
gh --version
```

#### Authentication with GitHub

Authenticate the GitHub CLI:

```bash
# Start authentication flow
gh auth login
```

You'll be prompted to:

1. Choose authentication method (browser recommended)
2. Select protocol (HTTPS or SSH)
3. Authenticate in browser
4. Confirm successful authentication

Verify authentication:

```bash
gh auth status
```

Expected output:
```
✓ Logged in to github.com as your-username
✓ Git operations for github.com configured to use https protocol
```

#### Basic gh Commands Reference

Common commands you'll use with Claude Code:

```bash
# Create a repository
gh repo create my-project --public

# Clone a repository
gh repo clone username/repository

# Create a pull request
gh pr create --title "Feature: Add new component" --body "Description here"

# View repository information
gh repo view

# List your repositories
gh repo list

# Open repository in browser
gh repo view --web

# Check issues
gh issue list

# Create an issue
gh issue create --title "Bug: Something broke" --body "Details"
```

For more commands: `gh --help`

#### Verifying Installation

Test all components are working:

```bash
# Check versions
echo "Node: $(node --version)"
echo "npm: $(npm --version)"
echo "Git: $(git --version)"
echo "GitHub CLI: $(gh --version)"
echo "Claude Code: $(claude-code --version)"
```

All commands should return version numbers without errors.

!!! success "Installation Complete!"
    You now have all the tools needed to start using Claude Code. In the next section, we'll create your first project and start coding with Claude!

---

## 4. Creating Your First Project

Now that you have Claude Code and the GitHub CLI installed, let's create a project and start working with Claude.

### 4.1 Setting Up a New Repository

We'll use the `gh` CLI to create a GitHub repository and clone it locally.

#### Creating a Repository

```bash
# Create a new public repository and clone it
gh repo create my-first-claude-project --public --clone

# Or for a private repository
gh repo create my-private-project --private --clone

# Navigate into the directory
cd my-first-claude-project
```

This command:

1. Creates a repository on GitHub
2. Initializes it with a README
3. Clones it to your local machine
4. Sets up the remote origin

??? tip "Repository Options"
    Additional options for `gh repo create`:

    ```bash
    # Add description
    gh repo create my-project --public --clone \
      --description "My awesome Claude Code project"

    # Add .gitignore template
    gh repo create my-project --public --clone \
      --gitignore Python

    # Add license
    gh repo create my-project --public --clone \
      --license mit

    # Combine options
    gh repo create my-project --public --clone \
      --description "Python web app" \
      --gitignore Python \
      --license apache-2.0
    ```

#### Alternative: Clone Existing Repository

If you already have a repository:

```bash
# Clone a repository
gh repo clone username/repository-name

# Navigate into it
cd repository-name
```

#### Verify Directory Structure

Check what was created:

```bash
# List files (including hidden)
ls -la

# Expected output:
# .
# ..
# .git/
# README.md
```

The `.git` directory indicates this is a Git repository.

### 4.2 Starting Claude Code

Now let's start Claude Code in your project directory.

#### CLI: Starting a Session

Navigate to your project and start Claude Code:

```bash
# Make sure you're in the project directory
cd /path/to/my-first-claude-project

# Start Claude Code
claude-code
```

You'll see Claude Code's interactive prompt:

```
Claude Code v1.x.x
Connected to claude-4-5-sonnet-20260115

Ready to help! Type your message or '/help' for available commands.

You:
```

#### VS Code Extension: Opening Workspace

1. **Open VS Code in your project directory:**

```bash
code /path/to/my-first-claude-project
```

2. **Open Claude Code panel:**
   - Click Claude Code icon in sidebar
   - Or use Command Palette: `Cmd/Ctrl + Shift + P` → "Claude Code: Chat"

3. **Start a conversation:**
   - Type your message in the chat input
   - Press Enter to send

#### Initial Interface Walkthrough

Let's understand the Claude Code interface:

```mermaid
flowchart TB
    Start[You open Claude Code] --> Interface{Interface Type}

    Interface -->|CLI| CLI[Terminal Interface]
    Interface -->|VS Code| VSC[VS Code Panel]

    CLI --> CLI1[Chat input/output]
    CLI --> CLI2[Command history]
    CLI --> CLI3[File changes shown inline]

    VSC --> VSC1[Chat panel on side]
    VSC --> VSC2[Inline code suggestions]
    VSC --> VSC3[Diff viewer for changes]
    VSC --> VSC4[Integrated terminal]

    style CLI fill:#e1f5ff
    style VSC fill:#e1f5ff
```

**CLI Interface Components:**

- **Chat Area**: Your messages and Claude's responses
- **Command Prompt**: Where you type (indicated by `You:`)
- **Status Bar**: Shows current model and connection status
- **File Changes**: Displays diffs when files are modified

**VS Code Extension Components:**

- **Chat Panel**: Conversation history and input (sidebar or panel)
- **Inline Suggestions**: Code completions and edits in editor
- **Diff Viewer**: Compare changes before accepting
- **Status Bar**: Model indicator and settings (bottom of VS Code)
- **Commands**: Access via Command Palette (`Cmd/Ctrl + Shift + P`)

#### First Conversation

Test Claude Code with a simple request:

**CLI:**

```bash
You: Hello! Can you help me understand this repository?
```

**VS Code:**

Type in chat panel:
```
Hello! Can you help me understand this repository?
```

Claude will respond, analyzing the directory structure and asking what you'd like to do next.

---

## 5. Initialization: Two Paths

When starting with Claude Code, you'll take one of two paths depending on whether you're working with existing code or starting fresh.

### 5.1 Path A: Existing Codebase

Use this approach when you have an established project with existing code.

#### When to Use This Path

- Joining an existing project
- Working with legacy code
- Analyzing unfamiliar codebases
- Adding features to established apps
- Debugging existing implementations

#### Running `/init` Command

The `/init` command tells Claude to comprehensively analyze your codebase:

**CLI:**

```bash
You: /init
```

**VS Code:**

Type in chat:
```
/init
```

#### What Claude Analyzes

When you run `/init`, Claude Code:

1. **Traverses Directory Structure**
   - Maps out folders and files
   - Identifies important directories (`src/`, `tests/`, `docs/`, etc.)
   - Notes configuration files

2. **Identifies Technologies**
   - Programming languages used
   - Frameworks and libraries (from package files)
   - Build tools and task runners
   - Testing frameworks

3. **Analyzes Code Patterns**
   - Architecture and design patterns
   - Code organization conventions
   - Naming conventions
   - Common patterns and idioms

4. **Reads Key Files**
   - README and documentation
   - Package manifests (`package.json`, `requirements.txt`, `Cargo.toml`, etc.)
   - Configuration files (`.env.example`, config files)
   - Entry points (`main.py`, `index.js`, `app.py`, etc.)

5. **Understands Dependencies**
   - External libraries and versions
   - Internal module relationships
   - Import/export patterns

#### Example Output

Here's what Claude might report after analyzing a Python web application:

```
I've analyzed your codebase. Here's what I found:

**Project Structure:**
- Python Flask web application
- Backend API in `src/api/`
- Frontend templates in `templates/`
- Database models in `src/models/`
- Tests in `tests/`

**Key Technologies:**
- Flask 2.3.2 web framework
- SQLAlchemy ORM
- PostgreSQL database
- pytest for testing
- Docker for containerization

**Architecture:**
- MVC pattern with blueprints
- RESTful API design
- Token-based authentication (JWT)
- Database migrations with Alembic

**Entry Point:** `src/app.py`

**Notable Patterns:**
- Factory pattern for app creation
- Repository pattern for data access
- Dependency injection for services

What would you like me to help with?
```

#### Best Practices for Large Projects

When working with large codebases:

**1. Start with High-Level Overview**

```bash
You: /init --summary
```

Get a high-level summary before diving deep.

**2. Focus on Specific Areas**

```bash
You: Can you analyze just the authentication system in src/auth/?
```

Narrow the scope to avoid overwhelming context.

**3. Ask About Specific Patterns**

```bash
You: How is error handling implemented across the codebase?
```

Target specific architectural questions.

**4. Request Diagrams**

```bash
You: Can you create a diagram showing how the main modules interact?
```

Visual representations help with complex systems.

**5. Incremental Exploration**

Don't try to understand everything at once. Start with:
- Entry points and main flows
- Core business logic
- Critical paths
- Then expand to utilities and helpers

??? warning "Context Window Limits"
    Claude has a large context window (200K tokens ≈ 150,000 words), but extremely large codebases might exceed this. If you encounter limits:

    - Focus on specific directories
    - Use `.claudeignore` to exclude generated files, dependencies
    - Ask Claude to analyze subsystems separately
    - Provide context incrementally as needed

### 5.2 Path B: Starting from Scratch

Use this approach when creating a new project from an empty or minimal repository.

#### When to Use This Path

- Starting a new project
- Building a proof of concept
- Learning a new framework
- Creating a tool or utility
- Prototyping an idea

#### Planning Session Workflow

Instead of `/init`, start a planning conversation:

```bash
You: I want to create a new Python CLI tool that helps developers manage their dotfiles. Can you help me plan the structure?
```

Claude will engage in a conversation to understand:

1. **Project Requirements**
   - What problem are you solving?
   - Who are the users?
   - What features are essential?

2. **Technical Decisions**
   - Programming language and version
   - Frameworks or libraries
   - Architecture approach
   - Testing strategy

3. **Project Structure**
   - Directory organization
   - File naming conventions
   - Module breakdown
   - Configuration approach

#### Example Planning Conversation

**You:**
```
I want to create a task management CLI app in Python that stores tasks in a local SQLite database. It should support adding, listing, completing, and deleting tasks.
```

**Claude:**
```
Great! Let's plan this project. Here's what I'm thinking:

**Project Structure:**
```
task-manager/
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── cli.py          # CLI interface (Click or argparse)
│   ├── database.py     # SQLite operations
│   ├── models.py       # Task data model
│   └── commands/
│       ├── __init__.py
│       ├── add.py
│       ├── list.py
│       ├── complete.py
│       └── delete.py
└── tests/
    ├── __init__.py
    ├── test_database.py
    ├── test_commands.py
    └── fixtures/
```

**Technology Stack:**
- Python 3.9+
- Click for CLI framework (better than argparse for this use case)
- SQLite3 (built-in)
- pytest for testing
- Rich for beautiful terminal output (optional but nice)

**Features:**
1. `task add "Task description"` - Add new task
2. `task list [--all|--completed|--pending]` - List tasks
3. `task complete <id>` - Mark task as done
4. `task delete <id>` - Delete task
5. `task init` - Initialize database

Should I proceed with creating these files? Any changes you'd like?
```

**You:**
```
Yes, looks good! Let's also add a priority field to tasks. And use Rich for better output.
```

**Claude:**
```
Perfect! I'll update the plan to include:
- Priority field (LOW, MEDIUM, HIGH)
- Rich library for colored, formatted output
- Priority sorting in list command

Ready to create the project structure?
```

#### Essential Files

Claude will help you create these foundational files:

**1. README.md**

Explains what the project does, how to install, and how to use it:

```bash
You: Create a comprehensive README.md
```

Claude generates:
```markdown
# Task Manager CLI

A simple, elegant command-line task manager built with Python.

## Features

- Add tasks with priorities
- List tasks with filtering
- Mark tasks complete
- Beautiful terminal output

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Add a task
task add "Write documentation" --priority high

# List all tasks
task list

# Complete a task
task complete 1

# Delete a task
task delete 2
```

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```
```

**2. LICENSE**

```bash
You: Add an MIT license
```

Claude creates `LICENSE` with proper MIT license text and your name/year.

**3. .gitignore**

```bash
You: Create a Python .gitignore
```

Claude generates `.gitignore` with common Python exclusions:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/
dist/
build/

# Database
*.db
*.sqlite
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS
.DS_Store
Thumbs.db
```

**4. requirements.txt**

```bash
You: Create requirements.txt with our dependencies
```

```text
click>=8.1.0
rich>=13.0.0
pytest>=7.4.0
pytest-cov>=4.1.0
```

**5. CONTRIBUTING.md (Optional)**

For open-source projects:

```bash
You: Add a CONTRIBUTING.md guide
```

#### Setting Up for Different Languages

Claude can help you structure projects in any language:

**Python:**
```bash
You: Create a Python package structure with setuptools
```

**JavaScript/Node:**
```bash
You: Create a Node.js project with Express and TypeScript
```

**Rust:**
```bash
You: Initialize a Rust project with Cargo
```

**Go:**
```bash
You: Create a Go module with a standard project layout
```

Claude will generate appropriate:
- Directory structures
- Configuration files (`Cargo.toml`, `package.json`, `go.mod`, etc.)
- Build scripts
- Testing setup
- CI/CD templates

#### Integration with MCP

For advanced projects, integrate [Model Context Protocol (MCP)](mcp.md) servers:

```bash
You: Set up MCP to connect to my PostgreSQL database
```

Claude will:
1. Create `.claude/mcp.json` configuration
2. Set up database connection settings
3. Create example queries
4. Configure environment variables

Example MCP configuration:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://localhost/mydb"
      }
    }
  }
}
```

See our [MCP Documentation](mcp.md) for comprehensive setup guides.

!!! tip "Start Simple, Iterate"
    Don't try to plan every detail upfront. Start with a basic structure and let it evolve as you build. Claude can help refactor and reorganize as the project grows.

---

## 6. Working with Custom Agents

One of Claude Code's most powerful features is the ability to create specialized agents for repeated tasks.

### 6.1 What are Agents?

In Claude Code, an **agent** is a specialized AI assistant configured for specific tasks with custom instructions, knowledge, and behaviors.

**How Agents Differ from Regular Prompts:**

| Aspect | Regular Conversation | Custom Agent |
|--------|----------------------|--------------|
| **Instructions** | General Claude behavior | Specialized, task-specific instructions |
| **Context** | Current conversation | Pre-loaded domain knowledge |
| **Consistency** | Varies by prompt | Consistent behavior across uses |
| **Reusability** | Manual copy-paste | Invoked by name or command |
| **Specialization** | General assistance | Expert in specific domain |

**Benefits of Specialized Agents:**

1. **Consistency**: Same approach every time
2. **Efficiency**: No need to repeat instructions
3. **Quality**: Optimized prompts and workflows
4. **Team Alignment**: Shared standards across team
5. **Expertise**: Deep knowledge in specific areas

For deeper understanding of agentic AI concepts, see [Agentic AI](agentic.md).

### 6.2 Creating a Documentation Writer Agent

Let's create a practical example: a documentation writer agent that maintains your project's documentation.

#### Conceptual Explanation

A documentation agent should:

- Understand your documentation style and standards
- Know what type of documentation you need (API docs, tutorials, README updates)
- Follow consistent formatting and tone
- Keep documentation in sync with code changes
- Generate examples and usage instructions

#### Step-by-Step Creation

**Step 1: Create Agents Directory**

```bash
# In your project root
mkdir -p .claude/agents
```

**Step 2: Create Agent Configuration**

Create `.claude/agents/docs-writer.yaml`:

```yaml
name: Documentation Writer
description: Technical documentation specialist for this project
version: 1.0.0

# Instructions for the agent
instructions: |
  You are a technical documentation expert specializing in clear, concise, and
  comprehensive documentation for software projects.

  DOCUMENTATION STANDARDS:
  - Write in clear, active voice
  - Use consistent formatting (Markdown)
  - Include code examples for all features
  - Provide usage examples with realistic scenarios
  - Keep README.md up-to-date with project changes
  - Document all public APIs, functions, and classes
  - Include installation and setup instructions
  - Add troubleshooting sections for common issues

  STYLE GUIDE:
  - Use second person ("you") for instructions
  - Use present tense for descriptions
  - Keep sentences concise (< 20 words)
  - Use bullet points for lists
  - Include code blocks with syntax highlighting
  - Add warnings/notes/tips using appropriate formatting

  DOCUMENTATION TYPES:
  - README.md: Project overview, installation, quick start
  - API.md: Detailed API documentation
  - CONTRIBUTING.md: Contribution guidelines
  - CHANGELOG.md: Version history and changes
  - Inline comments: For complex code sections
  - Docstrings: For all functions and classes

# Domain knowledge
knowledge:
  - "This project follows semantic versioning (MAJOR.MINOR.PATCH)"
  - "Code examples should be runnable without modification"
  - "All public APIs must have docstrings with type hints"
  - "Documentation deploys automatically on merge to main"

# Capabilities
skills:
  - markdown
  - api-documentation
  - technical-writing
  - code-examples
  - tutorial-writing

# Behavior preferences
preferences:
  verbosity: concise
  code_style: pythonic  # or javascript, rust, etc.
  example_complexity: medium
```

**Step 3: Register Agent (if needed)**

Some configurations require explicit registration:

```bash
# CLI
claude-code agents add .claude/agents/docs-writer.yaml

# Or in VS Code settings.json
{
  "claude-code.agents": [
    ".claude/agents/docs-writer.yaml"
  ]
}
```

#### How to Invoke the Agent

**CLI:**

```bash
You: @docs-writer Please document the new authentication module in src/auth.py
```

**VS Code:**

In chat panel:
```
@docs-writer Please document the new authentication module in src/auth.py
```

Or via command palette:
```
Cmd/Ctrl + Shift + P → "Claude Code: Use Agent" → Select "Documentation Writer"
```

#### Example Interaction

**You:**
```
@docs-writer I just added a new function called calculate_fibonacci(n) in src/math_utils.py.
Please add a comprehensive docstring.
```

**Documentation Writer Agent:**
```python
def calculate_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using iterative approach.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The Fibonacci number at position n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> calculate_fibonacci(0)
        0
        >>> calculate_fibonacci(1)
        1
        >>> calculate_fibonacci(10)
        55
        >>> calculate_fibonacci(20)
        6765

    Time Complexity:
        O(n) - Linear time complexity

    Space Complexity:
        O(1) - Constant space complexity

    Note:
        For very large values of n (> 1000), consider using
        memoization or matrix exponentiation for better performance.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

#### When to Use Documentation Agent

Invoke the documentation agent when:

- Adding new features or functions
- Refactoring existing code
- Creating release notes
- Writing tutorials or guides
- Updating API documentation
- Generating changelogs
- Writing contribution guidelines

### 6.3 Other Useful Agent Ideas

Here are other specialized agents you might create (conceptual descriptions):

#### Testing Agent

**Purpose**: Generate comprehensive test suites

**Key Instructions**:
- Write tests for all public functions
- Include edge cases and error conditions
- Use appropriate testing framework (pytest, Jest, etc.)
- Aim for 80%+ code coverage
- Write descriptive test names
- Use fixtures and mocks appropriately

**Invocation**: `@test-writer Generate tests for the UserService class`

#### Code Review Agent

**Purpose**: Provide thorough code reviews with constructive feedback

**Key Instructions**:
- Check for bugs and edge cases
- Identify performance issues
- Suggest best practices
- Point out security vulnerabilities
- Review naming and code style
- Suggest refactoring opportunities
- Be constructive and specific

**Invocation**: `@code-reviewer Please review the changes in src/api/users.py`

#### Refactoring Agent

**Purpose**: Improve code structure without changing behavior

**Key Instructions**:
- Extract functions for repeated code
- Simplify complex conditionals
- Apply SOLID principles
- Improve naming and clarity
- Reduce coupling and increase cohesion
- Preserve existing tests and behavior
- Make incremental, testable changes

**Invocation**: `@refactor-agent Improve the structure of the DataProcessor class`

#### Security Auditor Agent

**Purpose**: Identify security vulnerabilities

**Key Instructions**:
- Check for SQL injection vulnerabilities
- Identify XSS and CSRF risks
- Review authentication and authorization
- Check for insecure dependencies
- Verify proper input validation
- Review secrets management
- Check for information disclosure

**Invocation**: `@security-auditor Audit the login endpoint for vulnerabilities`

#### Performance Optimizer Agent

**Purpose**: Identify and fix performance bottlenecks

**Key Instructions**:
- Profile code for bottlenecks
- Suggest algorithmic improvements
- Identify unnecessary computations
- Recommend caching strategies
- Optimize database queries
- Reduce memory allocations
- Improve concurrency

**Invocation**: `@performance-optimizer Analyze the data processing pipeline`

!!! tip "Creating Your Own Agents"
    Think about tasks you repeat frequently and create specialized agents for them. The more specific the instructions, the better the results!

---

## 7. Custom Slash Commands

Slash commands provide shortcuts for common workflows, turning multi-step processes into single commands.

### 7.1 Understanding Slash Commands

**What are Slash Commands?**

Slash commands are custom shortcuts that trigger predefined workflows in Claude Code. They're like macros or aliases that encapsulate common development tasks.

**Why They're Useful:**

- **Efficiency**: Execute complex workflows with one command
- **Consistency**: Same process every time
- **Team Alignment**: Share common workflows across team
- **Automation**: Reduce manual, repetitive tasks
- **Error Reduction**: Less chance of forgetting steps

**Built-in Commands:**

Claude Code includes several built-in commands:

| Command | Purpose |
|---------|---------|
| `/init` | Analyze codebase structure |
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `/context` | Show current context size |
| `/files` | List files in current context |
| `/model` | Change AI model |
| `/save` | Save conversation to file |

### 7.2 Example: Creating `/commit` Command

Let's create a powerful `/commit` command that automates the git commit workflow.

#### Purpose and Workflow

The `/commit` command should:

1. Show `git status` to review changes
2. Stage all changes (or prompt for selective staging)
3. Generate a descriptive commit message based on changes
4. Create the commit
5. Optionally push to remote

#### Configuration Syntax

Create `.claude/commands/commit.yaml`:

```yaml
name: commit
description: Intelligent git commit with AI-generated message
version: 1.0.0

# Command behavior
workflow:
  - name: check_git_status
    action: run_command
    command: "git status --short"
    description: "Show current changes"

  - name: confirm_changes
    action: prompt_user
    message: "Proceed with committing these changes?"
    options:
      - value: "all"
        label: "Commit all changes"
      - value: "selective"
        label: "Let me choose files"
      - value: "cancel"
        label: "Cancel"

  - name: stage_changes
    action: conditional
    condition: "confirm_changes != 'cancel'"
    then:
      - action: run_command
        command: "git add -A"
        when: "confirm_changes == 'all'"
      - action: prompt_for_files
        when: "confirm_changes == 'selective'"

  - name: analyze_diff
    action: run_command
    command: "git diff --cached"
    store_output: "diff_content"

  - name: generate_message
    action: ai_task
    prompt: |
      Based on this git diff, generate a commit message following conventional commits format:

      <type>(<scope>): <subject>

      <body>

      <footer>

      Types: feat, fix, docs, style, refactor, test, chore

      Git diff:
      ```
      {{diff_content}}
      ```

      Generate a clear, concise commit message that explains what changed and why.
    store_output: "commit_message"

  - name: show_message
    action: display
    content: |
      Proposed commit message:

      {{commit_message}}

      Approve this message?

  - name: confirm_message
    action: prompt_user
    message: "Use this commit message?"
    options:
      - value: "yes"
        label: "Yes, commit with this message"
      - value: "edit"
        label: "Let me edit it"
      - value: "cancel"
        label: "Cancel"

  - name: edit_message
    action: conditional
    condition: "confirm_message == 'edit'"
    then:
      - action: prompt_for_text
        multiline: true
        default: "{{commit_message}}"
        store_output: "commit_message"

  - name: create_commit
    action: conditional
    condition: "confirm_message != 'cancel'"
    then:
      - action: run_command
        command: "git commit -m '{{commit_message}}'"

  - name: ask_push
    action: prompt_user
    message: "Push to remote?"
    options:
      - value: "yes"
        label: "Yes, push now"
      - value: "no"
        label: "No, I'll push later"

  - name: push_changes
    action: conditional
    condition: "ask_push == 'yes'"
    then:
      - action: run_command
        command: "git push"

# Safety settings
safety:
  confirm_before_execute: true
  allow_destructive_ops: false

# Permissions needed
permissions:
  - git
  - filesystem.read
  - filesystem.write
```

#### Simpler Version

If the full workflow is too complex, here's a simpler version:

`.claude/commands/commit-simple.yaml`:

```yaml
name: commit
description: Quick commit with AI-generated message

workflow:
  - action: run_command
    command: "git add -A"

  - action: ai_task
    prompt: "Analyze the git diff and generate a conventional commit message"
    command: "git diff --cached"

  - action: git_commit
    message: "{{ai_output}}"

permissions:
  - git
```

#### Usage Demonstration

**Basic Usage:**

```bash
You: /commit
```

**With Options:**

```bash
You: /commit --no-push
You: /commit --message "fix: resolve login bug"
You: /commit --amend
```

**Example Flow:**

```
You: /commit

Claude Code: Analyzing changes...

Modified files:
  M src/auth.py
  M tests/test_auth.py
  A docs/authentication.md

Proposed commit message:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
feat(auth): add support for OAuth 2.0 authentication

- Implement OAuth2 authentication flow
- Add token validation and refresh logic
- Update authentication tests for new flow
- Add documentation for OAuth setup

Closes #42
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use this commit message? [Yes/Edit/Cancel]: Yes

Creating commit... Done!
Push to remote? [Yes/No]: Yes
Pushing to origin/main... Done!

✓ Committed and pushed successfully!
```

### 7.3 Other Slash Command Ideas

Here are more useful custom commands (conceptual descriptions):

#### `/test` - Run Test Suite

```yaml
name: test
description: Run tests with coverage and report results

workflow:
  - Run pytest with coverage
  - Generate coverage report
  - Show failed tests with context
  - Suggest fixes for failures
```

**Usage**: `/test` or `/test --file tests/test_api.py`

#### `/review` - Code Review Workflow

```yaml
name: review
description: Request code review before merging

workflow:
  - Show uncommitted changes
  - Run linters and formatters
  - Check for common issues
  - Generate review checklist
  - Create pull request (optional)
```

**Usage**: `/review` or `/review --create-pr`

#### `/deploy` - Deployment Workflow

```yaml
name: deploy
description: Deploy to specified environment

workflow:
  - Verify tests pass
  - Check environment variables
  - Build application
  - Run deployment script
  - Verify deployment
  - Tag release
```

**Usage**: `/deploy production` or `/deploy staging --skip-tests`

#### `/docs` - Documentation Generation

```yaml
name: docs
description: Generate or update documentation

workflow:
  - Scan for undocumented functions
  - Generate missing docstrings
  - Update README if needed
  - Build documentation site
  - Show coverage report
```

**Usage**: `/docs` or `/docs --module auth`

#### `/refactor` - Smart Refactoring

```yaml
name: refactor
description: Refactor code with specific pattern

workflow:
  - Analyze current structure
  - Suggest refactoring approach
  - Apply changes incrementally
  - Run tests after each change
  - Create commit if successful
```

**Usage**: `/refactor extract-method` or `/refactor simplify-conditionals`

#### `/fix` - Automated Bug Fixing

```yaml
name: fix
description: Analyze and fix errors

workflow:
  - Run application/tests
  - Capture error messages
  - Analyze stack traces
  - Suggest fixes
  - Apply fix with approval
  - Verify fix works
```

**Usage**: `/fix` or `/fix --error "IndexError on line 42"`

!!! tip "Command Best Practices"
    - Keep commands focused on single workflows
    - Always include confirmation steps for destructive operations
    - Provide clear output at each step
    - Allow customization through parameters
    - Include safety checks and validation

---

## 8. Development Workflow Best Practices

Now that you understand the tools, let's explore effective workflows for daily development with Claude Code.

### 8.1 Typical Development Session

Here's how a productive Claude Code session typically flows:

#### Starting Your Work

**1. Navigate to Project:**

```bash
cd /path/to/your-project
```

**2. Start Claude Code:**

```bash
# CLI
claude-code

# VS Code
code . # Opens VS Code, then open Claude panel
```

**3. Review Context:**

```bash
You: What was I working on last time?
```

Claude can reference conversation history (if saved) or analyze recent git commits.

**4. Set Today's Goal:**

```bash
You: Today I need to implement user authentication. Let's start by planning the approach.
```

#### Iterative Development Flow

**Development Loop:**

```mermaid
flowchart TD
    A[Describe Feature/Fix] --> B[Claude Generates Code]
    B --> C[Review & Discuss]
    C --> D{Satisfactory?}
    D -->|No| E[Request Changes]
    E --> B
    D -->|Yes| F[Apply Changes]
    F --> G[Run Tests]
    G --> H{Tests Pass?}
    H -->|No| I[Debug with Claude]
    I --> B
    H -->|Yes| J[Commit Changes]
    J --> K{More Work?}
    K -->|Yes| A
    K -->|No| L[End Session]

    style F fill:#c8e6c9
    style J fill:#c8e6c9
    style L fill:#e1f5ff
```

**Example Development Flow:**

```bash
# Step 1: Plan the feature
You: I need to add a password reset feature. What's the best approach?

Claude: [Suggests approach with email tokens, expiration, security considerations]

# Step 2: Implement backend
You: Let's start with the backend. Create the password reset endpoint.

Claude: [Generates Flask/Express/etc. endpoint code]

# Step 3: Review and refine
You: Looks good, but let's add rate limiting to prevent abuse.

Claude: [Updates code with rate limiting]

# Step 4: Write tests
You: @test-writer Create tests for the password reset endpoint

Test Agent: [Generates comprehensive test suite]

# Step 5: Run tests
You: /test

Claude: [Runs tests, reports results]

# Step 6: Update documentation
You: @docs-writer Document the new password reset flow

Docs Agent: [Updates API documentation and README]

# Step 7: Commit
You: /commit

Claude: [Creates commit with descriptive message]
```

#### Managing Context

**Keep Context Relevant:**

```bash
# Clear context if conversation gets too long
You: /clear

# Focus on specific files
You: Let's focus on just src/auth.py and tests/test_auth.py

# Remove files from context
You: You can forget about the migration files, we don't need those
```

**Loading Additional Context:**

```bash
# Add files to context
You: Can you also look at config/auth_config.py?

# Load related code
You: Show me other places where we handle authentication
```

#### Conversation Organization

**Use Clear, Specific Requests:**

✅ Good:
```
Refactor the authenticate_user function in src/auth.py to use the Strategy pattern,
making it easier to add new authentication methods.
```

❌ Unclear:
```
Make auth better
```

**Break Down Complex Tasks:**

Instead of:
```
Build a complete user authentication system
```

Do:
```
1. Let's start with the database models for User and Session
2. Next, create the login endpoint
3. Then, implement JWT token generation
[etc.]
```

### 8.2 Git Integration Patterns

Claude Code can be a powerful Git assistant.

#### Commit Message Generation

Let Claude analyze your changes:

```bash
You: /commit

# Or manually:
You: Generate a commit message for my changes
```

Claude will:
- Analyze the diff
- Identify the type of change (feat, fix, refactor, etc.)
- Write a clear, conventional commit message
- Include relevant details and context

**Example Generated Commit:**

```
feat(auth): implement OAuth2 authentication flow

- Add OAuth2 client configuration
- Implement authorization code flow
- Add token refresh mechanism
- Update user model to store OAuth tokens
- Add middleware for OAuth protected routes

This enables users to authenticate using Google, GitHub, and other
OAuth providers instead of just username/password.

Closes #42
```

#### Branch Management Strategies

**Feature Branch Workflow:**

```bash
# Create feature branch
You: Can you help me create a branch for the password reset feature?

Claude: Sure! Run: git checkout -b feature/password-reset

# Work on feature...

# Before merging
You: /review
You: /test
You: /commit
```

**Reviewing Before Merge:**

```bash
You: Compare my feature branch with main and identify any conflicts

Claude: [Analyzes differences, identifies conflicts, suggests resolution]
```

**Rebasing:**

```bash
You: I need to rebase my feature branch on the latest main. Walk me through it safely.

Claude: [Provides step-by-step rebase instructions with safety checks]
```

#### Pull Request Descriptions

Generate comprehensive PR descriptions:

```bash
You: Generate a pull request description for my authentication feature

Claude:
```
```markdown
## Pull Request: Add OAuth2 Authentication

### Summary
Implements OAuth2 authentication flow allowing users to sign in with Google, GitHub, and Microsoft accounts.

### Changes
- ✨ Add OAuth2 client configuration (`src/auth/oauth.py`)
- ✨ Implement authorization code flow
- ✨ Add token management and refresh logic
- 🗃️ Update User model to store OAuth provider info
- 🔒 Add middleware for OAuth-protected routes
- ✅ Add comprehensive test coverage (95%)
- 📝 Update API documentation

### Testing
- [x] Unit tests pass
- [x] Integration tests pass
- [x] Manual testing with Google OAuth
- [x] Manual testing with GitHub OAuth
- [x] Security review completed

### Security Considerations
- OAuth tokens stored encrypted in database
- State parameter used to prevent CSRF
- Strict redirect URI validation
- Token refresh handled automatically

### Breaking Changes
None. Existing username/password authentication continues to work.

### Related Issues
Closes #42
Relates to #38, #45

### Screenshots
[Add screenshots of OAuth login flow]

### Deployment Notes
Requires new environment variables:
- `OAUTH_GOOGLE_CLIENT_ID`
- `OAUTH_GOOGLE_CLIENT_SECRET`
- `OAUTH_GITHUB_CLIENT_ID`
- `OAUTH_GITHUB_CLIENT_SECRET`
```
```

#### Code Review with Claude

Before submitting PR:

```bash
You: @code-reviewer Review my changes and check for issues

Code Reviewer: [Provides detailed feedback on:]
- Potential bugs
- Security concerns
- Performance issues
- Style inconsistencies
- Missing tests
- Documentation gaps
```

### 8.3 Security & Privacy

Developing securely with AI assistance requires careful attention.

#### API Key Management

**Environment Variables:**

Never hardcode API keys:

```python
# ❌ BAD - Hardcoded
api_key = "sk-ant-1234567890"

# ✅ GOOD - Environment variable
import os
api_key = os.getenv("ANTHROPIC_API_KEY")
```

**Setting Environment Variables:**

```bash
# .env file (add to .gitignore!)
ANTHROPIC_API_KEY=your-key-here
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
```

Load in code:

```python
from dotenv import load_dotenv
load_dotenv()
```

**Claude Can Help:**

```bash
You: Review my code for hardcoded secrets

Claude: [Identifies hardcoded credentials and suggests fixes]
```

#### .gitignore Best Practices

Ensure sensitive files are never committed:

```bash
You: Create a comprehensive .gitignore for Python/Node/etc.

Claude: [Generates .gitignore including:]
```

```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Secrets and credentials
*.key
*.pem
*.p12
secrets.yaml
credentials.json

# Database
*.db
*.sqlite
*.sqlite3

# API keys and tokens
.anthropic
.openai
*_key.txt
*_token.txt

# IDE and editors
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db
```

**Verify Nothing Sensitive is Tracked:**

```bash
# Check what's tracked by git
git ls-files

# Check for accidental secrets
You: Scan my repository for potential secrets or API keys

Claude: [Uses regex patterns to identify potential secrets]
```

#### Sensitive Data Handling

**Sanitize Before Sharing with Claude:**

```bash
# ❌ Don't paste
You: Debug this: DATABASE_URL=postgresql://admin:MyPassword123@prod.example.com/db

# ✅ Do paste
You: Debug this: DATABASE_URL=postgresql://user:password@host/db
```

**Use Placeholders:**

```bash
You: Here's my config (I've replaced sensitive values with placeholders):

API_KEY=<redacted>
SECRET=<redacted>
DATABASE_URL=postgresql://USER:PASSWORD@HOST/DATABASE

The issue is...
```

#### Institutional Compliance

!!! danger "Follow Your Organization's Policies"
    Many universities and companies have strict policies about AI tools:

    - **Data Classification**: Don't share classified or sensitive data
    - **Approved Tools**: Use only approved AI services
    - **Code Review**: Additional review may be required for AI-generated code
    - **Logging**: Be aware of what's logged and where
    - **Intellectual Property**: Understand IP implications

    **Check with your IT security team before using Claude Code with:**
    - Proprietary code
    - Sensitive research data
    - Personal information (PII)
    - Protected health information (PHI)
    - Financial data
    - Any classified information

#### Security Checklist

Before deploying AI-assisted code:

- [ ] No hardcoded credentials
- [ ] Environment variables used properly
- [ ] `.gitignore` includes sensitive files
- [ ] No secrets in git history
- [ ] Input validation on all user input
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection implemented
- [ ] Authentication tested thoroughly
- [ ] Authorization checks in place
- [ ] Encryption for sensitive data
- [ ] Secure communication (HTTPS)
- [ ] Security review completed
- [ ] Compliance requirements met

**Ask Claude to Help:**

```bash
You: @security-auditor Review my authentication system for vulnerabilities

Security Auditor: [Comprehensive security analysis]
```

!!! warning "AI-Generated Code Requires Review"
    Always review AI-generated code for security issues. AI can make mistakes or suggest insecure patterns. Your judgment is essential.

---

## 9. AI Sandbox Environments

For certain use cases, you may want to run Claude Code in an isolated sandbox environment.

### 9.1 Why Use Sandboxes?

**Isolation Benefits:**
- Separate development from production environment
- Prevent accidental changes to main system
- Test destructive operations safely
- Maintain clean, reproducible environments

**Testing Environments:**
- Test installations and configurations
- Experiment with different setups
- Verify cross-platform compatibility
- CI/CD integration

**Team Collaboration:**
- Consistent environment across team
- Share exact development setup
- Onboard new developers quickly
- Document infrastructure as code

**Security & Compliance:**
- Meet institutional security requirements
- Isolate sensitive data processing
- Audit and monitor activity
- Enforce security policies

### 9.2 Options Overview

#### Docker Containers

**What**: Lightweight, isolated containers that package applications with their dependencies.

**Pros**:
- Fast startup
- Minimal resource usage
- Easy to share (Dockerfile)
- Perfect for CI/CD
- Version controlled environments

**Cons**:
- Requires Docker knowledge
- Linux-only containers (mostly)
- Networking can be complex

**Learn More**: [Docker Documentation](https://docs.docker.com){target=_blank}

#### Virtual Machines

**What**: Complete OS instances running on your hardware.

**Pros**:
- Complete isolation
- Run different OS (Windows on Mac, etc.)
- Snapshots and restore
- Better for GUI applications

**Cons**:
- Resource-intensive
- Slower startup
- Large disk usage
- More complex setup

**Popular Options**:
- [VirtualBox](https://www.virtualbox.org){target=_blank} (Free, open-source)
- VMware Workstation/Fusion
- Parallels (Mac)
- Hyper-V (Windows)

#### Jupyter Lab Integration

**What**: Run Claude Code within Jupyter Lab for notebook-based development.

**Pros**:
- Interactive development
- Great for data science
- Inline documentation
- Shareable notebooks

**Cons**:
- Different workflow than traditional coding
- Less suitable for large applications

**Learn More**: See our [Jupyter AI Guide](jupyter.md) for detailed setup.

#### Cloud Development Environments

**GitHub Codespaces**
- Cloud-based VS Code
- Integrated with GitHub repos
- Automatic environment setup
- [Learn more](https://github.com/features/codespaces){target=_blank}

**GitPod**
- Open-source alternative to Codespaces
- Works with GitHub, GitLab, Bitbucket
- Free tier available
- [Learn more](https://www.gitpod.io){target=_blank}

**AWS Cloud9**
- AWS-integrated IDE
- Serverless friendly
- Pre-configured for AWS services
- [Learn more](https://aws.amazon.com/cloud9/){target=_blank}

**Replit**
- Browser-based IDE
- Instant setup
- Collaborative coding
- [Learn more](https://replit.com){target=_blank}

### 9.3 Quick Docker Setup Example

Here's a basic Docker setup for Claude Code development:

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

# Install Node.js for Claude Code CLI
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Claude Code
RUN npm install -g @anthropic-ai/claude-code

# Install GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
    dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
    tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && \
    apt-get install gh -y

# Set up workspace
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
```

**Usage:**

```bash
# Build the image
docker build -t claude-dev .

# Run container with volume mount
docker run -it \
  -v $(pwd):/workspace \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  claude-dev

# Inside container
claude-code --version
gh auth login
cd /workspace
claude-code
```

For comprehensive Docker guides, see the [official Docker documentation](https://docs.docker.com){target=_blank}.

---

## 10. Troubleshooting

Common issues and their solutions.

### Installation Problems

**Issue**: `npm install -g @anthropic-ai/claude-code` fails

**Solutions**:

1. **Check Node/npm versions:**
   ```bash
   node --version  # Should be v16+
   npm --version   # Should be v7+
   ```

2. **Update Node:**
   ```bash
   # macOS
   brew upgrade node

   # Or use nvm
   nvm install --lts
   ```

3. **Try without global:**
   ```bash
   npx @anthropic-ai/claude-code --version
   ```

4. **Permissions issue:**
   ```bash
   # Use correct npm permissions (don't use sudo!)
   mkdir ~/.npm-global
   npm config set prefix '~/.npm-global'
   echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc
   ```

**Issue**: VS Code extension not appearing

**Solutions**:

1. **Reload VS Code:**
   - `Cmd/Ctrl + Shift + P` → "Developer: Reload Window"

2. **Check VS Code version:**
   - Must be v1.75.0 or later
   - Help → About

3. **Reinstall extension:**
   ```bash
   code --uninstall-extension anthropic.claude-code
   code --install-extension anthropic.claude-code
   ```

### Authentication Errors

**Issue**: "Authentication failed" or "Invalid API key"

**Solutions**:

1. **Verify API key:**
   ```bash
   echo $ANTHROPIC_API_KEY  # Should output your key
   ```

2. **Re-authenticate:**
   ```bash
   # CLI
   claude-code auth logout
   claude-code auth login

   # Check status
   claude-code auth status
   ```

3. **Check API key format:**
   - Should start with `sk-ant-`
   - No extra spaces or quotes
   - Not expired or revoked

4. **Environment variable:**
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export ANTHROPIC_API_KEY="your-key-here"
   source ~/.bashrc
   ```

**Issue**: "Rate limit exceeded"

**Solution**:
- You've hit usage limits
- Wait and try again
- Upgrade to Pro plan for higher limits
- Check [console.anthropic.com](https://console.anthropic.com){target=_blank} for usage

### Extension Not Loading

**Issue**: VS Code extension installed but not working

**Solutions**:

1. **Check extension status:**
   - View → Extensions
   - Search "Claude Code"
   - Should show "Enabled"

2. **Check for conflicts:**
   - Disable other AI coding extensions
   - Restart VS Code

3. **View logs:**
   - Help → Toggle Developer Tools
   - Console tab → filter for "claude"
   - Look for error messages

4. **Reinstall clean:**
   ```bash
   # Remove extension completely
   rm -rf ~/.vscode/extensions/anthropic.claude-code-*

   # Reinstall
   code --install-extension anthropic.claude-code
   ```

### Performance Issues

**Issue**: Claude Code is slow or unresponsive

**Solutions**:

1. **Reduce context:**
   ```bash
   You: /clear
   You: Let's focus only on the files we need
   ```

2. **Use faster model:**
   ```bash
   You: /model claude-4-5-haiku-20260115
   ```

3. **Close unnecessary files (VS Code):**
   - Close tabs you're not editing
   - Use `.claudeignore` to exclude files

4. **Check network:**
   ```bash
   ping console.anthropic.com
   ```

5. **System resources:**
   - Close other applications
   - Check RAM and CPU usage
   - Restart VS Code/terminal

### Context Window Limits

**Issue**: "Context window exceeded" error

**Solutions**:

1. **Clear conversation:**
   ```bash
   You: /clear
   ```

2. **Focus on specific files:**
   ```bash
   You: Let's work only with src/auth.py for now
   ```

3. **Create `.claudeignore`:**
   ```bash
   # .claudeignore (like .gitignore)
   node_modules/
   dist/
   build/
   *.log
   *.min.js
   vendor/
   .git/
   ```

4. **Split large files:**
   - Refactor large files into smaller modules
   - Use more focused conversations

5. **Use summaries:**
   ```bash
   You: Give me a summary of the auth module instead of showing all the code
   ```

### Common Error Messages

**"Cannot read properties of undefined"**
- Usually a configuration issue
- Check `.claude/config.json` syntax
- Reset config: `rm -rf .claude/` and reinitialize

**"EACCES: permission denied"**
- File permission issue
- Check file ownership: `ls -la`
- Fix permissions: `chmod +x script.sh`

**"Git not found"**
- Git not installed or not in PATH
- Install Git: [git-scm.com](https://git-scm.com){target=_blank}
- Check PATH: `echo $PATH`

### Getting Help

If you're still stuck:

1. **Check official documentation:**
   - [docs.anthropic.com/claude-code](https://docs.anthropic.com/en/docs/claude-code){target=_blank}

2. **Search GitHub issues:**
   - Known issues and solutions
   - Report new bugs

3. **Community resources:**
   - [Anthropic Discord](https://discord.gg/anthropic){target=_blank}
   - Stack Overflow (tag: claude-code)
   - Reddit r/ClaudeAI

4. **Contact support:**
   - Pro/Team subscribers: support@anthropic.com
   - Include: Claude Code version, OS, error messages, steps to reproduce

---

## 11. Tips & Advanced Techniques

### Productivity Tips

**Keyboard Shortcuts (VS Code Extension)**

| Shortcut | Action |
|----------|--------|
| `Cmd/Ctrl + Shift + C` | Open Claude Code panel |
| `Cmd/Ctrl + K` | Quick ask Claude |
| `Cmd/Ctrl + Shift + P` → "Claude" | All Claude commands |
| `Esc` | Cancel current request |
| `Tab` | Accept inline suggestion |

**Efficient Prompting**

✅ **Be Specific:**
```
Refactor the authenticate_user function in src/auth.py to handle OAuth2 tokens
```

❌ **Too Vague:**
```
Make auth better
```

✅ **Provide Context:**
```
This is a Flask app using SQLAlchemy. I need to add a user profile endpoint
that returns user info as JSON. It should require authentication and handle
missing users gracefully.
```

❌ **Lacking Context:**
```
Add a user profile endpoint
```

✅ **Iterative Refinement:**
```
1. Create the basic endpoint
2. [After review] Add pagination support
3. [After review] Add filtering by date
```

❌ **Everything at Once:**
```
Create a user profile endpoint with pagination, filtering, sorting, search,
export to CSV, and admin overrides
```

**Project Organization**

Create a `.claude/` directory for Claude-specific files:

```
.claude/
├── agents/              # Custom agents
│   ├── docs-writer.yaml
│   ├── test-writer.yaml
│   └── reviewer.yaml
├── commands/            # Slash commands
│   ├── commit.yaml
│   ├── test.yaml
│   └── deploy.yaml
├── config.json          # Claude Code settings
├── context/             # Pre-loaded context
│   └── architecture.md
└── prompts/             # Saved prompts
    └── code-review.md
```

**Using the Projects Feature**

Organize work by project:

```bash
# CLI
claude-code project create my-app
claude-code project switch my-app

# Each project maintains separate:
# - Conversation history
# - Context
# - Agent configurations
# - Settings
```

In VS Code: Use workspaces to separate projects.

### Advanced Workflows

#### Multi-File Editing

Ask Claude to make coordinated changes:

```bash
You: Rename the User class to Account across the entire codebase,
including imports, tests, and documentation. Make sure everything
still works.
```

Claude will:
1. Find all occurrences
2. Show proposed changes
3. Apply consistently
4. Update related code
5. Fix broken imports

#### Refactoring Large Codebases

For major refactors:

```bash
You: I want to refactor our monolithic app into microservices.
Let's start by analyzing the current structure and identifying
service boundaries.
```

Then iteratively:
```bash
1. Identify services
2. Define interfaces
3. Extract first service
4. Test integration
5. Repeat for each service
```

#### Integration with CI/CD

Add Claude Code to your CI pipeline:

**.github/workflows/claude-review.yml:**

```yaml
name: Claude Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude-code review \
            --files $(git diff --name-only origin/main) \
            --output review.md

      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: review
            });
```

#### Team Collaboration Patterns

**Shared Agent Library:**

Create team-wide agents in a shared repository:

```
company-claude-agents/
├── agents/
│   ├── python-tester.yaml
│   ├── api-docs.yaml
│   └── security-audit.yaml
└── commands/
    ├── deploy-staging.yaml
    └── create-release.yaml
```

Team members clone and symlink:

```bash
git clone git@github.com:company/claude-agents.git ~/.claude-agents
ln -s ~/.claude-agents/agents .claude/agents
ln -s ~/.claude-agents/commands .claude/commands
```

**Code Review Guidelines:**

Establish team standards for AI-assisted development:

```markdown
## Team Guidelines for Claude Code

### Required Reviews
- All AI-generated code must be reviewed by a human
- Security-sensitive code requires additional security review
- Database migrations require team lead approval

### Documentation
- Add "Generated with Claude Code" to commit messages for AI-generated code
- Document significant AI assistance in PR descriptions
- Explain any non-obvious AI suggestions

### Testing
- All AI-generated code must have tests
- Tests should be human-written or thoroughly reviewed
- Aim for 80%+ coverage on new code

### Security
- Never commit API keys or secrets
- Run security scanners on AI-generated code
- Review authentication/authorization logic manually
```

---

## 12. Next Steps & Resources

Congratulations! You now have a comprehensive understanding of Claude Code and how to use it effectively in your development workflow.

### Related Documentation

Explore these related topics to deepen your understanding:

**[:material-cursor-default-click: Vibe Coding](vibe.md)**
- Compare Claude Code with other AI coding tools
- Understand the vibe coding landscape
- Choose the right tool for different scenarios
- Security considerations for AI-assisted development

**[:simple-anthropic: Model Context Protocol (MCP)](mcp.md)**
- Connect Claude Code to databases, APIs, and external services
- Set up MCP servers for enhanced capabilities
- Build custom integrations
- Leverage context-aware assistance

**[:material-robot: Agentic AI](agentic.md)**
- Understand the principles behind agentic systems
- Learn about autonomous AI behaviors
- Explore advanced agent patterns
- See how agents transform software development

**[:material-code-braces: Code Interpreters](code.md)**
- Understand code execution fundamentals
- Compare sandboxed vs local execution
- Security and privacy considerations
- Best practices for AI-generated code

**[:simple-jupyter: Jupyter AI](jupyter.md)**
- Integrate Claude with Jupyter notebooks
- Data science workflows with AI assistance
- Interactive development patterns
- Research and analysis use cases

### Official Resources

**Documentation:**
- [Anthropic Documentation](https://docs.anthropic.com){target=_blank}
- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/claude-code){target=_blank}
- [API Reference](https://docs.anthropic.com/en/api){target=_blank}
- [Model Context Protocol](https://modelcontextprotocol.io){target=_blank}

**Community:**
- [Anthropic Discord](https://discord.gg/anthropic){target=_blank} - Active community, get help, share projects
- [GitHub Discussions](https://github.com/anthropics/anthropic-sdk-python/discussions){target=_blank} - Technical discussions
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook){target=_blank} - Code examples and tutorials

**Social Media:**
- [@AnthropicAI on Twitter](https://twitter.com/AnthropicAI){target=_blank}
- [Anthropic Blog](https://www.anthropic.com/news){target=_blank}
- [Research Papers](https://www.anthropic.com/research){target=_blank}

### Example Projects

Check out these example projects to see Claude Code in action:

- [Claude Code Starter Templates](https://github.com/anthropics/claude-code-starters){target=_blank}
- [Anthropic Cookbook Examples](https://github.com/anthropics/anthropic-cookbook){target=_blank}
- [Community Projects Showcase](https://discord.gg/anthropic){target=_blank} (Discord #showcase channel)

### Continuing Your Learning Journey

**Week 1-2: Foundation**
- Complete this tutorial's exercises
- Create a simple project with Claude Code
- Practice using agents and slash commands
- Join the Discord community

**Week 3-4: Intermediate**
- Contribute to an open-source project using Claude Code
- Create custom agents for your workflow
- Set up MCP servers for your tools
- Explore integration with CI/CD

**Month 2: Advanced**
- Build a complex multi-service application
- Create team-shared agent libraries
- Develop custom MCP servers
- Contribute back to the community

**Ongoing:**
- Follow Anthropic's blog for updates
- Experiment with new Claude models
- Share your experiences and learnings
- Help others in the community

### Stay Updated

Claude Code and AI development tools evolve rapidly:

- Subscribe to [Anthropic Newsletter](https://www.anthropic.com){target=_blank}
- Watch for Claude Code release notes
- Follow the #claude-code channel on Discord
- Check this documentation for updates

### Getting Involved

**Share Your Experience:**
- Write blog posts about your Claude Code workflow
- Create video tutorials
- Share agents and commands on GitHub
- Help others on Discord

**Provide Feedback:**
- Report bugs and issues
- Suggest new features
- Share use cases and success stories
- Contribute to documentation

**Build Extensions:**
- Create MCP servers for popular tools
- Develop Claude Code plugins
- Share agent configurations
- Build integrations with other tools

### Thank You!

Thank you for completing this comprehensive Claude Code tutorial. We hope this guide helps you unlock the full potential of AI-assisted development. Happy coding! 🚀

---

## 13. Assessment

Test your understanding of Claude Code concepts with these questions:

??? question "What's the primary difference between Claude Code CLI and the VS Code Extension?"

    ??? success "Answer"
        **Claude Code CLI** is a terminal-based tool accessed via command line, best for terminal-first developers and automation workflows. The **VS Code Extension** integrates directly into VS Code with a visual interface, inline editing, and GUI features, making it better for developers who prefer visual development environments. Both have access to the same Claude models and capabilities, just different interfaces.

??? question "When should you use `/init` vs starting a planning session?"

    ??? success "Answer"
        Use **`/init`** when you have an **existing codebase** and want Claude to analyze and understand the current structure, technologies, patterns, and architecture.

        Use a **planning session** when **starting from scratch** or with a minimal repository, where you want Claude to help design the project structure, choose technologies, and plan the implementation.

??? question "What is a custom agent in Claude Code?"

    ??? success "Answer"
        A **custom agent** is a specialized AI assistant configured with specific instructions, knowledge, and behaviors for particular tasks. Agents differ from regular conversations by having:
        - Pre-defined domain expertise
        - Consistent behavior patterns
        - Reusable configurations
        - Specialized skills and instructions

        Examples include documentation writers, code reviewers, test generators, and security auditors.

??? question "True or False: You should commit your `.env` file containing API keys to git for your team to access."

    ??? failure "False"
        **Never commit API keys or secrets to version control!** API keys should be:
        - Stored in `.env` files that are added to `.gitignore`
        - Passed via environment variables
        - Stored securely using secret management tools
        - Shared with team members through secure channels (not git)

        Committing secrets to git exposes them to anyone with repository access and makes them nearly impossible to fully remove from git history.

??? question "Which slash command would you use to stage changes and create a commit with an AI-generated message?"

    1. `/init`
    2. `/commit`
    3. `/review`
    4. `/deploy`

    ??? success "Correct Answer: 2"
        **`/commit`** is the slash command that stages changes, generates an intelligent commit message based on the diff, and creates the commit. The `/init` command analyzes codebases, `/review` performs code reviews, and `/deploy` handles deployment workflows.

??? question "What is the Model Context Protocol (MCP) used for in Claude Code?"

    ??? success "Answer"
        **Model Context Protocol (MCP)** is a standardized communication framework that allows Claude Code to:
        - Access local file systems and databases
        - Interact with external APIs and services
        - Connect to tools like GitHub, PostgreSQL, Slack, etc.
        - Provide real-time application state awareness
        - Enable deep integration with development tools

        MCP enables Claude Code to go beyond conversation and actually interact with your development environment. See our [MCP Documentation](mcp.md) for more details.

??? question "True or False: All code generated by Claude Code is guaranteed to be secure and bug-free."

    ??? failure "False"
        **AI-generated code requires careful human review.** While Claude Code is sophisticated, it can:
        - Make mistakes or misunderstand requirements
        - Suggest outdated or insecure patterns
        - Miss edge cases or error conditions
        - Replicate biases from training data

        Always:
        - Review all AI-generated code
        - Run comprehensive tests
        - Check for security vulnerabilities
        - Verify against best practices
        - Use your judgment and expertise

??? question "Which of the following is a best practice when working with Claude Code?"

    1. Share all your production database credentials in prompts for better debugging
    2. Commit all generated code immediately without review
    3. Use specific, contextual prompts and iterate on solutions
    4. Try to include your entire codebase in every conversation

    ??? success "Correct Answer: 3"
        **Using specific, contextual prompts and iterating on solutions** is the correct best practice. The other options are problematic:
        - Never share sensitive credentials in prompts (security risk)
        - Always review AI-generated code before committing
        - Focus conversations on relevant files to avoid context limits

        Effective Claude Code usage involves clear communication, incremental development, and maintaining security awareness.
