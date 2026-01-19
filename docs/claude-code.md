# Claude Code: Setup and Usage Tutorial

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Claude Code

This tutorial will guide you through setting up and using **Claude Code**, Anthropic's AI-powered development tool.

Claude Code acts as a pair programmer that understands context, writes code, creates documentation, and helps you create software faster.

!!! Tip "What You'll Learn"

    This tutorial covers both the Claude Code **CLI** (command-line interface), the **VS Code Extension**, and **Claude Desktop Code** feature. 
    
    We'll highlight the differences and help you choose the right tool for your workflow.

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

??? Question "Are there other CLI :simple-gnubash: Code Assistants?"

    Yes! Claude Code is not the only CLI tool for AI-assisted development. 
    
    Other popular options include:
     
    [**:material-google: Google Gemini CLI**](https://geminicli.com/){:target="_blank"}
    
    [**:fontawesome-brands-openai: ChatGPT Codex**](https://chat.openai.com/codex){:target="_blank"}
    
    [**:simple-opensourceinitiative: OpenCode.ai**](https://opencode.ai){:target="_blank"}
    
    [**:simple-gnubash: aider.chat**](https://aider.chat){:target="_blank"}

---

## 1. What is Claude Code?

**Claude Code** is an AI-powered development assistant built by Anthropic that integrates directly into your development workflow.

Unlike simple code completion tools, Claude Code is an [**agentic AI system**](agentic.md) capable of:

- **Understanding entire codebases** through contextual analysis
- **Writing and editing code** across multiple files simultaneously
- **Running commands** in your terminal to test and verify changes
- **Debugging errors** by analyzing stack traces and suggesting fixes
- **Generating documentation** that stays in sync with your code
- **Creating tests** based on your implementation
- **Refactoring** code while maintaining functionality

Claude Code represents the evolution of AI-assisted development—moving beyond autocomplete to truly collaborative coding experiences often called [**"Vibe Coding"**](vibe.md).

??? Question "CLI vs VS Code Extension: Which Should You Use?"

    Claude Code comes in two primary forms, each suited to different workflows?

    | Feature | Claude Code CLI | Claude Code VS Code Extension |
    |---------|----------------|------------------------------|
    | **Platform** | :simple-gnubash: Terminal/Command Line | :material-microsoft-visual-studio-code: VS Code Editor |
    | **Installation** | :simple-gnubash: `npm install -g @anthropic-ai/claude` | VS Code Extensions Marketplace |
    | **Interface** | Text-based conversations in terminal | Integrated chat panel + inline edits |
    | **File Editing** | Creates/modifies files via CLI commands | Direct in-editor modifications |
    | **Context Awareness** | Full project directory access | VS Code workspace integration |
    | **Terminal Integration** | Native terminal environment | VS Code integrated terminal |
    | **Best For** | Terminal-first developers, automation, CI/CD | VS Code users, visual development, GUI preferences |
    | **Keyboard Shortcuts** | Standard terminal shortcuts | VS Code keybindings + custom shortcuts |
    | **MCP Support** | Yes, via configuration | Yes, via configuration |
    | **Multi-Project** | Switch directories manually | Workspace support |

    !!! Answer "Recommendation: Start with Your Comfort Zone"
        
        If you're primarily a terminal user who lives in vim, emacs, or tmux, start with the **CLI**. 
        
        If you spend most of your time in VS Code, start with the **Extension**. You can always use both!

---

## 2. Prerequisites & Account Setup

### 2.1 Account Options

#### Option 1: Claude.ai

**Claude** (\$20/month), **Claude Pro** (\$100/month), **Claude Pro Max** (\$200/month) 

- Access to Claude Code CLI and VS Code Extension
- Extended usage limits (5x more than free tier)
- Priority access during high-traffic periods
- Access to all Claude models (Sonnet, Opus, Haiku)
- Early access to new features

**Best for**: Individual developers and frequent users

**Sign up**: [claude.ai](https://claude.ai){target=_blank}

#### Option 2: Anthropic API Key

For programmatic access and integration:

- **Sign up**: [console.anthropic.com](https://console.anthropic.com){target=_blank}
- **Pricing**: Pay-per-use based on tokens (see pricing below)
- **API key management**: Generate keys in console dashboard
- **Usage tracking**: Monitor consumption in real-time

**Best for**: Teams, developers who want fine-grained control, batch processing, or integration with other tools

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

### 2.2 System Requirements

#### Operating System

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

**VS Code (or clone)**:

- Visual Studio Code v1.75.0 or later: [code.visualstudio.com](https://code.visualstudio.com){target=_blank}
- Posit Positron: [posit.com](https://posit.com){target=_blank}
- Google Antigravity: [antigravity.google](https://antigravity.google){target=_blank}

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

- CyVerse: [cyverse.org](https://cyverse.org){target=_blank}
- Jetstream-2: [jetstream-cloud.org](https://jetstream-cloud.org){target=_blank}

??? info "When to Use AISandboxes"

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
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```


Expected output:

```
2.1.9 (Claude Code)
```

#### Installation on Windows

**Option 1: Using WSL2 (Recommended)**

Windows Subsystem for Linux provides the best experience:

```bash
# In WSL2 terminal
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

**Option 2: PowerShell/Command Prompt**

```powershell
# In PowerShell or CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
claude --version
```

#### Authentication Setup

After installation, authenticate with your Claude account:

```bash
claude
```

Claude will start with a welcome graphic and ask you to select a color palette

```bash
Welcome to Claude Code v2.1.9                                                                   
…………………………………………………………………………………………………………………………………………………………                                      
                                                                                                
     *                                       █████▓▓░                                           
                                 *         ███▓░     ░░                                         
            ░░░░░░                        ███▓░                                                 
    ░░░   ░░░░░░░░░░                      ███▓░                                                 
   ░░░░░░░░░░░░░░░░░░░    *                ██▓░░      ▓                                         
                                             ░▓▓███▓▓░                                          
 *                                 ░░░░                                                         
                                 ░░░░░░░░                                                       
                               ░░░░░░░░░░░░░░░░                                                 
       █████████                                        *                                       
      ██▄█████▄██                        *                                                      
       █████████      *                                                                         
…………………█ █   █ █………………………………………………………………………………………………………………                                      
                                                                                                
 Let's get started.                                                                             
                                                                                                
 Choose the text style that looks best with your terminal                                       
 To change this later, run /theme                                                               
                                                                                                
 ❯ 1. Dark mode ✔                                                                               
   2. Light mode                                                                                
   3. Dark mode (colorblind-friendly)                                                           
   4. Light mode (colorblind-friendly)                                                          
   5. Dark mode (ANSI colors only)                                                              
   6. Light mode (ANSI colors only)                                                             
                                                                                                
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
 1  function greet() {                                                                          
 2 -  console.log("Hello, World!");                                                             
 2 +  console.log("Hello, Claude!");                                                            
 3  }                                                                                           
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
```

Next, you will need to authenticate in one of two ways:

```bash
Welcome to Claude Code v2.1.9                                                                   
…………………………………………………………………………………………………………………………………………………………                                      
                                                                                                
     *                                       █████▓▓░                                           
                                 *         ███▓░     ░░                                         
            ░░░░░░                        ███▓░                                                 
    ░░░   ░░░░░░░░░░                      ███▓░                                                 
   ░░░░░░░░░░░░░░░░░░░    *                ██▓░░      ▓                                         
                                             ░▓▓███▓▓░                                          
 *                                 ░░░░                                                         
                                 ░░░░░░░░                                                       
                               ░░░░░░░░░░░░░░░░                                                 
       █████████                                        *                                       
      ██▄█████▄██                        *                                                      
       █████████      *                                                                         
…………………█ █   █ █………………………………………………………………………………………………………………                                      
                                                                                                
                                                                                                
 Claude Code can be used with your Claude subscription or billed based on API usage through your
  Console account.                                                                              
                                                                                                
 Select login method:                                                                           
                                                                                                
 ❯ 1. Claude account with subscription · Pro, Max, Team, or Enterprise                          
                                                                                                
   2. Anthropic Console account · API usage billing              
```

This will:

1. Open your browser to authenticate
2. Ask you to authorize Claude Code
3. Save your credentials securely

**For API key users:**

```bash
# Set API key via environment variable
export ANTHROPIC_API_KEY="your-api-key-here"
```

!!! tip "Environment Variables"
    Add to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

    ```bash
    export ANTHROPIC_API_KEY="your-api-key-here"
    ```

    Then reload: `source ~/.zshrc`

#### Basic Configurations

Configure Claude Code preferences using slash commands

In Claude, type the `/model` command:

```bash
 ▐▛███▜▌   Claude Code v2.1.9                                                                   
▝▜█████▛▘  Sonnet 4.5 (1M context) · Claude Max                                                 
  ▘▘ ▝▝    ~/github/intro-gpt                                                                   
                                                                                                
────────────────────────────────────────────────────────────────────────────────────────────────
❯ /model                                                                                        
────────────────────────────────────────────────────────────────────────────────────────────────
  /model                  Set the AI model for Claude Code                                      
  /status                 Show Claude Code status including version, model, account, API conn…  
  /vim                    Toggle between Vim and Normal editing modes                           
  /plan                   Enable plan mode or view the current session plan           
```

Hit :material-keyboard-return: `return` or :material-keyboard-return: `enter` key on your keyboard to enter the new menu

Select a model from the list:

```bash
 ▐▛███▜▌   Claude Code v2.1.9                                                                   
▝▜█████▛▘  Sonnet 4.5 (1M context) · Claude Max                                                 
  ▘▘ ▝▝    ~/github/intro-gpt                                                                   
────────────────────────────────────────────────────────────────────────────────────────────────
 Select model                                                                                   
 Switch between Claude models. Applies to this session and future Claude Code sessions. For     
 other/previous model names, specify with --model.                                              
                                                                                                
   1. Default (recommended)  Opus 4.5 · Most capable for complex work                           
   2. Sonnet                 Sonnet 4.5 · Best for everyday tasks                               
 ❯ 3. Sonnet (1M context) ✔  Sonnet 4.5 with 1M context · Uses rate limits faster               
   4. Haiku                  Haiku 4.5 · Fastest for quick answers    
```

In general, the default `Sonnet 4.5` model should be most useful (both efficient and accurate) for coding tasks.

Use the `Opus 4.5` model when creating complex plans or for analysing a new codebase

Use `Sonnet 4.5 1M` for large projects (this is actually the most expensive model)

Use `Haiku 4.5` for faster outputs that don't require complexity (Haiku is still excellent for writing code, and is the least expensive model).

### 3.2 VS Code Extension

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
code --install-extension anthropic.claude
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

#### Your First Conversational Git Experience

Now that you've installed `gh` CLI and authenticated with GitHub, here's the exciting part: **you don't need to memorize Git commands anymore**. 

Instead of typing manual commands, you can have natural conversations with Claude Code about what you want to accomplish, and Claude handles the Git operations for you.

**The Paradigm Shift:**

Traditional Git requires remembering specific commands, flags, and syntax. 

With Claude Code, you simply describe what you want in plain English, and Claude translates your intent into the appropriate Git operations.

**Traditional Git vs. Conversational Git:**

| **Traditional Workflow** | **Claude Code Conversation** |
|-------------------------|------------------------------|
| `git status`<br>`git add .`<br>`git commit -m "message"`<br>`git push` | **You:** "Commit and push my changes"<br>**Claude:** [Checks status, stages files, creates commit, pushes] |
| `git status`<br>(manually review changes)<br>`git diff file.py` | **You:** "What's the current state of my repository?"<br>**Claude:** [Runs git status, summarizes changes clearly] |
| `git add .`<br>`git commit -m "fix: update config"`<br>(hope the message is good enough) | **You:** "Add all my files and commit with a good message"<br>**Claude:** [Analyzes changes, creates descriptive commit message] |
| `gh pr create --title "..." --body "..."`<br>(write PR description from scratch) | **You:** "Create a pull request"<br>**Claude:** [Analyzes commits, drafts PR with summary and test plan] |

**Essential Conversational Git Patterns:**

Here are realistic dialogues showing how Claude Code handles common Git workflows. Notice how you can ask in natural language, and Claude explains what it's doing:

**Example 1: Checking Repository Status**

**You:** What's the current state of my repository?

**Claude:** Let me check...

[Runs `git status`]

Your repository is on branch `main` and it's up to date with `origin/main`.

You have:
- 3 untracked files: `src/app.py`, `requirements.txt`, and `README.md`
- No staged or unstaged changes to tracked files

Would you like to add these files and commit them?

---

**Alternative natural phrasings:**

- "Check my git status"
- "What files have I changed?"
- "Show me what's in my repo"
- "Did I modify anything?"

---

**Example 2: Adding and Committing Files**

**You:** Add all my files and commit them with a good message

**Claude:** I'll help you commit these changes. Let me check what we're committing...

[Runs `git status`]

I see 3 new files:
- `src/app.py` - A Flask application setup
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

[Runs `git add .`]

[Runs `git commit -m "feat: initial project setup with Flask app

- Add Flask application skeleton
- Add project dependencies
- Add initial documentation"`]

✓ Changes committed! Would you like to push to the remote repository?

---

**Alternative natural phrasings:**
- "Commit my changes"
- "Save all my work to git"
- "Make a commit with a descriptive message"
- "Stage and commit everything"

!!! tip "Claude Analyzes Before Acting"

    Notice how Claude first checks what files are being committed and provides context. This helps you understand what's happening and catch any mistakes before they're committed.

---

**Example 3: Pushing to Remote**

**You:** Push my changes to GitHub

**Claude:** I'll push your commits to the remote repository.

[Runs `git push`]

✓ Successfully pushed to origin/main!

Your changes are now on GitHub at: https://github.com/username/repo

---

**Alternative natural phrasings:**

- "Push to remote"
- "Upload my commits to GitHub"
- "Send my changes to GitHub"
- "Sync with GitHub"

---

**Example 4: Creating a Pull Request**

**You:** Create a pull request for my changes

**Claude:** I'll create a PR for you. Let me analyze your changes...

[Runs `git diff main`]

[Runs `gh pr create --title "feat: Add Flask application" --body "## Summary

- Initial Flask application setup
- Added project dependencies
- Created documentation

---

**Alternative natural phrasings:**

- "Make a PR"
- "Open a pull request"
- "Submit for review"
- "Create PR from my branch"

!!! example "Try It Yourself"

    The best way to learn is by doing. Once you've created your first project in Section 4, come back and try these conversations. You'll be amazed at how natural it feels!

---

**What You Just Experienced:**

With Claude Code, Git operations become conversational:

✓ **Natural language** instead of command memorization
✓ **Context awareness** - Claude understands your project state
✓ **Smart defaults** - Claude writes good commit messages and PR descriptions
✓ **Safety checks** - Claude shows you what it's doing before making changes
✓ **Flexibility** - Ask in whatever way feels natural to you

!!! info "Advanced Git Workflows"

    This section covered the essential Git workflow (status, add, commit, push, PR) that beginners need. For advanced operations like branching strategies, rebasing, stashing, handling merge conflicts, and collaborative workflows, see [Section 8.2: Git Integration Patterns](#82-git-integration-patterns).

---

#### Quick Command Reference

!!! info "Claude Can Run These For You"
    You don't need to memorize or manually type these commands! Claude Code can execute all of these through natural conversation (as shown above). This reference is useful for:

    - **Understanding what Claude does** behind the scenes
    - **Manual use** when Claude Code isn't running
    - **Scripts and automation** that don't need AI assistance

Common `gh` and `git` commands for reference:

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
echo "Claude Code: $(claude --version)"
```

All commands should return version numbers without errors.

!!! success "Installation Complete!"

    You've installed Claude Code, authenticated with GitHub, and learned how conversational Git works. In the next section, we'll create your first project and put these skills into practice!

---

## 4. Creating Your First Project

Now that you have Claude Code set up and understand conversational Git, let's create your first project using natural conversation. No need to memorize `gh` commands—just tell Claude what you want to build!

First, create a new folder in the CLI and change directory into it

```bash
mkdir review-paper
cd review-paper
```

### 4.1 Starting Claude Code

Before activating the local folder as a git repository, let's start Claude Code inside the new empty directory.

#### CLI: Starting a Session

Start Claude Code:

```bash
# Start Claude Code from any directory
claude
```

You'll see Claude Code's interactive prompt:

```
(base) ➜  review-paper claude
                                                                                                
────────────────────────────────────────────────────────────────────────────────────────────────
 Do you trust the files in this folder?                                                         
                                                                                                
 /Users/tswetnam/review-paper                                                                   
                                                                                                
 Claude Code may read, write, or execute files contained in this directory. This can pose       
 security risks, so only use files from trusted sources.                                        
                                                                                                
 Learn more                                                                                     
                                                                                                
 ❯ 1. Yes, proceed                                                                              
   2. No, exit                                                                                  
                                                                                                
 Enter to confirm · Esc to cancel                    
```

Click :material-keyboard-return: `1. Yes, proceed` at this point if you are in the correct folder. 

!!! tip "Pro Tip"

    You can start Claude Code from any directory. 
    
    Claude can navigate the file system, create directories, and set up projects wherever you need them!

### 4.2 Creating a New Repository (Conversational)

Now comes the exciting part: creating your first GitHub repository through conversation with Claude. 

No manual commands needed!

#### Example: Creating a Brand New Project

**You:** 

```bash
❯ set up this folder as a git repository, include all of the common files for a data            
  science project that uses Python  
```

**Claude:** 

```bash

⏺ I'll help you set up this folder as a git repository with common files for a Python data      
  science project. Let me plan this out.                                                        
                                                                                                
⏺ Bash(git init)                                                                                
  ⎿  Running…                                                                                   
                                                                                                
  Todos · ctrl+t to hide todos                                                                  
  ☐ Initialize git repository                                                                   
  ☐ Create Python .gitignore file                                                               
  ☐ Create README.md with project template                                                      
  ☐ Create requirements.txt file                                                                
  ☐ Create standard directory structure                                                         
  ☐ Create initial git commit                                                                   
                                                                                                
────────────────────────────────────────────────────────────────────────────────────────────────
 Bash command                                                                                   
                                                                                                
   git init                                                                                     
   Initialize git repository                                                                    
                                                                                                
 Do you want to proceed?                                                                        
 ❯ 1. Yes                                                                                       
   2. Yes, and don't ask again for git init commands in /Users/tswetnam/review-paper            
   3. No                                                                                        
                                                                                                
 Esc to cancel · Tab to add additional instructions   
```

Say `Yes`

```bash
                                                                                                
⏺ Bash(git init)                                                                                
  ⎿  Initialized empty Git repository in /Users/tswetnam/review-paper/.git/                     
     hint: Using 'master' as the name for the initial branch. This default branch name          
     hint: is subject to change. To configure the initial branch name to use in all             
     … +8 lines (ctrl+o to expand)                                                              
                                                                                                
⏺ Write(.gitignore)                                                                             
  ⎿  Wrote 187 lines to .gitignore                                                              
      1 # Byte-compiled / optimized / DLL files                                                 
      2 __pycache__/                                                                            
      3 *.py[cod]                                                                               
      4 *$py.class                                                                              
      5 # C extensions                                                                          
      6 *.so                                                                                    
      7 # Distribution / packaging                                                              
      8 .Python                                                                                 
     … +177 lines (ctrl+o to expand)                                                            
                                                                                                
⏺ Write(README.md)                                                                              
                                                                                                
  Todos · ctrl+t to hide todos                                                                  
  ☒ Initialize git repository                                                                   
  ☒ Create Python .gitignore file                                                               
  ☐ Create README.md with project template                                                      
  ☐ Create requirements.txt file                                                                
  ☐ Create standard directory structure                                                         
  ☐ Create initial git commit                                                                   
                                                                                                
────────────────────────────────────────────────────────────────────────────────────────────────
 Create file README.md                                                                          
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
   1 # Review Paper                                                                             
   2                                                                                            
   3 ## Project Description                                                                     
   4                                                                                            
   5 A brief description of your review paper project.                                          
   6                                                                                            
   7 ## Project Structure                                                                       
   8                                                                                            
   9 ```                                                                                        
  10 review-paper/                                                                              
  11 ├── data/                                                                                  
  12 │   ├── raw/              # Original, immutable data                                       
  13 │   ├── interim/          # Intermediate transformed data                                  
  14 │   ├── processed/        # Final data sets for modeling                                   
  15 │   └── external/         # Data from third party sources                                  
  16 ├── notebooks/            # Jupyter notebooks for exploration                              
  17 ├── src/                  # Source code for this project                                   
  18 │   ├── __init__.py                                                                        
  19 │   ├── data/            # Scripts to download or generate data                            
  20 │   ├── features/        # Scripts to turn raw data into features                          
  21 │   ├── models/          # Scripts to train models and make predictions                    
  22 │   └── visualization/   # Scripts to create visualizations                                
  23 ├── models/              # Trained and serialized models                                   
  24 ├── reports/             # Generated analysis as HTML, PDF, LaTeX, etc.                    
  25 │   └── figures/         # Generated graphics and figures                                  
  26 ├── tests/               # Unit tests                                                      
  27 ├── requirements.txt     # Python dependencies                                             
  28 ├── .gitignore                                                                             
  29 └── README.md                                                                              
  30 ```                                                                                        
  31                                                                                            
  32 ## Setup                                                                                   
  33                                                                                            
  34 ### Prerequisites                                                                          
  35                                                                                            
  36 - Python 3.8 or higher                                                                     
  37 - pip or conda                                                                             
  38                                                                                            
  39 ### Installation                                                                           
  40                                                                                            
  41 1. Clone this repository                                                                   
  42 ```bash                                                                                    
  43 git clone <repository-url>                                                                 
  44 cd review-paper                                                                            
  45 ```                                                                                        
  46                                                                                            
  47 2. Create a virtual environment                                                            
  48 ```bash                                                                                    
  49 python -m venv venv                                                                        
  50 source venv/bin/activate  # On Windows: venv\Scripts\activate                              
  51 ```                                                                                        
  52                                                                                            
  53 3. Install dependencies                                                                    
  54 ```bash                                                                                    
  55 pip install -r requirements.txt                                                            
  56 ```                                                                                        
  57                                                                                            
  58 ## Usage                                                                                   
  59                                                                                            
  60 Describe how to use your project here.                                                     
  61                                                                                            
  62 ## Data                                                                                    
  63                                                                                            
  64 Describe your data sources and how to obtain them.                                         
  65                                                                                            
  66 ## Results                                                                                 
  67                                                                                            
  68 Summarize key findings and results.                                                        
  69                                                                                            
  70 ## Contributing                                                                            
  71                                                                                            
  72 If this is a collaborative project, describe how others can contribute.                    
  73                                                                                            
  74 ## License                                                                                 
  75                                                                                            
  76 Specify your license here.                                                                 
  77                                                                                            
  78 ## Contact                                                                                 
  79                                                                                            
  80 Your contact information or project maintainer details.                                    
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
 Do you want to create README.md?                                                               
 ❯ 1. Yes                                                                                       
   2. Yes, allow all edits during this session (shift+tab)                                      
   3. No                                                                                        
                                                                                                
 Esc to cancel · Tab to add additional instructions      

```

Continue to accept Claude's questions until the tasks are complete.

!!! tip "Claude Understands Context"

    Notice how Claude:

    - Inferred you wanted a **public** repository (common for learning projects)
    - Automatically added a **Python .gitignore** (you mentioned Python)
    - Added a **license** (good practice for public repos)
    - **Cloned it locally** and navigated into the directory
    - **Asked follow-up questions** to understand next steps

    You can always be more specific: "Create a **private** repo" or "Don't add a license yet"

Claude will continue to execute on the plan until it completes:

```                                                                                    
⏺ Write(.gitignore)                                                                             
  ⎿  Wrote 187 lines to .gitignore                                                              
      1 # Byte-compiled / optimized / DLL files                                                 
      2 __pycache__/                                                                            
      3 *.py[cod]                                                                               
      4 *$py.class                                                                              
      5 # C extensions                                                                          
      6 *.so                                                                                    
      7 # Distribution / packaging                                                              
      8 .Python                                                                                 
     … +177 lines (ctrl+o to expand)                                                            
                                                                                                
⏺ Write(README.md)                                                                              
  ⎿  Wrote 81 lines to README.md                                                                
      1 # Review Paper                                                                          
      2 ## Project Description                                                                  
      3 A brief description of your review paper project.                                       
      4 ## Project Structure                                                                    
      5 ```                                                                                     
      6 review-paper/                                                                           
     … +71 lines (ctrl+o to expand)                                                             
                                                                                                
⏺ Write(requirements.txt)                                                                       
  ⎿  Wrote 35 lines to requirements.txt                                                         
      1 # Core data science libraries                                                           
      2 numpy>=1.24.0                                                                           
      3 pandas>=2.0.0                                                                           
      4 scipy>=1.10.0                                                                           
      5 # Visualization                                                                         
      6 matplotlib>=3.7.0                                                                       
      7 seaborn>=0.12.0                                                                         
      8 plotly>=5.14.0                                                                          
     … +25 lines (ctrl+o to expand)                                                             
                                                                                                
⏺ Bash(mkdir -p data/raw data/interim data/processed data/external notebooks src/data           
      src/features src/models src/visualization models reports/figures tests && touch d…)       
  ⎿  (No content)                                                                               
                                                                                                
⏺ Bash(git add . && git commit -m "Initial commit: Set up Python data science project           
      structure…)                                                                               
  ⎿ [master (root-commit) 0e41ecd] Initial commit: Set up Python data science project struc     
    ture                                                                                        
     14 files changed, 300 insertions(+)                                                        
    … +14 lines (ctrl+o to expand)                                                              
                                                                                                
                                                                                                
⏺ Done! I've successfully set up your folder as a git repository with a complete Python data    
  science project structure. Here's what was created:                                           
                                                                                                
  Core Files:                                                                                   
  - .gitignore - Comprehensive Python and data science exclusions                               
  - README.md - Project template with structure documentation                                   
  - requirements.txt - Common data science libraries (numpy, pandas, scikit-learn, jupyter,     
  matplotlib, etc.)                                                                             
                                                                                                
  Directory Structure:                                                                          
  review-paper/                                                                                 
  ├── data/                                                                                     
  │   ├── raw/              # For original data                                                 
  │   ├── interim/          # For intermediate data                                             
  │   ├── processed/        # For final datasets                                                
  │   └── external/         # For third-party data                                              
  ├── notebooks/            # For Jupyter notebooks                                             
  ├── src/                  # Source code modules                                               
  │   ├── data/                                                                                 
  │   ├── features/                                                                             
  │   ├── models/                                                                               
  │   └── visualization/                                                                        
  ├── models/               # For saved models                                                  
  ├── reports/                                                                                  
  │   └── figures/         # For generated visualizations                                       
  └── tests/               # For unit tests                                                     
                                                                                                
  All changes have been committed to git. You can start working by:                             
  1. Creating a virtual environment: python -m venv venv                                        
  2. Activating it: source venv/bin/activate                                                    
  3. Installing dependencies: pip install -r requirements.txt                                   
                                                                                                
✻ Baked for 1m 32s   
```


!!! success "What You Just Experienced"

    In this conversation, Claude:

    ✓ **Created a complete project structure** from a simple request

    ✓ **Wrote actual code** (Python project with folders)
    
    ✓ **Set up environment** (virtual environment and dependencies)
    
    ✓ **Committed changes** with a well-formatted message
    
    ✓ **Pushed to GitHub** to save your work

    All through natural conversation—no manual commands needed!

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

```bash
You: /init
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
                                                                                                
⏺ I'll analyze the codebase and create a CLAUDE.md file with relevant guidance for future       
  instances.                                                                                    
                                                                                                
⏺ Bash(find . -type f -name "*.py" -o -name "*.ipynb" -o -name "*.md" -o -name "*.txt" -o -name 
      "*.yml" -o -name "*.yaml" -o -name "*.json" | grep -v ".git" | head -20)                  
  ⎿  ./requirements.txt                                                                         
     ./README.md                                                                                
     ./src/visualization/__init__.py                                                            
     … +4 lines (ctrl+o to expand)                                                              
                                                                                                
⏺ Bash(ls -la)                                                                                  
  ⎿  total 24                                                                                   
     drwxr-xr-x@  12 tswetnam  staff   384 Jan 16 15:45 .                                       
     drwxr-xr-x+ 199 tswetnam  staff  6368 Jan 16 15:55 ..                                      
     … +10 lines (ctrl+o to expand)                                                             
                                                                                                
⏺ Read(README.md)                                                                               
  ⎿  Read 81 lines                                                                              
                                                                                                
⏺ Read(requirements.txt)                                                                        
  ⎿  Read 35 lines                                                                              
                                                                                                
⏺ Bash(test -f .cursorrules && cat .cursorrules || test -d .cursor/rules && ls -la .cursor/rules
       || echo "No cursor rules found")                                                         
  ⎿  No cursor rules found                                                                      
                                                                                                
⏺ Bash(test -f .github/copilot-instructions.md && cat .github/copilot-instructions.md || echo   
      "No copilot instructions found")                                                          
  ⎿  No copilot instructions found                                                              
                                                                                                
⏺ Now I'll create the CLAUDE.md file with relevant guidance for this Python data science        
  project.                                                                                      
                                                                                                
⏺ Write(CLAUDE.md)                                                                              
  ⎿  Wrote 103 lines to CLAUDE.md                                                               
      1 # CLAUDE.md                                                                             
      2 This file provides guidance to Claude Code (claude.ai/code) when working with cod       
        e in this repository.                                                                   
      3 ## Project Overview                                                                     
      4 This is a Python data science project for a review paper, following a standard da       
        ta science project structure with separation between raw data, processed data, so       
        urce code, notebooks, and outputs.                                                      
      5 ## Environment Setup                                                                    
     … +93 lines (ctrl+o to expand)                                                             
                                                                                                
⏺ I've created a CLAUDE.md file for this repository. The file includes:                         
                                                                                                
  1. Environment setup commands - How to create a virtual environment and install dependencies  
  2. Testing commands - How to run all tests, tests with coverage, single test files, and       
  specific tests                                                                                
  3. Code quality commands - How to use Black for formatting and flake8 for linting             
  4. Architecture overview - The Cookiecutter Data Science structure pattern with explanations  
  of each directory's purpose                                                                   
  5. Data flow pattern - The intended workflow from raw data through processing to final outputs
  6. Key dependencies - Categorized list of main libraries used                                 
                                                                                                
  The file focuses on the practical commands needed for development and the high-level          
  architectural patterns that aren't immediately obvious from the directory structure alone.    
  Future instances of Claude Code will be able to use this to understand how to work effectively
   in this codebase.                                                                            
                                                                                                
✻ Baked for 55s     
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

```bash
Great! Let's plan this project. Here's what I'm thinking:

**Project Structure:**

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

### 6.2 Built-in Specialized Agents

Claude Code includes several built-in specialized agents that handle common development tasks. These agents are always available and can be invoked using the Task tool or through natural conversation.

**Available Built-in Agents:**

| Agent | Purpose | When to Use | Key Capabilities |
|-------|---------|-------------|------------------|
| **Explore** | Codebase exploration specialist | Finding files, searching code, understanding project structure | Fast pattern matching, keyword search, architectural analysis. Supports thoroughness levels: "quick", "medium", "very thorough" |
| **Plan** | Software architecture and planning | Designing implementation strategies before coding | Creates step-by-step plans, identifies critical files, considers architectural trade-offs |
| **Bash** | Command execution specialist | Git operations, terminal tasks, system commands | Specialized for bash command execution and terminal operations |
| **general-purpose** | Multi-step task automation | Complex research, iterative searching, multi-step workflows | Access to all tools, autonomous task handling, ideal when multiple search attempts needed |
| **claude-code-guide** | Claude documentation expert | Questions about Claude Code, API, or Agent SDK | Specialized knowledge of Claude features, tools, commands, and best practices |
| **webcrawler** | Web content extraction | Documentation research, gathering information from websites | Web fetching, search, content extraction and analysis |
| **statusline-setup** | Configuration assistant | Setting up Claude Code status line | Reads and edits status line configuration |

**How to Invoke Built-in Agents:**

Built-in agents are automatically invoked by Claude when appropriate for your task, but you can also request them explicitly:

```bash
# Examples of natural requests that invoke specific agents:
"Explore the authentication system in this codebase"  # → Explore agent
"Plan out how to implement dark mode"                 # → Plan agent
"How do I configure Claude Code hooks?"               # → claude-code-guide agent
"Search for information about Zensical features"      # → webcrawler agent
```

**Thoroughness Levels for Explore Agent:**

When using the Explore agent, you can specify how thorough the search should be:

- **"quick"**: Basic searches, fastest response
- **"medium"**: Moderate exploration, balanced approach
- **"very thorough"**: Comprehensive analysis across multiple locations and naming conventions

!!! tip "Choosing the Right Agent"
    Claude automatically selects the most appropriate built-in agent for your task. For codebase exploration, the Explore agent is much faster than running search commands directly. For implementation planning, the Plan agent helps you design before you code.

### 6.3 Creating a Documentation Writer Agent

Let's create a practical example: a documentation writer agent that maintains your project's documentation.

#### Conceptual Explanation

A documentation agent should:

- Understand your documentation style and standards
- Know what type of documentation you need (API docs, tutorials, README updates)
- Follow consistent formatting and tone
- Keep documentation in sync with code changes
- Generate examples and usage instructions

#### Step-by-Step Creation Using `/agents`

Claude Code provides the `/agents` slash command to create custom agents interactively. This is the recommended approach as it guides you through the process and generates the configuration file automatically.

**Step 1: Run the `/agents` Command**

In Claude Code chat:

```
/agents
```

This launches the agent creation wizard that will:

1. Ask you to describe the agent's purpose and responsibilities
2. Help you define the agent's instructions and behavior
3. Set up any domain-specific knowledge
4. Create the agent configuration file in `.claude/agents/`
5. Automatically register the agent for use

**Step 2: Describe Your Agent**

When prompted, provide a clear description. For a documentation writer agent:

```
I need a documentation writer agent that:
- Writes clear, concise technical documentation
- Follows Markdown formatting standards
- Includes code examples for all features
- Creates API docs, README updates, and tutorials
- Uses active voice and present tense
- Keeps documentation in sync with code changes
```

**Step 3: Refine Agent Instructions**

The wizard will generate initial instructions and allow you to refine them. You can specify:

- **Documentation standards**: Formatting, style, structure
- **Style guide**: Voice, tense, sentence length
- **Documentation types**: README, API docs, changelogs, etc.
- **Code style preferences**: Language-specific conventions
- **Domain knowledge**: Project-specific information

The wizard creates a configuration file like `.claude/agents/docs-writer.yaml` with content similar to:

```yaml
name: Documentation Writer
description: Technical documentation specialist for this project
version: 1.0.0

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

  STYLE GUIDE:
  - Use second person ("you") for instructions
  - Use present tense for descriptions
  - Keep sentences concise (< 20 words)
  - Use bullet points for lists
  - Include code blocks with syntax highlighting

# Additional configuration generated by the wizard...
```

!!! tip "Manual Creation Alternative"
    While `/agents` is recommended, you can also manually create agent files in `.claude/agents/` if you prefer full control. See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) for the complete YAML schema.

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

### 6.4 Other Useful Agent Ideas

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
claude

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
```

Claude will generate:

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
RUN npm install -g @anthropic-ai/claude

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
claude --version
gh auth login
cd /workspace
claude
```

For comprehensive Docker guides, see the [official Docker documentation](https://docs.docker.com){target=_blank}.

---

## 10. Troubleshooting

Common issues and their solutions.

### Installation Problems

**Issue**: `npm install -g @anthropic-ai/claude` fails

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
   npx @anthropic-ai/claude --version
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
   code --uninstall-extension anthropic.claude
   code --install-extension anthropic.claude
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
   claude auth logout
   claude auth login

   # Check status
   claude auth status
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
   rm -rf ~/.vscode/extensions/anthropic.claude-*

   # Reinstall
   code --install-extension anthropic.claude
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
   - [docs.anthropic.com/claude](https://docs.anthropic.com/en/docs/claude){target=_blank}

2. **Search GitHub issues:**
   - Known issues and solutions
   - Report new bugs

3. **Community resources:**
   - [Anthropic Discord](https://discord.gg/anthropic){target=_blank}
   - Stack Overflow (tag: claude)
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
claude project create my-app
claude project switch my-app

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
        run: npm install -g @anthropic-ai/claude

      - name: Run Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude review \
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
- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/claude){target=_blank}
- [API Reference](https://docs.anthropic.com/en/api){target=_blank}
- [Model Context Protocol](https://modelcontextprotocol.io){target=_blank}

**Community:**

- [Anthropic Discord](https://discord.gg/anthropic){target=_blank} - Active community, get help, share projects
- [GitHub Discussions](https://github.com/anthropics/anthropic-sdk-python/discussions){target=_blank} - Technical discussions
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook){target=_blank} - Code examples and tutorials

**Social Media:**

- [Anthropic Blog](https://www.anthropic.com/news){target=_blank}
- [Research Papers](https://www.anthropic.com/research){target=_blank}

### Example Projects

Check out these example projects to see Claude Code in action:

- [Claude Code Starter Templates](https://github.com/anthropics/claude-starters){target=_blank}
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
- Follow the #claude channel on Discord
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
