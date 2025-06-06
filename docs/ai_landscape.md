# The Landscape

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! info "A Glance at the Generative AI Landscape (2024-2025)"

    The field of Generative AI is rapidly evolving. This section provides a snapshot of some of the most influential models and platforms as of early 2024, with a look towards what we might expect in 2025.

    [![tree](assets/tree.jpeg){width=800}](https://arxiv.org/abs/2304.13712){target=_blank}
    
    Image Credit: [Yang et al. :simple-arxiv:](https://arxiv.org/abs/2304.13712){target=_blank} (While this image depicts the state of LLMs in 2023, it effectively illustrates the foundational models and their evolution)

## View the [:octicons-trophy-24: HuggingFace :simple-huggingface: Arena LLM Leaderboard](https://lmarena.ai/leaderboard){target=_blank}

<iframe
	src="https://lmarena.ai/leaderboard"
	frameborder="0"
	width="850"
	height="450"
></iframe>

## Table: Prices of Services (last checked 06/2025)

| **LLM Service**  | **Plan** | **Price (per month)** | **Details**  |
| :--------------- | :------- | :-------------------- | :----------- |
| [**Anthropic Claude**](https://www.anthropic.com/pricing){target=_blank} | Free | $0 | Access to Claude 3 Sonnet with usage limits |
| | Pro | $20 | 5x more usage, access to Claude 3 Opus and Haiku, priority access |
| | Team | $25/user (min 5) | Everything in Pro plus central billing, team collaboration features |
| [**Claude API**](https://www.anthropic.com/api){target=_blank} | Pay-As-You-Go | Varies | **Claude 3.7 Sonnet:** $3/1M input, $15/1M output <br> **Claude 4 Opus:** $15/1M input, $75/1M output <br> **Claude 3.5 Haiku:** $0.25/1M input, $1.25/1M output |
| [**Google Gemini**](https://gemini.google.com/){target=_blank} | Free | $0 | Access to Gemini Pro with usage limits |
| | Gemini Advanced | $19.99 | Access to Gemini Ultra 1.0, 2TB storage, integration with Google Workspace |
| | Gemini Business | $20/user | Access to Gemini in Workspace apps (Docs, Sheets, Slides, Meet) |
| | Gemini Enterprise | $30/user | Advanced features, enhanced security, admin controls |
| [**Vertex AI Gemini API**](https://cloud.google.com/vertex-ai/docs/generative-ai/pricing){target=_blank} | Pay-As-You-Go | Varies | **Gemini 1.5 Flash:** $0.075/1M input, $0.30/1M output <br> **Gemini 1.5 Pro:** $1.25/1M input, $5.00/1M output <br> **Gemini 2.5 Pro (128k):** $3.50/1M input, $10.50/1M output |
| [**OpenAI ChatGPT**](https://chat.openai.com/){target=_blank} | Free | $0 | Access to GPT-4o mini with usage limits |
| | Plus | $20 | Access to GPT-4+, DALL-E 3, advanced data analysis |
| | Pro | $200 | Unlimited access to o1, o4-mini, GPT-4.5, and Advanced Voice |
| | Team | $25/user | Everything in Plus with higher limits, admin console, team workspace |
| | Enterprise | Contact Sales | Unlimited high-speed GPT-4+ models, extended context windows, enterprise security |
| [**OpenAI API**](https://platform.openai.com/){target=_blank} | Pay-As-You-Go | Varies | **GPT-4o:** $5/1M input, $15/1M output <br> **GPT-4 Turbo:** $10/1M input, $30/1M output <br> **GPT-4:** $30/1M input, $60/1M output <br> **GPT-3.5 Turbo:** $0.50/1M input, $1.50/1M output |
| [**Perplexity AI**](https://www.perplexity.ai/){target=_blank} | Free | $0 | Limited searches with Perplexity model |
| | Pro | $20 | Unlimited Pro searches, file uploads, API access, choice of models (GPT-4, Claude, Gemini) |
| | Enterprise | Contact Sales | Team management, enhanced security, SSO, dedicated support |
| [**Microsoft Copilot**](https://copilot.microsoft.com/){target=_blank} | Free | $0 | Access to GPT-4, limited image generation with DALL-E 3 |
| | Pro | $20/user | Priority access, faster performance, 100 boosts/day with DALL-E 3 |
| [**Microsoft 365 Copilot**](https://www.microsoft.com/microsoft-365/copilot){target=_blank} | Business | $30/user | AI in Word, Excel, PowerPoint, Outlook, Teams. Requires M365 license |
| [**GitHub Copilot**](https://github.com/features/copilot){target=_blank} | Individual | $10 | AI pair programming in VS Code, Visual Studio, Neovim, JetBrains |
| | Business | $19/user | Everything in Individual plus organization management |
| | Enterprise | $39/user | Everything in Business plus security vulnerability filtering, IP indemnity |
| [**Mistral AI**](https://mistral.ai/){target=_blank} | La Plateforme | Varies | **Mistral 7B:** $0.25/1M tokens <br> **Mixtral 8x7B:** $0.70/1M tokens <br> **Mistral Small:** $2/1M input, $6/1M output <br> **Mistral Large:** $8/1M input, $24/1M output |
| [**Cohere**](https://cohere.com/){target=_blank} | Free Trial | $0 | Limited API calls for testing |
| | Production | Varies | **Command:** $1/1M input, $2/1M output <br> **Command Light:** $0.30/1M tokens <br> **Embed:** $0.10/1M tokens |
| [**Midjourney**](https://www.midjourney.com/){target=_blank} | Basic | $10 | ~200 image generations/month |
| | Standard | $30 | 15 hrs fast GPU time, unlimited relaxed |
| | Pro | $60 | 30 hrs fast GPU time, stealth mode |
| | Mega | $120 | 60 hrs fast GPU time, stealth mode |
| [**DALL-E 3**](https://openai.com/dall-e-3){target=_blank} | Via ChatGPT Plus | Included | Image generation within ChatGPT |
| | API | Varies | Standard: $0.040/image, HD: $0.080/image |
| [**Stable Diffusion**](https://stability.ai/){target=_blank} | DreamStudio | $10 | 1000 credits (~5000 images) |
| | API | Varies | $0.002 per image (512x512) |
| [**Grok by xAI**](https://x.com/i/grok){target=_blank} | X Premium | $8 | Access via X (Twitter) Premium |
| | X Premium+ | $16 | Priority access, higher limits |
| [**Character AI**](https://character.ai/){target=_blank} | Free | $0 | Limited features and queue priority |
| | c.ai+ | $9.99 | Priority access, faster responses, exclusive features |
| [**Replicate**](https://replicate.com/){target=_blank} | Pay-As-You-Go | Varies | Run open-source models, pricing per second of compute |
| [**Hugging Face**](https://huggingface.co/){target=_blank} | Free | $0 | Community models and datasets |
| | Pro | $9 | Advanced features, private repos |
| | Enterprise | Contact Sales | Dedicated support, SLAs, security features |
| [**Amazon Bedrock**](https://aws.amazon.com/bedrock/){target=_blank} | On-Demand | Varies | Access to Claude, Llama 2, Stable Diffusion, and more |
| [**Google Vertex AI**](https://cloud.google.com/vertex-ai){target=_blank} | On-Demand | Varies | 130+ foundation models including Gemini, Claude, Llama |
| [**Azure AI Studio**](https://ai.azure.com/){target=_blank} | On-Demand | Varies | Access to GPT-4, Claude, Llama, Mistral, and more |
| [**Meta Llama**](https://llama.meta.com/){target=_blank} | Open Source | Free | Llama 2 and Llama 3 models for download |
| [**Ollama**](https://ollama.com/){target=_blank} | Local Install | Free | Run LLMs locally on your hardware |
| [**LM Studio**](https://lmstudio.ai/){target=_blank} | Local Install | Free | Desktop app for running LLMs locally |
| [**Jan.ai**](https://jan.ai/){target=_blank} | Local Install | Free | Open-source ChatGPT alternative, runs locally |
| [**Continue.dev**](https://continue.dev/) | Open Source | Free | Open-source autopilot for VS Code and JetBrains |
| [**Poe by Quora**](https://poe.com/){target=_blank} | Monthly | $19.99 | Access to various chatbots including GPT-4, Claude |
|                                                        | Yearly | $199.99 | Annual subscription with all chatbot access |
| [**You.com**](https://you.com/pro){target=_blank} | YouPro | $20 | Latest AI models, personalized AI with memory |
| [**Jasper AI**](https://www.jasper.ai/pricing){target=_blank} | Creator | $49 | Writing assistant with templates |
| | Teams | $125 | Advanced features for small teams |
| | Business | Contact Sales | Custom pricing for organizations |
| [**Replit AI**](https://replit.com/pricing){target=_blank} | Core | $20 | AI coding assistant integrated in Replit IDE |

**Notes:**

*   Token pricing for API access can be complex. Refer to each provider's pricing page for the most accurate and up-to-date details.
*   "Contact Sales" typically indicates that pricing is customized based on usage, features, and the specific needs of the customer.
*   Many services offer free trials or limited free tiers, allowing you to test them out before committing to a paid plan.

**Additional Chatbot and LLM Services:**

1.  **Amazon Bedrock, Azure AI Foundry, Google Vertex:** Provide access to various foundation models but each run on a respective cloud service provider's hardware. Ideal for companies and institutions already running their infrastructure on commercial cloud services. 
   
2.  **You.com:** Offers a pro plan with access to latest AI models, personalized AI with memory and advanced AI writing tools.
   
3.  **Poe by Quora:**  A platform that gives you access to various chatbots (like GPT-4, Claude, etc.) through a single subscription.

!!! Info "Image and Video Generation Models"

    ## **Image Generation Models**

    **Stable Diffusion 3.5**

    [Stable Diffusion 3.5](https://stability.ai/stable-diffusion-3-5){target=_blank} is the latest iteration from [Stability AI](https://stability.ai/){target=_blank}, featuring multiple model sizes:
    - **SD3.5 Large (8B)**: High-quality generation with advanced prompt adherence
    - **SD3.5 Medium (2.5B)**: Balanced performance and quality
    - **SD3.5 Large Turbo**: Optimized for speed with 4-8 step generation

    Models are available via [HuggingFace](https://huggingface.co/stabilityai){target=_blank}, [GitHub](https://github.com/Stability-AI/StableDiffusion){target=_blank}, and various APIs.

    **FLUX Models**

    [FLUX](https://blackforestlabs.ai/){target=_blank} by Black Forest Labs (creators of Stable Diffusion) offers state-of-the-art diffusion models:
    - **FLUX.1 [pro]**: Top-tier model for commercial use
    - **FLUX.1 [dev]**: Open-weight model for non-commercial use
    - **FLUX.1 [schnell]**: Fast local generation model

    **Other Leading Image Generation Models**

    *   [DALL·E 3](https://openai.com/dall-e-3){target=_blank} (OpenAI): Photorealistic generation with excellent prompt understanding, integrated into ChatGPT Plus
    *   [Midjourney v6.1](https://www.midjourney.com/){target=_blank}: Industry-leading artistic and stylized generation via Discord
    *   [Imagen 3](https://deepmind.google/technologies/imagen-3/){target=_blank} (Google): Advanced text-to-image with excellent photorealism, available in ImageFX
    *   [Adobe Firefly 3](https://www.adobe.com/products/firefly.html){target=_blank}: Enterprise-focused with commercial-safe training data
    *   [Ideogram 2.0](https://ideogram.ai/){target=_blank}: Excellent text rendering capabilities within images
    *   [Leonardo.AI](https://leonardo.ai/){target=_blank}: Real-time canvas generation with fine-tuned models

    ## **Video Generation Models**

    **Google Veo 3**

    [Veo 3](https://deepmind.google/models/veo/){target=_blank} represents Google's latest advancement in video generation:
    - Generates up to 4K resolution videos
    - Includes voices and sound effects
    - Improved understanding of real-world physics and human movement
    - Better camera control and cinematic effects
    - Available through Google Labs and VideoFX

    **OpenAI Sora**

    [Sora](https://openai.com/sora){target=_blank} (OpenAI) features:
    - Up to 1-minute video generation at 1080p
    - Advanced physics simulation and 3D consistency
    - Available to ChatGPT Plus and Pro subscribers
    - Turbo mode for faster generation

    **Other Notable Video Generation Models**

    *   [Runway Gen-3 Alpha](https://runwayml.com/){target=_blank}: Professional-grade with advanced motion control
    *   [Pika 2.0](https://pika.art/){target=_blank}: Scene editing and sound effects generation
    *   [Stable Video Diffusion 2](https://stability.ai/stable-video){target=_blank}: Open-source image-to-video model
    *   [Meta Movie Gen](https://ai.meta.com/research/movie-gen/){target=_blank}: High-quality video with synchronized audio (research preview)
    *   [Kling 1.5](https://klingai.com/){target=_blank}: Chinese model with impressive motion quality
    *   [HeyGen](https://www.heygen.com/){target=_blank}: Specialized in AI avatar video generation
    *   [Synthesia](https://www.synthesia.io/){target=_blank}: Enterprise-focused avatar video platform

    ## **Advanced Capabilities**

    **Image and Video Understanding**

    *   [Segment Anything Model 2 (SAM 2)](https://segment-anything.com/){target=_blank} (Meta): Real-time segmentation for images and videos
    *   [CLIP](https://openai.com/research/clip){target=_blank} (OpenAI): Vision-language understanding
    *   [LLaVA](https://llava-vl.github.io/){target=_blank}: Open-source visual instruction tuning

    **3D Generation**

    *   [DreamGaussian](https://dreamgaussian.github.io/){target=_blank}: Text/image to 3D in minutes
    *   [Meshy](https://www.meshy.ai/){target=_blank}: Text to 3D mesh generation
    *   [Luma Genie](https://lumalabs.ai/genie){target=_blank}: Text to 3D model generation

    **Emerging Trends**

    *   **Consistency Models**: Faster generation with fewer steps
    *   **ControlNet Integration**: Precise control over generation
    *   **Real-time Generation**: Sub-second image creation
    *   **Multimodal Models**: Unified image, video, and audio generation
    *   **Neural Radiance Fields (NeRFs)**: 3D scene representation
    *   **Diffusion Transformers (DiT)**: Next-generation architectures

!!! Info "Glossary"

    [:simple-google: Google's Machine Learning Glossary](https://developers.google.com/machine-learning/glossary){target=_blank}

    [:simple-nvidia: NVIDIA's Data Science Glossary](https://www.nvidia.com/en-us/glossary){target=_blank}

    **Agentic AI:** uses sophisticated reasoning and iterative planning to autonomously solve complex, multi-step problems.

    **Anthropic:**  
    A research organization emphasizing AI safety and governance. Known for **Claude**, a large language model (LLM) with advanced reasoning and robust safety features.

    **ChatGPT:**  
    OpenAI’s general-purpose LLM, renowned for its conversational strengths, versatility, and ability to adapt to varied tasks through effective prompt engineering.

    **Claude:**  
    Anthropic’s LLM, recognized for its interpretability, strong reasoning capabilities, and rigorous safety considerations.

    **Copilot (GitHub, Microsoft):**  
    An AI-driven developer assistant offering code suggestions, debugging support, and efficiency improvements, leveraging generative AI to boost productivity.

    **Embeddings:**  
    Numerical vector representations of data (e.g., text, images, audio) that capture semantic meaning and relationships. Useful for search, clustering, recommendation, and more.

    **Foundation Models:**  
    Large-scale deep learning models (e.g., LLMs, vision models, multimodal models) trained on massive datasets. They serve as a base or "foundation" for a wide range of downstream tasks, enabling transfer learning and rapid adaptation.

    **Gemini:**  
    Google’s family of multimodal foundation models, capable of understanding and generating text, images, and other data types, reflecting Google’s advancements in AI research.

    **GitHub:**  
    A leading platform for version control and software collaboration. Now integrated with AI tools like GitHub Copilot for enhanced code development workflows.

    **HuggingFace:**  
    A hub and community for open-source AI models, datasets, and applications. Widely used in the natural language processing (NLP) community for model sharing and development.

    **Large Language Models (LLMs):**  
    A subset of foundation models trained on extensive text corpora, enabling them to generate human-like text, summarize information, reason about topics, and perform a variety of NLP tasks. Examples include **GPT**, **Claude**, and **Gemini**.

    **Parameters:**  
    The trainable values within a neural network, updated during the training process to minimize loss and define the model’s learned behavior.

    **Prompt Engineering:**  
    The practice of crafting, refining, and optimizing instructions (prompts) given to AI models in order to guide their outputs toward desired results.

    **Stable Diffusion:**  
    A family of open-source latent-diffusion-based models used for generating high-quality images from text or other forms of input (e.g., sketches).

    **Token:**  
    A fundamental unit of text—often a word, subword, or character—that LLMs process when understanding or generating language.

    **Weights:**  
    Numerical parameters within a neural network that determine the strength of connections between neurons or nodes.

    **Zero-shot Learning:**  
    The capability of an AI model to perform tasks it has never been explicitly trained on, often made possible by large-scale pretraining on diverse datasets.
