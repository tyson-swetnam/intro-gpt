---
type: Setup Guide
title: Google Gemini
description: >-
  Access Google Gemini via the web app, AI Studio, and Android, with
  September 2026 pricing, the free year of AI Pro for US college students,
  and API key setup.
resource: https://tyson-swetnam.github.io/intro-gpt/gemini/
tags: [setup, google, pricing]
sources:
  - resource: https://gemini.google.com/
    title: Gemini web app
  - resource: https://aistudio.google.com
    title: Google AI Studio
  - resource: https://notebook.google.com/
    title: Gemini Notebook (formerly NotebookLM)
  - resource: https://support.google.com/gemini/answer/14525875
    title: Gemini availability
  - resource: https://gemini.google/subscriptions/
    title: Gemini subscription plans
  - resource: https://ai.google.dev/gemini-api/docs/pricing
    title: Gemini API pricing
  - resource: https://gemini.google/students/
    title: Google AI Pro student offer
  - resource: https://edu.google.com/intl/ALL_us/ai/gemini-for-education/
    title: Gemini for Education
generated:
  by: human:tswetnam
  at: "2026-09-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2026-05-09T19:43:45Z"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# :simple-googlegemini: Google Gemini

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Creating a Gemini account

There are multiple ways to access and use Google Gemini:

**1. Through the Gemini Web Application:**

   *   Visit [gemini.google.com](https://gemini.google.com/){target=_blank}.
   *   Sign in with your Google Account. If you don't have one, create one at [accounts.google.com](https://accounts.google.com/){target=_blank}.
   *   You can start interacting with Gemini through the chat interface. The free tier includes Gemini Flash (unlimited) and limited Gemini Pro access.

!!! Info "Gemini Pricing & Comparisons (as of September 2026)"
    **Subscription Options:**

    - **Free:** Gemini app with Gemini Flash, limited Gemini Pro access, Deep Research, Gemini Live, Canvas, and 15 GB of storage
    - **AI Plus ($4.99/mo):** cut from $7.99 on June 8, 2026; 2x the Free limits, Gemini Notebook, 400 GB of storage
    - **AI Pro ($19.99/mo):** 4x the Free limits, Gemini 3 Pro and Deep Research, higher Gemini Notebook limits, Jules and Antigravity access, 5 TB of storage - **free for 12 months for US college students 18+: claim at [gemini.google/students](https://gemini.google/students/){target=_blank} between August 19 and December 31, 2026 (SheerID verification; renews at $19.99/mo afterwards). Students outside the US get a year of AI Plus instead.**
    - **AI Ultra ($99.99/mo or $199.99/mo):** 5x or 20x the Pro limits; Deep Think, Gemini Spark, and Project Genie
    - **Gemini for Education:** institutional access that Google Workspace for Education admins turn on (the Gemini app, Gemini Notebook, Gems, and Gemini in Classroom, with data not used to train models) - check with your campus IT. See [Gemini for Education](https://edu.google.com/intl/ALL_us/ai/gemini-for-education/){target=_blank}.

    **Compare with other AI platforms:** See [Choosing the Right AI Platform](choose.md) for detailed comparisons

**2. Through Google AI Studio (for Developers):**

   *   Go to [aistudio.google.com](https://aistudio.google.com){target=_blank}
   *   Sign in with your Google Account.
   *   You can prototype with the Gemini API on a free, rate-limited tier. Prompts and responses on the free tier may be used to improve Google products (outside the EEA, UK, and Switzerland), so never paste sensitive or unpublished data into it.
   *   Paid tier, per 1M tokens (input/output): Gemini 3.8 Flash and 3.7 Flash $0.75/$3.75 through December 31, 2026 ($1.50/$7.50 from January 1, 2027); Gemini 3.5 Flash $1.50/$9.00; 3.5 Flash-Lite $0.30/$2.50; 2.5 Flash $0.30/$2.50; 2.5 Flash-Lite $0.10/$0.40 - see [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing){target=_blank}.

**3. Integrated into Google Products:**

   *   Gemini features are built into Google Workspace, Google Search, Chrome, and other Google products.
   *   [Gemini Notebook (formerly NotebookLM)](notebooklm.md) is a document-based chat interface that lets you load your own sources and hold grounded conversations with them.
   *   [Google Antigravity](https://antigravity.google/){target=_blank} is Google's agentic IDE. Individuals get a free tier with weekly rate limits (Google does not publish the numbers) and there is no standalone paid plan: higher limits come bundled with Google AI Pro and the highest with AI Ultra. The Gemini CLI's free, AI Pro, and AI Ultra access ended on June 18, 2026 and moved to the Antigravity CLI; the open-source Gemini CLI still works with an API key. See the [VS Code guide](vscode.md#google-antigravity).
   *   [Jules](https://jules.google/){target=_blank} is Google's asynchronous coding agent that works on tasks in your GitHub repositories: 15 tasks/day free, 100/day on AI Pro, and 300/day on AI Ultra.

**4. On Android Devices:**

   *   Gemini Nano is available on select Android devices, enabling on-device AI capabilities.

## Troubleshooting Sign-In Issues

If you encounter issues signing in to your Google Account, follow the steps outlined in Google's [support documentation](https://support.google.com/accounts/answer/7682439){target=_blank}.

## Availability

Google Gemini is continuously expanding its availability in [more countries and languages](https://support.google.com/gemini/answer/14525875){target=_blank}.

For institution-managed Google Workspace accounts, Gemini access depends on whether your Google Workspace for Education administrators have enabled it; sign in with your institutional (work or school) account and check with your campus IT if Gemini is missing. UNM users: see [CARC](https://carc.unm.edu/){target=_blank}. Personal Google accounts (`name@gmail.com`) also work.

## What is Gemini?

Gemini is designed to understand and generate text, code, images, audio, and video. 

While Google initially launched Bard as its conversational AI, it has since been rebranded and significantly upgraded as **Gemini**.  The Gemini models are being integrated into various Google products and services, including:

*   [**Google AI Studio:**](https://aistudio.google.com/){target=_blank} A web-based IDE for developers to prototype and build with generative AI models.
*   [**Google Search:**](https://google.com){target=_blank} Enhancing search results with AI-generated summaries and insights.
*   [**Google Workspace:**](https://workspace.google.com/solutions/ai/){target=_blank} AI features to Google Docs, Sheets, Slides, Gmail, and Meet. (Similar to [Microsoft's Copilot](https://copilot.microsoft.com/){target=_blank} integration with Office 365).
*   **Android:** [Gemini Nano](https://deepmind.google/technologies/gemini/nano/){target=_blank} powers on-device AI features in Android devices.

!!! tip "Setting up your Gemini API Key"

    To use the Gemini API in your own applications, you need an API key. Google AI Studio creates one in a few clicks; you do not need to visit the Google Cloud Console first.

    1.  Go to [aistudio.google.com](https://aistudio.google.com/){target=_blank} and sign in with your Google Account.
    2.  Click **"Get API key"**.
    3.  Click **"Create API key"**. A Google Cloud project is created for you automatically (or pick an existing one if you already have projects).
    4.  **Copy the key and store it securely**, for example in a `GOOGLE_API_KEY` environment variable (see [Setting Up API Keys](vscode.md#environment-variables) in the VS Code guide).

    New keys start on the free tier. Attach a billing account to the project later only if you need the paid tier's higher limits. Keep the key confidential and never expose it in client-side code or public repositories.
