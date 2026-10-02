---
type: Setup Guide
title: OpenAI ChatGPT
description: >-
  Set up a ChatGPT account, compare the September 2026 plans from Free and Go
  to the Pro tiers, Business, and Edu, and create OpenAI API keys.
resource: https://tyson-swetnam.github.io/intro-gpt/chatgpt/
tags: [setup, openai, pricing]
sources:
  - resource: https://openai.com/chatgpt/pricing/
    title: ChatGPT pricing
  - resource: https://developers.openai.com/api/docs/pricing
    title: OpenAI API pricing
  - resource: https://platform.openai.com/docs/models
    title: OpenAI models documentation
  - resource: https://platform.openai.com/docs/overview
    title: OpenAI API Documentation
  - resource: https://github.com/openai/openai-cookbook
    title: OpenAI Cookbook
  - resource: https://openai.com/index/chatgpt-for-teachers/
    title: ChatGPT for Teachers
  - resource: https://openai.com/chatgpt/education/
    title: ChatGPT Edu
  - resource: https://prism.openai.com/
    title: OpenAI Prism
generated:
  by: human:tswetnam
  at: "2026-09-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2026-05-10T19:02:57Z"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# :fontawesome-brands-openai: OpenAI ChatGPT

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## About OpenAI and ChatGPT

**OpenAI** is an artificial intelligence research company founded in 2015, known for developing some of the most influential AI models in recent years. Their flagship product, **ChatGPT**, launched in November 2022 and quickly became the fastest-growing consumer application in history.

ChatGPT is powered by a family of large language models (LLMs) spanning flagship multimodal models, cost-efficient variants, and frontier reasoning models. These models can understand and generate human-like text, analyze images, write code, and assist with a wide range of tasks. For the current lineup, see [OpenAI's models page](https://platform.openai.com/docs/models){target=_blank}.

## Creating a ChatGPT Account

**Log In to Your Account**

   - Visit [chatgpt.com](https://chatgpt.com/){target=_blank} and log in using your existing credentials or create a new account.

**Access Account Settings:**

   - Once logged in, look for the sidebar (usually on the left).
   - Click on the **"Upgrade to Plus"** or **"Manage my plan"** button.
     - If you do not see this option, try refreshing the page or updating your browser.

**Initiate Upgrade:**

   - Click **"Upgrade to Plus"** ($20/mo) or one of the Pro tiers ($100, $200, or $500/mo).
   - A pricing page will appear with current subscription options.

!!! Info "Compare ChatGPT with Other AI Platforms"
    For comprehensive pricing comparisons and to see how ChatGPT stacks up against Claude, Gemini, and other AI platforms, visit:

    **[Choosing the Right AI Platform](choose.md)** - Compare features, pricing, and use cases

**Enter Payment Information:**

   - Provide the required billing details.
   - Review the payment terms and confirm your subscription.

**Confirmation and Billing Cycle:**

   - After completing the payment process, you will receive a confirmation email.
   - Your Plus account should be active immediately.
   - You can now enjoy features like priority access, faster response times, and the latest model updates.

## ChatGPT Subscription Plans

!!! info "Pricing tiers, as of September 2026 (check [OpenAI's pricing page](https://openai.com/chatgpt/pricing/){target=_blank} for current rates)"

    **Free Tier ($0)**

    - GPT-5.6 Luna in chat; limited Codex access
    - Standard response speed
    - **Shows ads on US accounts** (rolled out Feb 9, 2026)
    - Good for casual users exploring AI capabilities

    **ChatGPT Go ($8/month)**

    - About 10x the Free usage limits
    - Ads on US accounts

    **ChatGPT Plus ($20/month)**

    - GPT-5.6 Sol in chat; GPT-6 models in the Work and Codex surfaces
    - Full deep research
    - Codex (agentic coding)
    - Image generation, file uploads, voice mode, and data analysis (sandboxed Python)
    - No ads

    **ChatGPT Pro ($100/month)**

    - 5x Plus usage
    - GPT-6 Pro (Astra) in chat

    **ChatGPT Pro ($200/month)**

    - 20x Plus usage
    - New sign-ups were paused Sept 10–29, 2026 and have resumed with lower limits `(verify)`

    **ChatGPT Pro 500 ($500/month)**

    - 25x Plus usage
    - GPT-6 Astra Ultrafast
    - Launched Sept 29, 2026 `(verify)`

    **ChatGPT Business Standard ($25/seat/month, or $20/seat/month annual)**

    - Everything in Plus
    - Admin controls and workspace management
    - Data excluded from training by default
    - Minimum 2 seats

    **ChatGPT Business Premium ($125/seat/month, or $100/seat/month annual)**

    - 5x Business Standard usage

    **ChatGPT Enterprise (Custom pricing)**

    - Unlimited high-speed access to flagship models
    - Enterprise-grade security and compliance
    - Admin console with SSO and domain verification
    - Custom data retention policies
    - Priority support

    **ChatGPT Edu** — an institutional licence bought by the university (no individual student discount); see [openai.com/chatgpt/education](https://openai.com/chatgpt/education/){target=_blank}

    **Education and student offers**

    - **ChatGPT for Teachers:** free for verified US K-12 educators through June 2028 — [openai.com/index/chatgpt-for-teachers](https://openai.com/index/chatgpt-for-teachers/){target=_blank}
    - **Back to School 2026:** verified US college students get 4 free months of Plus; claim by Oct 31, 2026 `(verify)` — [help.openai.com](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students){target=_blank}
    - **Codex credits for students:** $100 in Codex credits for US/Canada university students — [developers.openai.com/community/students](https://developers.openai.com/community/students){target=_blank}

!!! note "Heads-up (September 2026)"
    - **Sora is fully discontinued.** OpenAI shut down the Sora web and app on April 26, 2026 and completed the API sunset on September 24, 2026; no successor has been named. For video work, use [Veo 3.1](https://deepmind.google/models/veo/){target=_blank}, [Runway](https://runwayml.com/){target=_blank}, or [Kling](https://kling.ai/){target=_blank}.
    - **ChatGPT Atlas browser discontinued** on August 9, 2026; the browser agent moved into the ChatGPT desktop app and the Chrome extension.
    - **GPT-6 Astra** was released September 2026 and **GPT-6.1 Sol** on September 29, 2026.
    - **Custom GPTs are being retired** in favor of plugins (skills + apps + MCP), Enterprise first (December 2026), with consumer plans expected to follow `(verify)`.
    - **Prism:** a free, LaTeX-native scientific-writing workspace at [prism.openai.com](https://prism.openai.com/){target=_blank} (launched January 2026 on GPT-5.2).

!!! info "API Pricing (per million tokens, September 2026)"
    Official rates from [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing){target=_blank}; check that page for current rates.

    - **GPT-6 Astra** (flagship): $10 input / $50 output (Ultrafast tier: $60 / $300)
    - **GPT-6.1 Sol** (released Sept 29, 2026): $2 input / $10 output
    - **GPT-6 Sol**: $2 input / $10 output
    - **GPT-6 Luna** (cheapest): $0.10 input / $0.50 output
    - **GPT-5.6 Sol**: $4 input / $20 output
    - **GPT-5.6 Terra**: $2 input / $12 output
    - **GPT-5.6 Luna**: $0.20 input / $1.20 output
    - **GPT-5.3-Codex** (coding): $1.75 input / $14 output
    - **GPT Image 2**: token-priced (about $0.05 per medium 1024px image) `(verify)`

## Using ChatGPT

**Web Interface (chatgpt.com):**

- **Prompting:** Type your requests or questions into the chat box. Be clear and specific in your prompts.
- **Conversation History:** ChatGPT remembers context within the current chat session.
- **Model Selection:** Plus and Pro users can switch between models (flagship multimodal, reasoning-focused, etc.) using the model selector.
- **File Uploads:** Upload images, PDFs, documents, and data files for analysis.
- **Voice Mode:** Use voice input and receive spoken responses (Plus feature).
- **Canvas:** Collaborative editing workspace for writing and coding projects.

**Custom GPTs and plugins:**

- **Custom GPTs are being retired** in favor of plugins — Enterprise workspaces first (December 2026), with consumer plans expected to follow `(verify)`. Existing GPTs and the GPT Store still work for now.
- **Plugins** (since July 2026) bundle skills, apps, and MCP servers into one installable package; browse them in the Plugin Directory.
- **Use Cases:** Research assistants, writing helpers, coding tutors, language learning, and more.

**Advanced Features:**

- **Web Browsing:** Search the internet for current information (enabled by default for Plus users).
- **Data analysis (sandboxed Python):** Run Python code, analyze data, create visualizations, and process files in a browser-based sandbox.
- **GPT Image 1.5 / 2:** Generate and edit images from text descriptions (DALL-E 3 was sunset May 2026).
- **Advanced Voice:** Natural, conversational voice interactions with low latency.
- **Codex:** agentic coding in the cloud, terminal, and VS Code — included in every plan (limited on Free/Go).
- **Deep research** (Plus and above): multi-step web research that returns a cited report.

---

## OpenAI Platform and API

Beyond ChatGPT, OpenAI provides a developer platform for programmatic access to their AI models.

[OpenAI Platform](https://platform.openai.com){target=_blank} allows developers to access the API and integrate powerful AI models into custom applications or systems.

### OpenAI API Access

The OpenAI API provides programmatic access to OpenAI's full model lineup — including flagship multimodal, cost-efficient, and frontier reasoning models, plus image and audio models — enabling integration into applications and research workflows. See [OpenAI's models page](https://platform.openai.com/docs/models){target=_blank} for the current lineup.

**Signing up for the OpenAI API:**

1. **Open the OpenAI Platform:** Go to [platform.openai.com](https://platform.openai.com/){target=_blank}.

2. **Sign up or Log in:**
    - **Sign up:** If you don't have an OpenAI account, create one. You can reuse your ChatGPT account credentials.
    - **Log in:** If you already have an account, log in.

**Creating API Keys:**

1. **Navigate to the API Keys page:** Click on your profile icon in the top-right corner and select "API keys."

2. **Create a new API key:** Click on "Create new secret key."

3. **Name your key (optional):** Give it a descriptive name for tracking purposes.

4. **Copy and securely store your API key:**
   **Important:** You will not be able to view the full API key again. Store it in a password manager or a secure environment variable.

!!! Warning "**Treat your API key like a password**"
    Do not share it publicly or commit it to version control platforms (like GitHub).

### Using the OpenAI API

**Quick Start (Python):**

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-6-sol",  # or "gpt-6-luna" for cheap tasks; model names change — check https://developers.openai.com/api/docs/pricing
    messages=[
        {"role": "user", "content": "Hello, GPT!"}
    ]
)
print(response.choices[0].message.content)
```

**Available SDKs:** Python, Node.js/TypeScript, and community libraries for other languages.

**Developer Resources:**

- **Documentation:** Visit the [OpenAI API Documentation](https://platform.openai.com/docs/overview){target=_blank} for guidance, code examples, and model parameters.

- **Pricing:** Review the [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing){target=_blank} page for cost details, which are based on tokens processed.

- **Rate Limits:** Familiarize yourself with [API rate limits](https://platform.openai.com/docs/guides/rate-limits){target=_blank} to prevent disruptions.

- **Playground:** [:fontawesome-brands-openai: OpenAI Playground](https://platform.openai.com/playground){target=_blank} allows you to experiment with models for Chat, Text Completion, Image generation, Embedding, Speech-to-Text, and Fine Tuning.

!!! tip "Context Windows and Costs"
    Large context windows allow for more extensive prompt engineering and large-document analysis but can increase costs significantly. Plan your usage accordingly.

### OpenAI Cookbook

Check out the [:simple-github: openai/openai-cookbook](https://github.com/openai/openai-cookbook){target=_blank} repository for Jupyter Notebook lessons and examples on using the OpenAI API.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=468576060&machine=basicLinux32gb&location=EastUs)

The cookbook is also available at [cookbook.openai.com](https://cookbook.openai.com){target=_blank}.

---

## Tips for Using ChatGPT

- **Be Specific:** Provide clear instructions and context in your prompts for better results.
- **Iterate:** Refine your prompts based on ChatGPT's responses to improve outcomes.
- **Use System Instructions:** For custom GPTs or API usage, system prompts guide the model's behavior.
- **Leverage Context:** Upload relevant documents or provide background information for complex tasks.
- **Experiment with Models:** Different models excel at different tasks — frontier reasoning models for complex problem-solving, flagship multimodal models for general use, and image/audio models for specialized media tasks.

---

## Additional Resources

**OpenAI Official Resources:**

- **OpenAI Website:** [openai.com](https://openai.com){target=_blank}
- **ChatGPT:** [chatgpt.com](https://chatgpt.com){target=_blank}
- **API Documentation:** [platform.openai.com/docs](https://platform.openai.com/docs/overview){target=_blank}
- **OpenAI Research:** [openai.com/research](https://openai.com/research/){target=_blank}
- **Developer Forum:** [community.openai.com](https://community.openai.com){target=_blank}

**Research and Technical Papers:**

- **GPT-4 Technical Report:** [arxiv.org/abs/2303.08774](https://arxiv.org/abs/2303.08774){target=_blank}
- **OpenAI Publications:** [openai.com/research/index/publication](https://openai.com/research/index/publication/){target=_blank}

**Privacy and Security:**

- Review OpenAI's [Privacy Policy](https://openai.com/policies/privacy-policy){target=_blank} and ensure compliance with your institution's guidelines.
- **Teaching Resources:** Some institutions have specific guidance on using AI tools in education. Check your local teaching center or ask your institution's IT or library services.

---

**Next Steps:**

- After setting up your account, proceed to the [Writing Prompts](prompts.md) section for hands-on prompt engineering exercises and best practices.
- Explore [Choosing the Right AI Platform](choose.md) to compare ChatGPT with Claude, Gemini, and other options.
