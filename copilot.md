---
type: Setup Guide
title: GitHub Copilot
description: >-
  Set up GitHub Copilot in VS Code and other editors: September 2026 plans
  from Free to Max, AI Credits billing, and free access for students and
  teachers.
resource: https://tyson-swetnam.github.io/intro-gpt/copilot/
tags: [setup, github, microsoft, coding, pricing]
sources:
  - resource: https://github.com/features/copilot/plans
    title: GitHub Copilot plans
  - resource: https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot
    title: Subscription plans for GitHub Copilot
  - resource: https://github.com/education/students
    title: GitHub Education for students
  - resource: https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer
    title: Getting free access to Copilot Pro as a student, teacher, or maintainer
  - resource: https://github.blog/changelog/2026-06-17-copilot-individual-plan-sign-ups-are-reopening/
    title: Copilot individual plan sign-ups are reopening
generated:
  by: human:tswetnam
  at: "2026-09-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2025-01-02T13:30:25-07:00"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# :octicons-copilot-48: GitHub Copilot

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

[GitHub Copilot](https://github.com/features/copilot){target=_blank} is GitHub's AI coding assistant. It began as autocomplete for code and has grown into a family of tools: chat, an agent that edits your project inside the editor, a cloud agent that works on GitHub issues while you do something else, a command-line tool, and automated code review. This page covers what it does as of September 2026, what the plans cost, how students and educators get it free, and how to install it. It is a separate product from the Microsoft 365 Copilot described in the [Microsoft Copilot guide](microsoft.md).

## What GitHub Copilot does now

- **Inline completions** - ghost-text suggestions as you type, from a single line to a whole function. Completions never consume AI credits on any plan.
- **Copilot Chat** - ask questions about your code, explain errors, and generate tests in a side panel or inline in the editor.
- **Agent mode in the IDE** - hand Copilot a task and it plans, edits multiple files, runs commands and tests, and iterates until done, asking your approval along the way.
- **Copilot cloud agent** (formerly "Copilot coding agent") - assign a GitHub issue to Copilot and it researches, plans, and codes in a cloud workspace, then opens a pull request for you to review. Pro plans and above.
- **Copilot CLI** - the same assistant in your terminal for shell commands, scripts, and repository tasks.
- **Copilot code review** - automated review comments on pull requests. Pro plans and above; consumes credits.
- **Model choice** - paid plans let you pick among models from OpenAI, Anthropic (Claude), and Google (Gemini). The Free and Student plans use automatic model selection.

## Plans (September 2026)

| Plan | Price | Notes |
|------|-------|-------|
| **Free** | $0 | 2,000 completions/mo, limited chat and agent-mode usage, automatic model selection |
| **Pro** | $10/mo | 1,500 AI credits/mo (about $15 of usage); cloud agent and code review; no Claude Opus models |
| **Pro+** | $39/mo | 7,000 AI credits/mo (about $70); Claude Opus models |
| **Max** | $100/mo | 20,000 AI credits/mo (about $200); priority access |
| **Business** | $19/user/mo | 1,900 credits per user; organisation-managed seats and policies |
| **Enterprise** | $39/user/mo | 3,900 credits per user; organisation-managed seats and policies |
| **Student** | $0 | Verified students through GitHub Education; automatic model selection |
| **Teachers and open-source maintainers** | $0 | Complimentary Copilot Pro through GitHub Education or the maintainer programme |

!!! warning "Billing and sign-ups (September 2026)"

    - Since **June 1, 2026**, usage on paid plans is metered in **GitHub AI Credits**: 1 credit = $0.01, spent per request at each model's rate. Code completions never consume credits. Once a month's credits are used up, further usage is billed per token at model rates.
    - New individual sign-ups (Student, Pro, Pro+) were **paused on April 20, 2026** and **reopened gradually from June 17, 2026**, when the Max plan also opened. If a sign-up page still shows a waitlist, check back later; the Free plan stayed open throughout.
    - **Claude Opus** models are available on Pro+ and above only (they were removed from Pro on April 20, 2026).

Full details are on the [Copilot plans page](https://github.com/features/copilot/plans){target=_blank} and in the [subscription plans documentation](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot){target=_blank}. To compare with other coding tools, see [Choosing the Right AI Platform](choose.md).

## Free access for students and educators

1. Create a [GitHub account](https://github.com/signup){target=_blank} if you do not have one, and add your school email address to it (**Settings** > **Emails**).
2. Go to [education.github.com](https://education.github.com/){target=_blank} and apply: students choose the **Student** benefits, faculty and staff choose **Teacher**.
3. Verify your status with your school email address, or upload a dated student ID, transcript, or enrolment letter if your school is not recognised automatically.
4. Approval usually takes a few days. Once approved, the **GitHub Copilot Student** plan (students) or complimentary **Copilot Pro** (teachers) appears on your account; see [Getting free access to Copilot Pro as a student, teacher, or maintainer](https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer){target=_blank}. Maintainers of popular open-source projects qualify through the same page.
5. GitHub Education also unlocks the [Student Developer Pack](https://education.github.com/pack){target=_blank}, [Codespaces](https://github.com/codespaces){target=_blank} hours, and [GitHub Classroom](https://classroom.github.com/){target=_blank} for instructors.

Institutions can join the [GitHub Campus Program](https://education.github.com/schools){target=_blank}, which gives the whole school GitHub Enterprise and streamlines student verification; check with your campus IT to find out whether yours participates. UNM users: see [CARC](https://carc.unm.edu/){target=_blank}.

## Install

=== "VS Code"

    1. Install [Visual Studio Code](https://code.visualstudio.com/){target=_blank} (see the [VS Code guide](vscode.md) for platform-specific steps).
    2. Press ++ctrl+shift+x++ (Windows/Linux) or ++cmd+shift+x++ (macOS) to open the Extensions view.
    3. Search for **GitHub Copilot** and click **Install** on the official GitHub extension. Copilot Chat is installed alongside it.
    4. Click the Copilot icon in the status bar (or the Accounts icon in the Activity Bar) and **Sign in to GitHub**; approve the authorisation in your browser.
    5. Back in VS Code, the status-bar icon turns solid when Copilot is active.

=== "JetBrains IDEs"

    1. Open **Settings** > **Plugins** in IntelliJ IDEA, PyCharm, WebStorm, or another [JetBrains IDE](https://www.jetbrains.com/){target=_blank}.
    2. Search the Marketplace for **GitHub Copilot** and install it; restart the IDE when prompted.
    3. Choose **Tools** > **GitHub Copilot** > **Login to GitHub** and complete the device-code sign-in in your browser.

=== "Visual Studio"

    1. Recent versions of [Visual Studio](https://visualstudio.microsoft.com/){target=_blank} 2022 ship with GitHub Copilot as a built-in component; if it is missing, open the Visual Studio Installer, click **Modify**, and add the **GitHub Copilot** component.
    2. In Visual Studio, click the Copilot badge in the top-right corner and sign in with your GitHub account.

=== "Neovim"

    1. Install the [copilot.vim](https://github.com/github/copilot.vim){target=_blank} plugin with your plugin manager (it requires Node.js and [Neovim](https://neovim.io/){target=_blank} 0.6 or later).
    2. Run `:Copilot setup` and follow the device-code sign-in in your browser.
    3. Run `:Copilot enable`; suggestions appear as virtual text and are accepted with ++tab++.

=== "Copilot CLI"

    1. Install the standalone Copilot CLI from [github.com/github/copilot-cli](https://github.com/github/copilot-cli){target=_blank}, or add the older `gh copilot` extension to the [GitHub CLI](https://cli.github.com/){target=_blank} with `gh extension install github/gh-copilot`.
    2. Run `copilot` (or `gh copilot`) in a terminal and sign in with your GitHub account when prompted.
    3. Ask it to explain a command, write a script, or work on the repository in the current directory.

=== "GitHub Copilot app"

    A standalone GitHub Copilot app has been available to all Copilot users since July 2026 `(verify)`. Look for the download link on the [Copilot product page](https://github.com/features/copilot){target=_blank} and sign in with the same GitHub account.

## First use

- **Completions:** open a code file, start typing, or write a comment that describes what you want (`# read a CSV and plot the first two columns`). Ghost text appears; press ++tab++ to accept it or keep typing to ignore it. Press ++alt+bracket-right++ (Windows/Linux) or ++option+bracket-right++ (macOS) to cycle through alternative suggestions.
- **Chat:** press ++ctrl+alt+i++ (Windows/Linux) or ++ctrl+cmd+i++ (macOS) in VS Code to open the Chat view, or ++ctrl+i++ / ++cmd+i++ for inline chat on selected code. Ask it to explain a function, write tests, or fix an error message you paste in.
- **Agent mode:** in the Chat view, switch the mode selector from **Ask** to **Agent**, describe a task ("add a command-line flag for the output directory and update the README"), and review each file edit and terminal command before accepting it.

For how Copilot compares with Claude Code, Cline, and other editor assistants, see the [VS Code and AI-Powered Development guide](vscode.md); for a broader look at agent-driven programming, see [Vibe Coding](vibe.md).
