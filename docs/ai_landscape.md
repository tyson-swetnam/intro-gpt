## AI Landscape

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! info "A Glance at the Generative AI Landscape (2024-2025)"

    The field of Generative AI is rapidly evolving. This section provides a snapshot of some of the most influential models and platforms as of early 2024, with a look towards what we might expect in 2025.

    [![tree](assets/tree.jpeg){width=800}](https://arxiv.org/abs/2304.13712){target=_blank}
    
    Image Credit: [Yang et al. :simple-arxiv:](https://arxiv.org/abs/2304.13712){target=_blank} (While this image depicts the state of LLMs in 2023, it effectively illustrates the foundational models and their evolution)

**Table**: Dominant LLM and Multimodal Models in Public Use (2024-2025)

| Name                                    | Creator                     | Application             | Access                       | Publications                                                                                                                                                |
| --------------------------------------- | --------------------------- | ----------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [:llama: LLaMA 3](https://llama.meta.com/llama3/){target=_blank}      | [:simple-meta: Meta](https://ai.meta.com/)      | LLM, Research           | Open Source                  | [:simple-github: meta-llama/llama3](https://github.com/meta-llama)                                                                                    |
| [Gemini 1.5 Pro](https://ai.google.dev/models/gemini){target=_blank}       | [:simple-google: Google](https://deepmind.google/)      | LLM, Multimodal, Search, Chat | Free, Subscription           | [:simple-arxiv: Gemini Team (Google)](https://www.google.com/url?sa=E&source=gmail&q=https://arxiv.org/abs/2312.11805) |
| [:material-microsoft-copilot: Copilot](https://copilot.microsoft.com/){target=_blank} | [:simple-microsoft: Microsoft](https://www.microsoft.com/en-us/ai) | Productivity, Search, Chat | Free, Subscription | [:simple-arxiv: Microsoft Copilot Research](https://www.google.com/url?sa=E&source=gmail&q=https://arxiv.org/search/?query=microsoft%2Bcopilot%2Bresearch&searchtype=all&abstracts=show&order=-announced_date_first&size=50)                                                                                                    |
| [ChatGPT (GPT-4)](https://openai.com/gpt-4){target=_blank}         | [:simple-openai: OpenAI](https://openai.com/)      | Chat, Multimodal        | Free (GPT-3.5), Subscription (GPT-4) | [:simple-arxiv: OpenAI GPT-4](https://www.google.com/url?sa=E&source=gmail&q=https://arxiv.org/abs/2303.08774)                                          |
| [Claude 3](https://www.anthropic.com/news/claude-3-family){target=_blank}         | [:simple-anthropic: Anthropic](https://www.anthropic.com)      | Chat        | Free, Subscription | [Anthropic Claude 3](https://www.google.com/url?sa=E&source=gmail&q=https://www.anthropic.com/news/claude-3-family)                                          |
| [DALL·E 3](https://openai.com/dall-e-3){target=_blank}         | [:simple-openai: OpenAI](https://openai.com/)      | Computer Vision, Chat   | Via ChatGPT Plus, API       | [:simple-openai: DALL-E 3 Paper](https://www.google.com/url?sa=E&source=gmail&q=https://cdn.openai.com/papers/dall-e-3.pdf)     |
| [Sora](https://openai.com/sora) | [:simple-openai: OpenAI](https://openai.com/)      | Text-to-video, Image-to-video   | Limited access       | [:simple-openai: Sora Technical Report](https://www.google.com/url?sa=E&source=gmail&q=https://openai.com/research/video-generation-models-as-world-simulators)     |
| [Stable Diffusion 3](https://stability.ai/news/stable-diffusion-3) | [:simple-stabilityai: Stability AI](https://stability.ai/) | Computer Vision | Open Source, API | [:simple-arxiv: Stable Diffusion 3 Paper](https://www.google.com/url?sa=E&source=gmail&q=https://arxiv.org/abs/2303.14686) |
| [Midjourney v6](https://www.midjourney.com/){target=_blank}     | [:simple-midjourney: Midjourney](https://www.midjourney.com/)  | Computer Vision         | Subscription                 | [Midjourney Documentation](https://www.google.com/url?sa=E&source=gmail&q=https://docs.midjourney.com/)                                                               |
| [GitHub Copilot](https://github.com/features/copilot){target=_blank} | [:simple-github: GitHub](https://github.com/)       | Code Generation         | Subscription                 | [:simple-github: GitHub Copilot Research](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/features/copilot)                           |

**Notes on the Table:**

*   **LLaMA 3:** Meta's LLaMA 3 is a significant open-source model that is highly competitive and driving innovation.
*   **Gemini:** Google's Gemini (formerly Bard) is rapidly evolving and positioned as a strong competitor to GPT-4, particularly in multimodal capabilities.
*   **Copilot:** Microsoft's Copilot (integrating OpenAI's technology) has become ubiquitous, especially for productivity and search.
*   **Claude 3:** Anthropic's Claude 3 is gaining popularity due to its strong performance on reasoning tasks and commitment to AI safety.
*   **Sora:** Although it is not yet fully accessible, OpenAI's text-to-video model has the potential to be a major innovation.
*   **Image Generation:** DALL-E 3, Stable Diffusion 3, and Midjourney v6 are leading the way in image generation, each with its strengths (photorealism, open-source nature, artistic style).
*   **GitHub Copilot:** Remains a dominant force in code generation and is increasingly integrated into developers' workflows.

## Image and Video Analysis

??? Tip "Stable Diffusion, Image, and Video Generation Models (2024-2025)"

    **Stable Diffusion 3**

    [Stable Diffusion 3](https://stability.ai/stable-diffusion-3){target=_blank} is the latest iteration of the popular open-source text-to-image model developed by [Stability AI](https://stability.ai/){target=_blank}. It builds upon the advancements of previous versions, offering improved image quality, more accurate adherence to prompts, and enhanced capabilities for generating complex scenes and details.

    Stable Diffusion models are available via [HuggingFace](https://huggingface.co/stabilityai){target=_blank}, [GitHub](https://github.com/Stability-AI/StableDiffusion3){target=_blank} and through various APIs and user interfaces.

    Diffusion models have two modes, forward and reverse. Forward diffusion adds random noise until the image is lost. Reverse diffusion uses Markov Chains to recover data from a Gaussian distribution, thereby gradually removing noise.

    Stable Diffusion relies upon [Latent Diffusion Model (LDM) :simple-arxiv:](https://arxiv.org/abs/2112.10752){target=_blank}

    **Other Notable Image Generation Models**

    *   [DALL·E 3](https://openai.com/dall-e-3){target=_blank} (OpenAI) is known for its photorealistic image generation and ability to understand complex prompts. It's integrated into ChatGPT Plus and available through an API.
    *   [Midjourney v6](https://www.midjourney.com/){target=_blank} is highly regarded for its artistic and stylized image generation. It's accessible through a Discord interface and requires a subscription.
    *   [Imagen 2](https://deepmind.google/technologies/imagen-2/){target=_blank} (Google): Not directly accessible to the public, but notable for its photorealistic text-to-image generation capabilities.
    *   [Adobe Firefly](https://www.adobe.com/products/firefly.html){target=_blank} is integrated into the Adobe Creative Cloud suite of applications and is geared toward enterprise creative workflows.

    **Video Generation Models**

    *   [Sora](https://openai.com/sora){target=_blank} (OpenAI) has generated significant excitement for its ability to create realistic and imaginative videos from text prompts. It is currently available on a limited basis.
    *   [Runway Gen-2](https://runwayml.com/){target=_blank} allows for text-to-video, image-to-video, and video-to-video editing. It's popular among video creators for its accessibility and range of features.
    *   [Pika Labs](https://www.pika.art/){target=_blank} is an additional option that allows for text-to-video generation and editing.
    *   [Stable Video Diffusion](https://stability.ai/news/introducing-stable-video-diffusion-generating-videos-from-images-with-svd-and-svd-xt){target=_blank} is an image-to-video diffusion model that allows users to generate short video clips based on a still image input.

    **Image and Video Segmentation**

    [Segment Anything (Meta)](https://segment-anything.com/){target=_blank}, [Kirillov et al. :simple-arxiv:](https://doi.org/10.48550/arXiv.2304.02643){target=_blank}, is a powerful image segmentation technology that allows you to isolate objects within images with high precision.

    **Emerging Trends in Image and Video Analysis**

    *   **Multimodal Integration:** Combining image/video analysis with other modalities (text, audio) for a more holistic understanding of content.
    *   **3D Scene Generation:**  Generating 3D models and environments from images and videos.
    *   **Real-time Analysis:**  Performing image and video analysis in real-time for applications like augmented reality and live video processing.

??? Info "Understanding Embeddings"

    [What are Embeddings? - Vicki Boykis](https://vickiboykis.com/what_are_embeddings/){target=_blank} - [download PDF :fontawesome-regular-file-pdf:](https://raw.githubusercontent.com/veekaybee/what_are_embeddings/main/embeddings.pdf)
    
    Embeddings are a way to represent data (words, images, etc.) as numerical vectors in a multi-dimensional space. These vectors capture semantic relationships between data points, meaning similar items are located closer together in the embedding space.

    Embedded space for geospatial applications:
    
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Visualizing how embeddings can organize satellite imagery. Millions of points covering the state of Alabama move between their geographic position and their location in the embedding space. <a href="https://t.co/Z6FtoMQ84B">pic.twitter.com/Z6FtoMQ84B</a></p>&mdash; Caleb Kruse (@clkruse) <a href="https://twitter.com/clkruse/status/1658131846121803777?ref_src=twsrc%5Etfw">May 15, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    Embedded space for natural language:

    [Credit: Stephen Wolfram](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/){target=_blank}

    [![wolfram](https://content.wolfram.com/uploads/sites/43/2023/02/hero3-chat-exposition.png)](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)

    **Why are Embeddings Important?**

    *   **Machine Learning:** Embeddings are essential for training machine learning models, as they provide a way to represent complex data in a format that algorithms can understand.
    *   **Semantic Search:**  Embeddings enable semantic search, where you can find information based on meaning rather than just keyword matching.
    *   **Recommendation Systems:** Embeddings help power recommendation systems by identifying items with similar characteristics.
    *   **Data Visualization:**  Embeddings can be used to visualize relationships between data points in a lower-dimensional space.

## Programmer Q/A

[Phind.com](https://phind.com){target=_blank} - is a search engine optimized for developers and technical questions with simple explanations and relevant code snippets from the web, drawing from sources like [StackOverFlow](https://stackoverflow.com/){target=_blank}. Another great option is to use the coding features built in to models such as [Gemini](https://gemini.google.com){target=_blank}, [Claude](https://claude.ai/){target=_blank}, or [GitHub Copilot](https://github.com/features/copilot){target=_blank} directly.
