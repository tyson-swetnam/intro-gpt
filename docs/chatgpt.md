# :fontawesome-brands-openai: OpenAI ChatGPT

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## About OpenAI and ChatGPT

**OpenAI** is an artificial intelligence research company founded in 2015, known for developing some of the most influential AI models in recent years. Their flagship product, **ChatGPT**, launched in November 2022 and quickly became the fastest-growing consumer application in history.

ChatGPT is powered by a family of large language models (LLMs) including GPT-4, GPT-4o, and the reasoning-focused o1 and o3 models. These models can understand and generate human-like text, analyze images, write code, and assist with a wide range of tasks.

## Creating a ChatGPT Account

**Log In to Your Account**

   - Visit [chatgpt.com](https://chatgpt.com/){target=_blank} and log in using your existing credentials or create a new account.

**Access Account Settings:**

   - Once logged in, look for the sidebar (usually on the left).
   - Click on the **"Upgrade to Plus"** or **"Manage my plan"** button.
     - If you do not see this option, try refreshing the page or updating your browser.

**Initiate Upgrade:**

   - Click **"Upgrade to Plus"** ($20/mo), or **"Upgrade to Pro"** ($200/mo).
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

!!! info "Pricing (as of January 2025)"

    **Free Tier**

    - Access to GPT-4o with usage limits
    - Standard response speed
    - Limited access to advanced features
    - Good for casual users exploring AI capabilities

    **ChatGPT Plus ($20/month)**

    - Priority access during peak hours
    - Faster response speeds
    - Access to GPT-4, GPT-4o, and o1 reasoning models
    - Image generation with DALL-E 3
    - File uploads, voice mode, and data analysis
    - Custom GPTs and GPT Store access
    - Advanced Voice mode with natural conversation

    **ChatGPT Pro ($200/month)**

    - Everything in Plus
    - Unlimited access to o1 and o1 pro mode (enhanced reasoning)
    - Unlimited access to GPT-4o
    - Higher limits on advanced features
    - Access to Sora video generation
    - Deep Research tool for comprehensive analysis
    - Priority access to newest features

    **ChatGPT Team ($25-30/user/month)**

    - Everything in Plus
    - Admin controls and workspace management
    - Higher usage limits per user
    - Data excluded from training by default
    - Minimum 2 users required

    **ChatGPT Enterprise (Custom pricing)**

    - Unlimited high-speed GPT-4 access
    - Enterprise-grade security and compliance
    - Admin console with SSO and domain verification
    - Custom data retention policies
    - Priority support

## Using ChatGPT

**Web Interface (chatgpt.com):**

- **Prompting:** Type your requests or questions into the chat box. Be clear and specific in your prompts.
- **Conversation History:** ChatGPT remembers context within the current chat session.
- **Model Selection:** Plus and Pro users can switch between models (GPT-4o, o1, etc.) using the model selector.
- **File Uploads:** Upload images, PDFs, documents, and data files for analysis.
- **Voice Mode:** Use voice input and receive spoken responses (Plus feature).
- **Canvas:** Collaborative editing workspace for writing and coding projects.

**Custom GPTs:**

- **GPT Store:** Browse and use specialized GPTs created by OpenAI and the community.
- **Create Your Own:** Build custom GPTs with specific instructions, knowledge, and capabilities.
- **Use Cases:** Research assistants, writing helpers, coding tutors, language learning, and more.

**Advanced Features:**

- **Web Browsing:** Search the internet for current information (enabled by default for Plus users).
- **Code Interpreter:** Run Python code, analyze data, create visualizations, and process files.
- **DALL-E 3:** Generate and edit images from text descriptions.
- **Advanced Voice:** Natural, conversational voice interactions with low latency.

---

## OpenAI Platform and API

Beyond ChatGPT, OpenAI provides a developer platform for programmatic access to their AI models.

[OpenAI Platform](https://platform.openai.com){target=_blank} allows developers to access the API and integrate powerful AI models into custom applications or systems.

### OpenAI API Access

The OpenAI API provides programmatic access to models like GPT-4, GPT-4o, o1, DALL-E, and more, enabling integration into applications and research workflows.

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
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, GPT!"}
    ]
)
print(response.choices[0].message.content)
```

**Available SDKs:** Python, Node.js/TypeScript, and community libraries for other languages.

**Developer Resources:**

- **Documentation:** Visit the [OpenAI API Documentation](https://platform.openai.com/docs/overview){target=_blank} for guidance, code examples, and model parameters.

- **Pricing:** Review the [OpenAI API Pricing](https://openai.com/api/pricing/){target=_blank} page for cost details, which are based on tokens processed.

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
- **Experiment with Models:** Different models excel at different tasks - o1 for reasoning, GPT-4o for general use, DALL-E for images.

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
