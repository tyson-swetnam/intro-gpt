# Choosing the Right AI Platform

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

This comprehensive guide helps you choose the right AI platform for your needs. All pricing information has been verified as of **May 2026**.

---

## Platform Comparison Tables

Below are tables that rank popular AI platforms by use case, organized by Chat, Research, Code, and Image/Video generation capabilities.

### Best for Chat

| **Platform** | **Strength** | **Weakness** | **Cost** | **Interface** | **Docs** |
|--------------|--------------|--------------|----------|---------------|----------|
| **Claude (Anthropic)** | - Fast, coherent dialogue <br/>- Large context window <br/>- Strong reasoning | - API can be expensive <br/>- Limited third-party integrations | Free, $20/mo (Pro), $100-200/mo (Max), $30+/seat (Team) | [**Claude**](https://claude.ai){target=_blank} | [**Anthropic Docs**](https://docs.anthropic.com/){target=_blank} |
| **Gemini (Google)** | - Multimodal (images + text + video) <br/>- Strong Google integration | - Some features Beta/experimental <br/>- Pricing tiers complex | Free, $7.99/mo (AI Plus), $19.99/mo (AI Pro), $249.99/mo (AI Ultra) | [**Gemini**](https://gemini.google.com/){target=_blank} | [**Gemini Docs**](https://ai.google.dev/gemini-api/docs){target=_blank} |
| **ChatGPT (OpenAI)** | - Strong reasoning (o-series) <br/>- Extensive plugin ecosystem <br/>- Multi-turn conversation | - Subscription required for best models <br/>- Usage caps on free tier <br/>- Free tier shows ads in US (Feb 9, 2026) | Free (now ad-supported in US), $8/mo (Go with ads), $20/mo (Plus), $100/mo (NEW Pro tier as of April 2026, verify), $200/mo (Pro), Team/Enterprise | [**ChatGPT**](https://chatgpt.com/){target=_blank} | [**OpenAI Docs**](https://platform.openai.com/docs/){target=_blank} |
| **DeepSeek (Open Source)**  | - Extremely affordable API <br/>- Open source models | - Smaller dev community <br/>- Data stored in China | Free (Web Chat) / Free (Open Source) / API from $0.28 per 1M tokens | [**DeepSeek Chat**](https://chat.deepseek.com/){target=_blank} | [**DeepSeek Docs**](https://api-docs.deepseek.com/){target=_blank} |
| **Microsoft 365 Copilot** | - Deep MS Office integration <br/>- Enterprise features | - Requires M365 license <br/>- Premium pricing | Free (Chat), $21/mo (Business), $30/mo (Enterprise) | [**Copilot**](https://copilot.microsoft.com/){target=_blank} | [**Copilot Docs**](https://learn.microsoft.com/en-us/copilot/microsoft-365/){target=_blank} |
| **Grok (xAI)** | - Multimodal capabilities <br/>- X platform integration | - Premium pricing <br/>- Content restrictions | Free (limited), $40/mo (X Premium+), API from $0.20 per 1M tokens | [**Grok**](https://grok.com){target=_blank} | [**xAI Docs**](https://docs.x.ai/docs/overview){target=_blank} |
| **HuggingFace Chat** | - 113+ open source models <br/>- Free access | - Quality varies by model <br/>- Some features need Pro | Free, $9/mo (Pro), $20/user/mo (Team), $50+/mo (Enterprise) | [**HF Chat**](https://huggingface.co/chat/){target=_blank} | [**HF Docs**](https://huggingface.co/docs){target=_blank} |
| **Jasper** | - Marketing-focused <br/>- Content workflows | - Expensive for individual use <br/>- Less technical depth | $59/mo (Pro), $69/mo (monthly billing) | [**Jasper**](https://www.jasper.ai/){target=_blank} | [**Jasper Docs**](https://developers.jasper.ai/){target=_blank} |
| **Perplexity** | - Research + search <br/>- Citation backing | - Subscription for advanced features | Free, $20/mo (Pro), $200/mo (Max) | [**Perplexity**](https://www.perplexity.ai/){target=_blank} | [**Perplexity Docs**](https://docs.perplexity.ai/){target=_blank} |
| **NotebookLM (Google)** | - RAG capabilities <br/>- Google Drive integration | - Still evolving features | Free, $19.99/mo (Plus via Google One AI Premium) | [**NotebookLM**](https://notebooklm.google.com/){target=_blank} | [**NotebookLM Docs**](https://support.google.com/notebooklm){target=_blank} |
| **Vicuna** | - Open source <br/>- Free to use | - Smaller than frontier models <br/>- Self-hosting required | Free (self-host) or free demos | [**Vicuna Demo**](https://chat.lmsys.org/){target=_blank} | [**Vicuna GitHub**](https://github.com/lm-sys/FastChat){target=_blank} |
| **Pi (Inflection AI)** | - Empathetic conversation style <br/>- Personal AI | - Rate limited <br/>- No coding support | Free (personal use, rate limits) | [**Pi**](https://pi.ai){target=_blank} | N/A (Enterprise API only) |
| **Poe (Quora)** | - Access to multiple models <br/>- Single subscription | - Usage caps on free tier | $4.99/mo (Lite, 10k daily points), $19.99/mo (Standard, 1M monthly points), $249.99/mo (Power, 12.5M monthly points) | [**Poe**](https://poe.com/){target=_blank} | [**Poe Docs**](https://help.poe.com/){target=_blank} |
| **Mistral AI** | - European LLMs <br/>- Multilingual | - Still evolving ecosystem | Free + API from $0.02-$6 per 1M tokens, Le Chat Pro $14.99/mo | [**Mistral**](https://mistral.ai/){target=_blank} | [**Mistral Docs**](https://docs.mistral.ai/){target=_blank} |
| **Latimer** | - Diversity-focused training <br/>- Inclusive perspective | - Smaller user base | Free (100 interactions), $9.99/mo (Individual) | [**Latimer**](https://app.latimer.ai/){target=_blank} | Email: support@latimer.ai |
| **Meta AI (Llama)** | - Open source <br/>- Multiple model sizes available | - Self-hosting requires resources | Free (self-host) or enterprise | [**Llama**](https://www.llama.com/){target=_blank} | [**Meta GitHub**](https://github.com/facebookresearch/llama){target=_blank} |
| **Apple Intelligence** | - iOS/macOS integration <br/>- Privacy-focused | - Apple ecosystem only | Included on Apple devices (iOS 18.1+, M1+ Macs) | [**Apple Intelligence**](https://www.apple.com/apple-intelligence/){target=_blank} | [**Apple Dev Docs**](https://developer.apple.com/apple-intelligence/){target=_blank} |
| **Amazon Titan** | - AWS ecosystem <br/>- Bedrock integration | - Enterprise-focused | Pay-per-use on Bedrock | [**Titan**](https://aws.amazon.com/bedrock/titan/){target=_blank} | [**AWS Docs**](https://docs.aws.amazon.com/bedrock/){target=_blank} |
| **Amazon Bedrock** | - Multi-model platform <br/>- 100+ models | - Requires AWS account | Pay-per-use (varies by model) | [**Bedrock**](https://aws.amazon.com/bedrock/){target=_blank} | [**Bedrock Docs**](https://docs.aws.amazon.com/bedrock/){target=_blank} |
| **Azure OpenAI Service** | - Enterprise security <br/>- Azure integration | - Azure subscription required | Pay-per-use (Azure pricing) | [**Azure OpenAI**](https://azure.microsoft.com/en-us/products/ai-services/openai-service){target=_blank} | [**Azure Docs**](https://learn.microsoft.com/en-us/azure/ai-services/openai/){target=_blank} |
| **Merlin AI** | - Multi-function tool <br/>- Browser extension | - "Unlimited" has hidden caps | Free (limited), $19/mo (Pro with $100/mo usage cap) | [**Merlin**](https://www.getmerlin.in/){target=_blank} | [**Merlin Help**](https://www.getmerlin.in/help){target=_blank} |

---

### Best for Research

| **Platform** | **Strength** | **Weakness** | **Cost** | **Interface** | **Docs** |
|--------------|--------------|--------------|----------|---------------|----------|
| **Perplexity** | - Citation-backed answers <br/>- Web search integration | - Subscription for Pro searches | Free, $20/mo (Pro), $200/mo (Max) | [**Perplexity**](https://www.perplexity.ai/){target=_blank} | [**Perplexity Docs**](https://docs.perplexity.ai/){target=_blank} |
| **Gemini (Google)** | - In-depth analysis <br/>- Chain-of-thought reasoning | - Can be slow for complex queries | Free, $7.99/mo (AI Plus), $19.99/mo (AI Pro), $249.99/mo (AI Ultra) | [**Gemini**](https://gemini.google.com/){target=_blank} | [**Gemini Docs**](https://ai.google.dev/gemini-api/docs){target=_blank} |
| **ChatGPT (OpenAI)** | - Advanced reasoning <br/>- Multi-step problems | - Requires Plus/Pro subscription | $20/mo (Plus), $200/mo (Pro) | [**ChatGPT**](https://chatgpt.com/){target=_blank} | [**OpenAI Docs**](https://platform.openai.com/docs/){target=_blank} |
| **Claude (Anthropic)** | - Strong analysis <br/>- 200K context window | - Higher API costs | Free, $20/mo (Pro), $100-200/mo (Max) | [**Claude**](https://claude.ai){target=_blank} | [**Anthropic Docs**](https://docs.anthropic.com/){target=_blank} |
| **ScholarAI** | - 200M+ papers <br/>- Academic focus | - Requires ChatGPT Plus or standalone subscription | Free (5 credits), $9.99/mo (Basic), $18.99/mo (Premium) | [**Scholar AI GPT**](https://chatgpt.com/g/g-L2HknCZTC-scholar-ai){target=_blank} / [**Web App**](https://app.scholarai.io){target=_blank} | [**ScholarAI Docs**](https://docs.scholarai.io){target=_blank} |
| **Scholar GPT** | - Academic database access <br/>- ChatGPT integration | - Requires ChatGPT Plus | $20/mo (ChatGPT Plus required) | [**Scholar GPT**](https://chatgpt.com/g/g-kZ0eYXlJe-scholar-gpt){target=_blank} | [**User Guide**](https://test.scholar-ai.net/gpt-guide){target=_blank} |
| **Semantic Scholar** | - 232M+ papers <br/>- Free API | - Not a conversational AI <br/>- Search-focused | Free | [**Semantic Scholar**](https://www.semanticscholar.org/){target=_blank} | [**API Docs**](https://api.semanticscholar.org/){target=_blank} |
| **Elicit** | - AI literature review <br/>- 138M+ papers | - Premium features expensive | Free (limited), $12/mo (Plus), $49/mo (Pro), $79/seat/mo (Team) | [**Elicit**](https://elicit.org/){target=_blank} | [**Elicit Support**](https://support.elicit.com/){target=_blank} |
| **Consensus** | - AI research summaries <br/>- 200M+ papers | - Limited free tier | Free (limited), $12-15/mo (Pro), $12.99/seat/mo (Teams) | [**Consensus**](https://consensus.app/){target=_blank} | [**Consensus Help**](https://help.consensus.app/){target=_blank} |
| **Scite** | - Smart Citations <br/>- 1.5B citations analyzed | - Subscription required for full access | Free (limited), $20/mo | [**Scite**](https://scite.ai/){target=_blank} | [**Scite API**](https://api.scite.ai/docs){target=_blank} |
| **Ai2 OpenScholar** | - 45M+ open-access papers <br/>- Citation accuracy | - Open-access content only | Free | [**OpenScholar Demo**](https://openscholar.allen.ai){target=_blank} | [**GitHub**](https://github.com/AkariAsai/OpenScholar){target=_blank} |
| **Polymathic AI** | - Scientific research focus <br/>- 72 models on HuggingFace | - Specialized for STEM | Free (Open Source) | [**Polymathic AI**](https://polymathic-ai.org/){target=_blank} | [**GitHub**](https://github.com/PolymathicAI){target=_blank} / [**HuggingFace**](https://huggingface.co/polymathic-ai){target=_blank} |
| **You.com** | - Multi-model access <br/>- Customizable AI agents | - Paid subscription for advanced | Free, $20/mo (Pro), $200/mo (Max) | [**You.com**](https://you.com/){target=_blank} | [**You.com Docs**](https://documentation.you.com/){target=_blank} |
| **OpenResearcher** | - arXiv integration <br/>- Open source | - arXiv-only corpus <br/>- Requires self-hosting | Free (Open Source) | [**arXiv Paper**](https://arxiv.org/abs/2408.06941){target=_blank} | [**GitHub**](https://github.com/GAIR-NLP/OpenResearcher){target=_blank} |

---

### Best for Code

| **Platform** | **Strength** | **Weakness** | **Cost** | **Interface** | **Docs** |
|--------------|--------------|--------------|----------|---------------|----------|
| **Claude Code (Anthropic)** | - CLI/IDE integration <br/>- Strong code generation | - Requires Pro+ subscription | Included with Pro ($20/mo) or higher | [**Claude**](https://claude.ai){target=_blank} | [**Anthropic Docs**](https://docs.anthropic.com/){target=_blank} |
| **Gemini (Google)** | - Code + text synergy <br/>- Fast responses | - Less specialized than dedicated coding tools | Free, $7.99/mo (AI Plus), $19.99/mo (AI Pro) | [**Gemini**](https://gemini.google.com/){target=_blank} | [**Gemini Docs**](https://ai.google.dev/gemini-api/docs){target=_blank} |
| **GitHub Copilot** | - Seamless IDE integration <br/>- Code completions | - Subscription required for unlimited | Free (students/OSS), $10/mo (Pro), $39/mo (Pro+), $19/user/mo (Business) <br/>Transitions to usage-based billing June 1, 2026 | [**GitHub Copilot**](https://github.com/features/copilot){target=_blank} | [**Copilot Docs**](https://docs.github.com/en/copilot){target=_blank} |
| **ChatGPT (OpenAI)** | - Interactive code execution <br/>- Good for learning | - Requires Plus/Pro for best experience <br/>- Free tier shows ads in US (Feb 9, 2026) | Free (now ad-supported in US), $20/mo (Plus), $100/mo (NEW Pro tier as of April 2026, verify), $200/mo (Pro) | [**ChatGPT**](https://chatgpt.com/){target=_blank} | [**OpenAI Docs**](https://platform.openai.com/docs/guides/code){target=_blank} |
| **Continue.dev** | - Open source <br/>- Multiple model support | - Requires technical setup <br/>- Users pay LLM API costs | Free (Open Source, users pay API costs) | [**Continue.dev**](https://continue.dev/){target=_blank} | [**Continue Docs**](https://continue.dev/docs/){target=_blank} |
| **Codeium (Windsurf)** | - Free tier available <br/>- IDE integration | - Rebranded to Windsurf (acquired by Cognition AI Dec 2025) <br/>- Credit-based limits | Free (5 sessions/day), $15/mo (Pro), $35/mo (Pro Plus) (verify), $25-35/user/mo (Teams) (verify), $60/user/mo (Enterprise) (verify) | [**Windsurf**](https://www.codeium.com/){target=_blank} | [**Codeium Docs**](https://docs.codeium.com/){target=_blank} |
| **Phind** | - Code search + AI chat | **Discontinued January 16, 2026** | **Discontinued January 16, 2026** — alternatives: Cursor, GitHub Copilot, Perplexity | [**Phind**](https://www.phind.com/){target=_blank} | [**Phind Help**](https://help.phind.com/hc/en-us){target=_blank} |
| **Replit AI** | - Cloud IDE + AI <br/>- Multi-language support | - Subscription for full features | Free tier, $20/mo (Core, ~5 collaborators), $100/mo (Pro, ~15 builders), Enterprise custom | [**Replit AI**](https://replit.com/ai){target=_blank} | [**Replit Docs**](https://docs.replit.com/){target=_blank} |
| **StarCoder** | - Open source <br/>- Multiple model sizes | - Self-hosting required | Free (Open Source) | [**StarCoder2**](https://huggingface.co/bigcode){target=_blank} | [**BigCode**](https://www.bigcode-project.org/){target=_blank} |
| **Code Llama (Meta)** | - Specialized for coding <br/>- Multiple variants | ⚠️ **Repository archived July 2025** - consider StarCoder2 instead | Free (Open Source, archived) | [**Code Llama**](https://ai.meta.com/blog/code-llama-large-language-model-coding/){target=_blank} | [**Meta GitHub**](https://github.com/facebookresearch/llama){target=_blank} |

---

### Best for Image/Video

| **Platform** | **Strength** | **Weakness** | **Cost** | **Interface** | **Docs** |
|--------------|--------------|--------------|----------|---------------|----------|
| **Gemini Nano Banana 2 (Google)** | - State-of-the-art image editing <br/>- Multi-image fusion, character consistency <br/>- Conversational refinement <br/>- SynthID watermark on every output | - Editing-first model; pure txt2img not always best | ~$0.039/image (Gemini API) or included in Gemini AI Pro/Ultra | [**Gemini**](https://gemini.google.com/){target=_blank} | [**Nano Banana Docs**](https://ai.google.dev/gemini-api/docs/image-generation){target=_blank} |
| **GPT Image 1.5 / 2 (OpenAI)** | - Top-ranked on human-vote leaderboards (May 2026) <br/>- Native ChatGPT integration <br/>- Strong text rendering and instruction following | - Higher per-image cost than Gemini <br/>- Geographic restrictions on some features | $20/mo (ChatGPT Plus) or per-image API pricing | [**ChatGPT**](https://chatgpt.com/){target=_blank} | [**OpenAI Image Docs**](https://platform.openai.com/docs/guides/images){target=_blank} |
| **Imagen 4 / Imagen 4 Ultra (Google)** | - Best-in-class photorealism <br/>- Strong text rendering | - Vertex AI / API only | Per-image API pricing via Vertex AI | [**Imagen**](https://deepmind.google/models/imagen/){target=_blank} | [**Imagen Docs**](https://ai.google.dev/gemini-api/docs/imagen){target=_blank} |
| **Midjourney v7** | - Exceptional artistic quality <br/>- Web interface available | - Subscription required | $10/mo (Basic), $30/mo (Standard), $60/mo (Pro), $120/mo (Mega) | [**Midjourney**](https://www.midjourney.com/){target=_blank} | [**Midjourney Docs**](https://docs.midjourney.com/){target=_blank} |
| **FLUX 1.1 Pro / FLUX 2 Pro (Black Forest Labs)** | - Best technical quality + speed <br/>- Open-weight tiers (Schnell, dev) | - Pro tiers API-only | Free open-weights (Schnell/dev) or per-image API | [**Black Forest Labs**](https://bfl.ai/){target=_blank} | [**FLUX Docs**](https://docs.bfl.ai/){target=_blank} |
| **Ideogram v3** | - Best-in-class text rendering and typography | - Less photorealistic than Imagen 4 | Free tier; $7-$48/mo paid plans | [**Ideogram**](https://ideogram.ai/){target=_blank} | [**Ideogram Docs**](https://developer.ideogram.ai){target=_blank} |
| **Stable Diffusion 3.5 (Stability AI)** | - Open source <br/>- Highly customizable, runs locally | - Requires technical knowledge | Free (open weights) or API services | [**Stability AI**](https://stability.ai/){target=_blank} | [**SD 3.5**](https://stability.ai/news/introducing-stable-diffusion-3-5){target=_blank} |
| **Adobe Firefly** | - Creative Cloud integration <br/>- Commercial-safe training data | - Subscription required | $9.99-$29.99/mo (standalone) or $70/mo (CC Pro) | [**Firefly**](https://firefly.adobe.com/){target=_blank} | [**Firefly Docs**](https://developer.adobe.com/firefly-services/docs/guides/){target=_blank} |
| **Veo 3 (Google)** | - High-quality video with native audio <br/>- Up to 4K resolution | - Limited daily generation on consumer tiers | $0.15-$0.60/second (API) or $19.99-$249.99/mo (subscription via AI Pro/Ultra) | [**Veo**](https://deepmind.google/technologies/veo/){target=_blank} | [**Veo Docs**](https://ai.google.dev/gemini-api/docs/video){target=_blank} |
| **Sora 2 (OpenAI)** | - Text-to-video with native audio <br/>- Up to 1080p | ⚠️ **NOT available in EU/UK** | $20/mo (ChatGPT Plus), $200/mo (ChatGPT Pro) | [**Sora**](https://openai.com/sora){target=_blank} | [**Sora Research**](https://openai.com/research/video-generation-models-as-world-simulators){target=_blank} |
| **Runway ML** | - Professional video tools <br/>- Latest generation models | - Higher-res requires paid plans | $15/mo (monthly), $12/mo (annual) to $95/mo | [**Runway**](https://runwayml.com/){target=_blank} | [**Runway Docs**](https://docs.runwayml.com/){target=_blank} |

---

!!! Info "Image and Video Generation Models"

    ## **Image Generation Models**

    The image-generation landscape in May 2026 has consolidated around a small set of multimodal frontier models (Nano Banana, GPT Image, Imagen 4) plus standalone leaders for artistic, technical, and typography work, alongside a strong open-weight ecosystem.

    **Multimodal chat-integrated (current leaders for editing and conversational refinement):**

    *   [**Gemini 2.5 Flash Image / Nano Banana 2**](https://deepmind.google/models/gemini-image/){target=_blank} (Google): State-of-the-art editing model. Multi-image fusion, character/style consistency across generations, targeted local edits via natural language ("blur the background," "remove the truck," "change the pose"), and SynthID watermarking on every output. Best for high-volume generation, conversational editing, and synthetic-data workflows. Nano Banana Pro / Nano Banana 2 (Gemini 3 Pro Image) adds 4K photorealism. ([API docs](https://ai.google.dev/gemini-api/docs/image-generation){target=_blank})
    *   [**GPT Image 1.5 / GPT Image 2**](https://platform.openai.com/docs/guides/images){target=_blank} (OpenAI): Top-ranked on the [LLM Stats human-vote leaderboard](https://llm-stats.com/leaderboards/best-ai-for-image-generation){target=_blank} (May 2026). Native ChatGPT integration, strong instruction following, multi-turn refinement. Replaced DALL-E 3.
    *   [**Imagen 4 / Imagen 4 Ultra**](https://deepmind.google/models/imagen/){target=_blank} (Google): Best-in-class photorealism and text rendering. Available via Vertex AI and the Gemini API.

    **Standalone commercial leaders:**

    *   [**Midjourney v7**](https://www.midjourney.com/){target=_blank}: Released April 2025. Still the benchmark for artistic and aesthetic image quality. Web and Discord interfaces.
    *   [**FLUX 1.1 Pro / FLUX 2 Pro**](https://bfl.ai/){target=_blank} (Black Forest Labs): Best technical quality plus speed (~4.5s generation). Often the best default for general commercial use. Open-weight tiers (Schnell, dev) also available.
    *   [**Ideogram v3**](https://ideogram.ai/){target=_blank}: Owns the typography niche. If text rendering matters in your output, start here.
    *   [**Adobe Firefly**](https://firefly.adobe.com/){target=_blank}: Commercial-safe training data, deep Creative Cloud integration. Important if you need indemnification for client work.
    *   [**Recraft V3**](https://www.recraft.ai/){target=_blank}: Vector art generation and extended text capabilities; popular for design workflows.
    *   [**Reve Image 1.0**](https://reve.art/){target=_blank}: Newer entrant (2025) competing on prompt adherence.
    *   [**Riverflow 2.0 Pro**](https://llm-stats.com/leaderboards/best-ai-for-image-generation){target=_blank}: Leaderboard top-three (May 2026); strong all-rounder.

    **Open-source / open-weight:**

    *   [**Stable Diffusion 3.5**](https://stability.ai/news/introducing-stable-diffusion-3-5){target=_blank} (Stability AI): Major step forward over SD 3. Highly customizable, runs locally. Available on [HuggingFace](https://huggingface.co/stabilityai){target=_blank}.
    *   [**FLUX.1 Schnell / FLUX.1 dev**](https://bfl.ai/){target=_blank} (Black Forest Labs): Open-weight tiers of FLUX, Apache-licensed (Schnell) and non-commercial (dev). Strong baseline for self-hosting.
    *   [**HiDream-I1**](https://hidream.org/){target=_blank}: MIT-licensed, fully open.
    *   [**Qwen Image**](https://huggingface.co/Qwen){target=_blank} (Alibaba): Strong open-weight alternative with multilingual prompt support.

    !!! example "Synthetic data for downstream model training: storm damage assessment from drone imagery"

        Drone imagery for disaster-damage classification is hard to come by — major storms are infrequent, drones often can't fly during or immediately after, and labeled examples of severe damage are especially scarce. Multimodal image-editing models like Gemini 2.5 Flash Image (Nano Banana) can systematically expand a small seed dataset of real drone images into a much larger paired training set with controlled variation across damage severity, structure type, and environmental conditions.

        **Workflow**

        1. **Collect a seed dataset.** Start with a small set of real labeled nadir-view drone images — for example, 200 images of intact rural rooftops captured at known altitudes between 60–100 m AGL.

        2. **Generate damage variants per scene.** For each seed image, prompt Nano Banana to produce a paired set of damage variants while preserving the underlying scene:

            ```
            I'm uploading a nadir drone image of an intact rural metal-panel roof
            captured at ~80 m altitude. Generate four variants of the same scene at
            the same camera angle, lighting, and surrounding vegetation, varying
            ONLY the roof condition:

            1. Light damage: 1-2 panels lifted, debris scattered around the perimeter
            2. Moderate damage: ~30% of panels missing, some structural deformation
            3. Severe damage: ~70% of panels missing, partial wall collapse on one side
            4. Total loss: roof completely removed, exposed framing and interior visible

            Maintain consistent perspective, vegetation, time of day, and shadow
            direction across all four variants so they form a paired training set.
            ```

        3. **Generate environmental variants.** For each seed-plus-damage combination, vary lighting, weather, and seasonal conditions to teach the downstream model invariances:

            ```
            Take this drone image and generate four variants for: overcast midday,
            golden-hour side-lit, low-altitude haze after rainfall, and partial cloud
            shadow. Keep the roof condition, structure, and surrounding vegetation
            identical across all four.
            ```

        4. **Generate structure-type diversity.** Use multi-image fusion to combine your scene templates with different roof morphologies (residential gable, commercial flat, agricultural barn) while preserving the damage signatures from step 2.

        5. **Train your downstream classifier** (e.g., YOLOv8 for object detection, ResNet or a vision transformer for damage-class scoring) on the combined real + synthetic dataset. **Reserve a real-only test set** for honest evaluation.

        **Why Nano Banana fits this workflow**

        - **Scene consistency across edits** means damage variants share the same underlying structure, giving cleanly paired before/after training examples — hard to do with standalone txt2img models.
        - **Multi-image fusion** lets you blend a real scene with a reference damage example to produce hybrids that retain your scene's geometry.
        - **Conversational refinement** lets you iterate on a single variant ("more debris around the eaves," "less smoke on the right side") instead of re-rolling from scratch.
        - **Low cost per image** (~$0.039 via API) makes augmenting a 200-image seed into a 10,000-image training set tractable (~$390).
        - **Automatic SynthID watermarking** is invisible but detectable — important for documenting the synthetic provenance of every generated image in your training corpus.

        **Caveats and methodological hygiene**

        - **Validate on real data only.** Synthetic data narrows your training distribution in ways that often don't show up at training time. Always reserve a real-only test split, and report performance on it separately.
        - **Domain gap.** Generated imagery can miss sensor-specific artifacts (rolling shutter, lens distortion, sensor noise, JPEG compression). Models trained heavily on synthetic data sometimes overfit to "synthetic-looking" features and degrade on real deployment.
        - **Bias amplification.** If your seed images skew toward one geography, structure type, season, or altitude, synthetic variants amplify that skew. Audit class balance and sub-population coverage after augmentation.
        - **Disclosure.** If you publish a model trained on synthetic data, document the generation workflow, prompt templates, sample sizes, and SynthID provenance in your methods section. Some journals and conferences now require it.
        - **Validation against ground truth.** For high-stakes deployments (insurance estimation, FEMA damage assessment, search-and-rescue prioritization), pair synthetic augmentation with physics-based scene synthesis or labeled real datasets like [xBD](https://xview2.org){target=_blank} (building damage from satellite imagery) and [LADI](https://github.com/LADI-Dataset/ladi-overview){target=_blank} (low-altitude disaster imagery).

        For the broader synthetic-data discussion in earth observation and disaster response, see also [Veo 3](https://deepmind.google/technologies/veo/){target=_blank} for video augmentation and physics-based CGI pipelines for defensible ground truth.

    ## **Video Generation Models**

    Video generation AI has advanced rapidly with several platforms offering text-to-video and image-to-video capabilities:

    **Commercial Platforms:**

    *   [**Sora**](https://openai.com/sora){target=_blank} (OpenAI): Text-to-video with native audio. Available to ChatGPT Plus/Pro subscribers. Not available in EU/UK.
    *   [**Veo**](https://deepmind.google/models/veo/){target=_blank} (Google): High-quality video with native audio. Available via Gemini API and Google AI Studio.
    *   [**Runway**](https://runwayml.com/){target=_blank}: Professional video tools with world consistency features.
    *   [**Pika**](https://pika.art/){target=_blank}: Keyframe-based video creation.
    *   [**Kling AI**](https://klingai.com/){target=_blank}: Strong motion handling.
    *   [**Luma**](https://lumalabs.ai/dream-machine){target=_blank}: Fast generation with draft mode.

    **Avatar and Presenter Platforms:**

    *   [**HeyGen**](https://www.heygen.com/){target=_blank}: AI avatars with multilingual support.
    *   [**Synthesia**](https://www.synthesia.io/){target=_blank}: AI avatars with dubbing capabilities.
    *   [**Hedra**](https://www.hedra.com/){target=_blank}: Full-body animation with speech.

    **Open-Source Options:**

    *   [**Hunyuan Video**](https://aivideo.hunyuan.tencent.com/){target=_blank} (Tencent): Large open-source model on GitHub/HuggingFace.
    *   [**Stable Video**](https://stability.ai/stable-video){target=_blank} (Stability AI): Open-source video generation.
    *   [**Mochi**](https://www.genmo.ai/){target=_blank} (Genmo): Apache 2.0 licensed.

    ## **Related Capabilities**

    **Image and Video Understanding:**

    *   [Segment Anything Model (SAM 2)](https://segment-anything.com/){target=_blank} (Meta): Image and video segmentation
    *   [CLIP](https://openai.com/research/clip){target=_blank} (OpenAI): Vision-language understanding
    *   [LLaVA](https://llava-vl.github.io/){target=_blank}: Open-source visual instruction tuning

    **3D Generation:**

    *   [DreamGaussian](https://dreamgaussian.github.io/){target=_blank}: Text/image to 3D
    *   [Meshy](https://www.meshy.ai/){target=_blank}: Text to 3D mesh generation
    *   [Luma Genie](https://lumalabs.ai/genie){target=_blank}: Text to 3D model generation

---

## Additional Platforms & Resources

### Open Source & Self-Hosted

!!! note "Pricing for tools below not re-verified May 2026 — check vendor pages."

| **Platform** | **Description** | **Cost** | **Link** |
|--------------|-----------------|----------|----------|
| **Amplify GenAI** | Open source multi-model platform from Vanderbilt | AWS usage + model costs (~$3/user/mo) | [**Amplify GenAI**](https://www.amplifygenai.org/){target=_blank} / [**GitHub**](https://github.com/gaiin-platform){target=_blank} |
| **Ollama** | Run LLMs locally | Free | [**Ollama**](https://ollama.com/){target=_blank} |
| **LM Studio** | Desktop app for local LLMs | Free | [**LM Studio**](https://lmstudio.ai/){target=_blank} |

---

## Educational AI Platforms

!!! note "Pricing for tools below not re-verified May 2026 — check vendor pages."

These platforms provide AI-powered tutoring and learning support across various subjects:

| **Platform** | **Subject Areas** | **Target Audience** | **Pricing** | **Key Features**  |
| :----------- | :---------------- | :------------------ | :---------- | :---------------- |
| [**IXL**](https://www.ixl.com/){target=_blank}  | Math, Language Arts, Science, Social Studies, Spanish | Pre-K to 12th Grade | $9.95/mo (single subject), $19.95/mo (all subjects) | Personalized learning, adaptive questions, real-time diagnostics, progress tracking |
| [**Khan Academy**](https://www.khanacademy.org/){target=_blank} | Math, Science, Economics, Arts & Humanities, Computing, Test Prep | K-12, College, Adults | Free | Video lessons, practice exercises, personalized dashboard, progress tracking |
| [**Duolingo**](https://www.duolingo.com/){target=_blank} | Languages (40+ languages) | All ages  | Free (Duolingo Plus for premium) | Gamified learning, bite-sized lessons, spaced repetition, pronunciation practice |
| [**Quizlet**](https://quizlet.com/){target=_blank} | User-Generated Content (all subjects) | All ages | Free (Quizlet Plus for premium)  | Flashcards, study games, practice tests, AI-powered study sets |
| [**EdX**](https://www.edx.org/){target=_blank} | University-Level Courses | Adults, Professionals | Free to audit, paid certificates | Courses from top universities, professional certificates, MicroMasters, online degrees |
| [**Coursera**](https://www.coursera.org/){target=_blank} | University-Level Courses | Adults, Professionals | Free to audit, paid certificates  | Courses from leading universities, specializations, professional certificates, degrees |
| [**Google Career Certificates**](https://grow.google/certificates/){target=_blank} | Data Analytics, Cybersecurity, IT, Project Management, UX, Marketing, AI | Adults, Career Changers | $49/mo via Coursera, 7-day free trial | Industry-recognized certificates, no degree required, 3-6 month completion, access to Employer Consortium (150+ companies) |
| [**Udemy**](https://www.udemy.com/){target=_blank} | Skills-Based Courses (business, tech, personal development) | Adults, Professionals | Courses priced individually  | Wide range of topics, frequent discounts, lifetime access to purchased courses |
| [**MasterClass**](https://www.masterclass.com/){target=_blank} | Expert-Led Courses (creative, professional skills) | Adults | $120/year (individual), $180/year (duo), $240/year (family)  | Video lessons from renowned experts, downloadable workbooks, community access |
| [**Codecademy**](https://www.codecademy.com/){target=_blank} | Programming, Data Science, Web Development | Teens, Adults | Free (basic), Pro: $239.88/year or $39.99/mo | Interactive coding lessons, projects, quizzes, skill paths, career paths |
| [**Brilliant**](https://brilliant.org/){target=_blank} | Math, Science, Computer Science | Teens, Adults | $149/year or $24.99/mo | Interactive problem-solving, conceptual understanding, guided learning paths |
| [**Google Classroom**](https://edu.google.com/products/classroom/){target=_blank} | Platform for any subject | K-12, Higher Education | Free for schools using Google Workspace | Assignment distribution, grading, integration with Google services |
| [**Kahoot**](https://kahoot.com/){target=_blank} | Gamified content for any subject | K-12, Higher Education, Corporate | Free (basic), paid plans for features | Game-based learning, quizzes, trivia, real-time engagement |
| [**Grammarly**](https://www.grammarly.com/grammar-check){target=_blank} | Writing improvement | K-12, Higher Education, Professionals | Free (basic), paid plans | AI writing assistant, grammar checking, style suggestions, tone detection |

For more information on using AI for tutoring and education, see [AI Tutoring: Student's Guide](tutoring.md).

---

## Important Notes

!!! Info "About This Guide"

    * **Verification Date:** All pricing verified May 2026
    * **Updates:** AI platforms change rapidly. Check official websites for current pricing
    * **Free Tiers:** Many services offer free tiers with usage limits
    * **Student Discounts:** Check for education pricing (Perplexity, Google AI Pro, GitHub Copilot, etc.)
    * **API vs Subscription:** Some platforms offer both subscription and pay-per-use API options

!!! Warning "⚠️ Deprecated/Archived Platforms"

    * **SearchGPT** - Merged into ChatGPT (no longer standalone)
    * **Code Llama** - Repository archived July 2025 (consider StarCoder instead)
    * **DALL-E 3** - Sunset May 2026 (replaced by GPT Image 1.5 / GPT Image 2)

!!! Tip "Best Options for Students & Educators"

    **Free/Low-Cost:**

    * **GitHub Copilot** - Free for students, teachers, OSS maintainers
    * **Perplexity Education** - $10/mo with SheerID verification
    * **Google AI Pro** - Free for university students (1 year)
    * **Khan Academy** - Completely free

    **Best Value Paid:**

    * **ChatGPT Plus** - $20/mo (good all-rounder)
    * **Claude Pro** - $20/mo (excellent for research and writing)
    * **Gemini AI Pro** - $19.99/mo (great multimodal capabilities)

**Security & Research Considerations:** For research use, consult your institution's AI policies. Some platforms (DeepSeek, Qwen) have restrictions for US-based researchers. See [Important Restrictions](#important-restrictions-for-us-based-researchers) below for details.

---

## Agentic Browsers (AI-Powered Web Browsers)

Agentic browsers integrate AI directly into your web browsing experience, enabling autonomous task execution, intelligent search, and productivity enhancements.

!!! note "Pricing for tools below not re-verified May 2026 — check vendor pages."

| **Browser**  | **Plan** | **Price (per month)** | **Details**  |
| :----------- | :------- | :-------------------- | :----------- |
| [**Perplexity Comet**](https://www.perplexity.ai/comet){target=_blank} | [Free](https://comet.perplexity.ai/){target=_blank} | $0 | AI-powered browser with sidecar assistant, Perplexity AI search, tab management, content summarization |
| | Perplexity Max | $200 | Background Assistant for multi-tasking, autonomous task execution (booking flights, sending emails), mission control dashboard |
| [**Dia Browser**](https://www.diabrowser.com){target=_blank} | [Free Beta](https://browserco.typeform.com/to/i6CycxSu){target=_blank} | $0 (Invite-only) | AI-first browser, URL bar = AI chat, tab conversations, Skills system, browsing history context (opt-in) <br> **macOS 14+ M1+ only** |
| | [Dia Pro](https://www.diabrowser.com){target=_blank} | $20 | Unlimited AI chat and Skills, multi-step reasoning, task automation <br> **Acquired by Atlassian ($610M)** |
| [**Fellou**](https://fellou.ai){target=_blank} | [Free](https://fellou.ai/pricing){target=_blank} | $0 | 1,000 Sparks (~4 tasks), Deep Search, autonomous web actions, Shadow Workspace for background tasks |
| | [Plus](https://fellou.ai/pricing){target=_blank} | $19 | 2,000 Sparks (~8 tasks), 3 scheduled tasks, priority support |
| | [Pro](https://fellou.ai/pricing){target=_blank} | $39.90 | 5,000 Sparks (~20 tasks), 5 scheduled tasks, Image/Code/Music agents |
| | [Ultra](https://fellou.ai/pricing){target=_blank} | $199.90 | Unlimited Sparks, unlimited scheduled/concurrent tasks, exclusive support |
| [**Opera Neon**](https://www.operaneon.com/){target=_blank} | [Subscription](https://www.operaneon.com/){target=_blank} | $19.99 (Waitlist) | Neon Do (autonomous browsing), Neon Make (AI creation), Cards system, Tasks workspaces, local processing |
| [**Genspark AI Browser**](https://www.genspark.ai){target=_blank} | [Free](https://www.genspark.ai/pricing){target=_blank} | $0 | 100 credits daily, Super Agent Everywhere, Autopilot Mode, 700+ MCP tool integrations |
| | [Plus](https://www.genspark.ai/pricing){target=_blank} | $24.99 | 10,000 credits monthly, priority AI agent access, top-tier models, AI Slides/Sheets/Docs |
| | [Pro](https://www.genspark.ai/pricing){target=_blank} | $249.99 | 125,000 credits monthly, full Super Agent access, phone calls, video generation |
| [**Google Chrome + Gemini**](https://gemini.google/overview/gemini-in-chrome/){target=_blank} | [Free](https://www.google.com/chrome/){target=_blank} | $0 | Gemini side panel (right rail), page summarization, cross-tab Q&A, in-browser Nano Banana image transformation, voice-driven browsing <br> **Free with any Google account** |
| | [Google AI Pro](https://gemini.google.com/){target=_blank} | $19.99 | **Auto Browse** (launched Jan 2026): agentic multi-step tasks — shopping, form filling, hotel/flight research, scheduling, subscription management. Personal Intelligence (calendar/email) rolling out <br> **US-only at launch** |
| | [Google AI Ultra](https://gemini.google.com/){target=_blank} | $249.99 | Higher Auto Browse limits, Gemini 3 Pro/Ultra access for deeper reasoning on agentic tasks |
| [**Microsoft Edge Copilot Mode**](https://www.microsoft.com/edge){target=_blank} | [Free (Experimental)](https://www.microsoft.com/en-us/edge/features/copilot){target=_blank} | $0 | Cross-tab awareness, task automation, in-page assistance, browser history/credentials access <br> **Windows/Mac, opt-in** |
| [**Opera One + Aria**](https://www.opera.com/features/aria){target=_blank} | [Free](https://www.opera.com/){target=_blank} | $0 | Free AI assistant, real-time web access, page context mode, image generation, tab commands, local AI models <br> **No account required** |
| [**Brave + Leo AI**](https://brave.com/leo/){target=_blank} | [Free](https://brave.com/){target=_blank} | $0 | Privacy-first AI, Llama, Mixtral, Claude Haiku, Qwen, content awareness, zero data retention |
| | Leo Premium | Varies | Claude Sonnet, DeepSeek reasoning models, Bring Your Own Model (BYOM) |

**Notes on Agentic Browsers:**

*   **True Agentic Capabilities:** Comet, Fellou, Opera Neon, Dia, Genspark, and Google Chrome (Auto Browse, AI Pro/Ultra) can autonomously perform multi-step tasks (booking, purchasing, form filling)
*   **AI-Enhanced:** Microsoft Edge Copilot Mode, Opera One, and Brave Leo provide AI assistance but with less autonomous action
*   **Major-vendor entry:** Google Chrome added agentic Auto Browse in January 2026, bringing autonomous web tasks into the world's most-used browser. Requires Google AI Pro or Ultra; US-only at launch.
*   **Platform Availability:** Most are Chromium-based; Dia is macOS only (M1+); Others support Windows/Mac/Linux
*   **Privacy Considerations:** Check each browser's data policies - some use cloud AI, others offer local processing

---

## API Pricing for Developers

For developers building with AI APIs, here's detailed token-level pricing:

!!! note "Cloud platform pricing (Together AI, Replicate, etc.) not re-verified May 2026 — check vendor pages."

| **Service**  | **Plan** | **Pricing** | **Details**  |
| :----------- | :------- | :---------- | :----------- |
| [**Claude API**](https://console.anthropic.com/){target=_blank} | Pay-As-You-Go | Varies by tier | **Opus tier** (most capable, highest cost), **Sonnet tier** (balanced), **Haiku tier** (fastest, cheapest). Batch: 50% discount, Prompt caching: substantial savings. Check [pricing page](https://www.anthropic.com/pricing){target=_blank} for current rates. |
| [**Gemini API**](https://aistudio.google.com/){target=_blank} | Pay-As-You-Go | Varies by tier | **Pro tier** (most capable), **Flash tier** (balanced), **Flash-Lite tier** (cheapest). Batch: 50% discount. Check [pricing page](https://ai.google.dev/pricing){target=_blank} for current rates. |
| [**OpenAI API**](https://platform.openai.com/){target=_blank} | Pay-As-You-Go | Varies by tier | Flagship GPT models, smaller/cheaper "mini" variants, and reasoning ("o-series") models at premium pricing. Check [pricing page](https://openai.com/api/pricing/){target=_blank} for current rates. |
| [**Mistral API**](https://console.mistral.ai/){target=_blank} | Pay-As-You-Go | Varies by tier | Large/Medium/small general models plus specialized variants (e.g., Codestral for code). Check [pricing page](https://mistral.ai/technology/#pricing){target=_blank} for current rates. |
| [**DeepSeek API**](https://platform.deepseek.com/){target=_blank} | Pay-As-You-Go | Significantly cheaper than US frontier APIs | Chat and reasoning model tiers. ⚠️ **NOT ALLOWED for US researchers** — see restrictions below. Check [pricing page](https://api-docs.deepseek.com/quick_start/pricing){target=_blank} for current rates. |
| [**Cohere API**](https://cohere.com/){target=_blank} | Pay-As-You-Go | Varies by tier | Command (general), Command R+ (premium), and Command-light (cheapest) tiers. Check [pricing page](https://cohere.com/pricing){target=_blank} for current rates. |
| [**Together AI**](https://www.together.ai/){target=_blank} | Serverless | Pay-As-You-Go | Text/Vision: $0.02-$3.50/1M tokens <br> Images: $0.0027-$0.08/MP <br> GPU Clusters: $1.76-$5.50/GPU hr |
| [**Groq**](https://groq.com/){target=_blank} | Developer | Pay-As-You-Go | 10x rate limits vs free, 50% batch discount |
| [**Replicate**](https://replicate.com/){target=_blank} | Pay-As-You-Go | Varies | CPU: $0.36/hr <br> T4 GPU: $0.81/hr <br> 8x H100: $43.92/hr |
| [**Amazon Bedrock**](https://aws.amazon.com/bedrock/){target=_blank} | On-Demand | Varies | Multi-model platform (Claude, Llama, etc.) - model-specific pricing |
| [**Google Vertex AI**](https://cloud.google.com/vertex-ai){target=_blank} | On-Demand | Varies | 130+ models - refer to Gemini API pricing + model-specific costs |
| [**Azure AI Studio**](https://ai.azure.com/){target=_blank} | On-Demand | Varies | GPT, Claude, Llama, Mistral - refer to OpenAI API pricing + Azure markup |

---

## ⚠️ Important Restrictions for US-Based Researchers

### **DeepSeek AI - Federal and State Restrictions**

**PAID CLOUD SERVICE NOT ALLOWED:**

DeepSeek's paid API and cloud services are **prohibited** for US-based researchers at many institutions due to:

**Federal Restrictions:**

- [**H.R. 1121**](https://www.congress.gov/bill/119th-congress/house-bill/1121){target=_blank} - "No DeepSeek on Government Devices Act" (Introduced Feb 2025)

- [**House Select Committee Report**](https://selectcommitteeontheccp.house.gov/media/reports/deepseek-unmasked-exposing-ccps-latest-tool-spying-stealing-and-subverting-us-export){target=_blank} - "DeepSeek Unmasked: Exposing the CCP's Latest Tool For Spying, Stealing, and Subverting U.S. Export Control Restrictions"

- **Federal Agency Bans:** NASA, U.S. Navy, Department of Defense (DOD), Department of Commerce have banned DeepSeek

- **Owned by High-Flyer** (Chinese company with CCP control)

- **Data stored in China** and accessible to Chinese government

- **Content manipulation** to align with CCP propaganda

**State-Level Bans:**

- [**Texas**](https://gov.texas.gov/news/post/governor-abbott-announces-ban-on-chinese-ai-social-media-apps){target=_blank} (Jan 31, 2025), [**Virginia**](https://www.governor.virginia.gov/newsroom/news-releases/2025/february/name-1040839-en.html){target=_blank} (Feb 11, 2025), [**New York**](https://www.governor.ny.gov/news/governor-hochul-issues-statewide-ban-deepseek-artificial-intelligence-government-devices-and){target=_blank} (Feb 10, 2025)

- Additional states: Iowa, South Dakota, Kansas, Tennessee, North Carolina, Nebraska, Arkansas, North Dakota, Oklahoma, Alabama, Georgia

**University Bans:**

- All Virginia public universities ([George Mason](https://its.gmu.edu/bulletins/deepseek-ai-ban-on-university-devices-and-networks/){target=_blank}, [UVA](https://www.cavalierdaily.com/article/2025/02/in-compliance-with-youngkin-order-university-bans-use-of-deepseek-ai-on-networks){target=_blank}, [Virginia Tech](https://news.vt.edu/notices/2025/02/it-deepseek-restriction-executive-order.html){target=_blank}, [William & Mary](https://www.wm.edu/offices/it/announcements/deepseek-ai-no-longer-permitted-on-wm-wireless-network-devices.php){target=_blank}, [JMU](https://www.jmu.edu/news/computing/2025/02-12-deepseek-executive-order.shtml){target=_blank})

- North Dakota University System

**SELF-HOSTED OPEN-SOURCE MAY BE PERMITTED:**

Open-source DeepSeek models can be downloaded and run **on-premises**, but researchers MUST:

- ✅ Check with institutional IT and security teams first

- ✅ Ensure compliance with federal grant requirements (NSF, DOD, DOE)

- ✅ Never upload sensitive, proprietary, or controlled data

- ✅ Document usage for research security compliance

---

### **Qwen (Alibaba) - Data Sovereignty Concerns**

**NOT SPECIFICALLY BANNED, BUT NOT RECOMMENDED:**

Qwen is **not subject to specific federal bans** like DeepSeek, but has serious concerns for US researchers:

**Key Issues:**

- **Owned by Alibaba** (Chinese company subject to CCP control)

- **Data stored in China** under Chinese data sovereignty laws

- **No GDPR compliance** or EU data protection representative

- **Potential surveillance** under Chinese national security laws

- **Congressional scrutiny** (Senators urged sanctions in 2023, not yet implemented)

**Regulatory Framework:**

- [**NSF Research Security**](https://www.nsf.gov/notices/important/important-notice-no-149-updates-nsf-research-security/in149){target=_blank} - Requires disclosure of foreign support and affiliations

- [**Treasury Outbound Investment Restrictions**](https://home.treasury.gov/news/press-releases/jy2687){target=_blank} - Limits US investments in Chinese AI companies (affects funding, not use)

- **No Entity List designation** (as of Oct 2025)

**SELF-HOSTED OPEN-SOURCE MAY BE PERMITTED:**

Qwen's Apache 2.0 licensed models (40M+ downloads on HuggingFace) can be run **on-premises**, but researchers MUST:

- ✅ Check with institutional IT and security teams first

- ✅ Verify compliance with federal grant terms

- ✅ Avoid uploading to Chinese cloud services

- ✅ Document AI tool usage in research security plans

---

### **Recommendations for Researchers**

**✅ SAFE FOR RESEARCH (US-based alternatives):**

- OpenAI (ChatGPT, GPT API) - US company

- Anthropic (Claude) - US company

- Google (Gemini) - US company

- Microsoft (Copilot) - US company

- Mistral AI - French company (EU-based)

- Cohere - Canadian company

**⚠️ USE WITH EXTREME CAUTION (Chinese companies):**

- DeepSeek - **BANNED at many institutions**

- Qwen - Not banned, but data sovereignty concerns

- Check institutional policies BEFORE use

**✅ SELF-HOSTED OPEN-SOURCE (May be acceptable):**

- Meta Llama (US company, Apache 2.0)

- DeepSeek open-source (with institutional approval)

- Qwen open-source (with institutional approval)

- Mistral open-source (EU company, Apache 2.0)

**ALWAYS:**

1. Check your institution's AI usage policy

2. Review federal grant terms (NSF, NIH, DOD, DOE)

3. Consult with IT security and research compliance offices

4. Never share sensitive, proprietary, or controlled data with foreign AI services

5. Document all AI tool usage for research security requirements

---
