# The Landscape

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## The Generative AI Landscape in 2026

The generative AI landscape has transformed dramatically since the release of ChatGPT in November 2022. What began as text-generation models has exploded into a diverse ecosystem of platforms capable of creating text, images, video, code, and music—while also evolving from simple chatbots into sophisticated **agentic systems** that can autonomously complete complex tasks.

This page provides an overview of the generative AI landscape as of January 2026, focusing on three key perspectives:

1. **The Evolution of Foundation Models** - How we arrived at today's capable AI systems
2. **Platform Comparison** - Choosing the right tool for your needs
3. **The Age of Agentic AI** - How AI has evolved from conversation to autonomous action

---

## Evolution of Foundation Models

### The LLM Family Tree (2018–2026)

[![tree](assets/tree.jpeg){width=800}](https://arxiv.org/abs/2304.13712){target=_blank}

Image Credit: [Yang et al. 2023 :simple-arxiv:](https://arxiv.org/abs/2304.13712){target=_blank} — historical lineage through early 2023.

This diagram traces the early lineage of large language models. Today's models (Claude, ChatGPT, Gemini, Llama, Qwen, DeepSeek, Mistral, Gemma, GPT-OSS) descend from these architectures. Key milestones:

- **2017**: [Transformer architecture](https://arxiv.org/abs/1706.03762){target=_blank} introduced ("Attention is All You Need")
- **2018–2019**: BERT and GPT-2 demonstrate transfer learning at scale
- **2020**: GPT-3 (175B parameters) shows few-shot learning at scale
- **2021–2022**: Model scaling continues (PaLM, GPT-3.5, ChatGPT launches Nov 2022)
- **2023**: Multimodal models emerge; Llama 2 ships open-weights; Bard (since rebranded as Gemini) launches; Mistral 7B released
- **2024**: Llama 3 family, Mistral Large, multimodal Claude and ChatGPT; **Model Context Protocol (MCP)** introduced by Anthropic in November
- **2025**: Reasoning-focused models (Claude reasoning, ChatGPT o-series, Gemini Deep Think); DeepSeek R1 open reasoning model; Qwen and Gemma family releases; OpenAI publishes open-weights **GPT-OSS**; agentic IDEs (Cursor, Claude Code, OpenCode, ClawCode) mature
- **2026**: Consolidation around tool use and agentic workflows, MCP ecosystem expansion, on-device + frontier models coexist; agentic browsers (Perplexity Comet, Dia, Fellou) reach broad availability

---

### From Text Generation to World Simulation

The evolution of generative AI has progressed through distinct phases:

**Phase 1: Text Generation (2018-2022)**

- Models like GPT-3 (2020), BERT, and T5 focused on understanding and generating text
- Primary use cases: chatbots, summarization, translation
- Interaction model: single-turn question-and-answer

**Phase 2: Multimodal Integration (2022-2024)**

- Models gained ability to process images, audio, and eventually video
- ChatGPT, Gemini, and Claude could analyze charts, diagrams, and photos
- Enabled new use cases: visual analysis, document understanding, accessibility

**Phase 3: Agentic Systems (2024-Present)**

- AI evolved from responding to acting
- Systems can now plan, use tools, and complete multi-step tasks autonomously
- Examples: Claude Code, GitHub Copilot Workspace, ChatGPT with Canvas

**Phase 4: Interactive World Models (Emerging)**

The frontier of generative AI research focuses on systems that not only generate content but simulate interactive environments:

**Self-Evolving AI Agents**

[![agent-taxonomy](https://cdn-uploads.huggingface.co/production/uploads/652ebdcc76365388909b06cf/r46yBos814XV5enSDompo.jpeg){width=700}](https://arxiv.org/abs/2508.07407){target=_blank}

Image: Self-Evolving Agent Taxonomy from [Fang et al. 2025 :simple-arxiv:](https://arxiv.org/abs/2508.07407){target=_blank}

Research is exploring agents that improve their own capabilities through experience, optimizing:

- **Behavior**: Learning better action strategies through reinforcement learning
- **Prompts**: Refining self-instructions iteratively
- **Memory**: Improving information storage and retrieval
- **Tool Use**: Learning when and how to leverage external capabilities
- **Collaboration**: Optimizing workflows across multiple specialized agents

For more on agentic AI systems, see our dedicated [Agentic AI documentation](agentic.md).

**Interactive Generative Video (IGV)**

[![igv-architecture](https://cdn-uploads.huggingface.co/production/uploads/64105a6d14215c0775dfdd14/5kPNXDj9LIsgShhFz5WSg.jpeg){width=700}](https://arxiv.org/abs/2504.21853){target=_blank}

Image: IGV System Architecture from [Yu et al. 2025 :simple-arxiv:](https://arxiv.org/abs/2504.21853){target=_blank}

Unlike traditional video generation (Sora, Runway), **Interactive Generative Video** systems generate video content that responds to user input in real-time—essentially creating playable worlds from text descriptions.

IGV systems combine five key modules:

| Module | Function | Challenge |
|--------|----------|-----------|
| **Generation** | Creates high-quality video frames | Real-time performance |
| **Control** | Handles user input (keyboard, mouse, natural language) | Open-domain control |
| **Memory** | Maintains temporal consistency | Long-term coherence |
| **Dynamics** | Simulates realistic physics | Accurate simulation |
| **Intelligence** | Makes autonomous decisions | Causal reasoning |

Applications include:

- **Gaming**: Procedurally generated worlds that respond to player actions
- **Embodied AI**: Robots training in safe, scalable simulated environments
- **Autonomous Driving**: Testing edge cases in synthetic scenarios
- **Education**: Interactive science simulations
- **Entertainment**: Choose-your-own-adventure video content

**Example: Genie 3 (Google DeepMind)**

[Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/){target=_blank} represents a breakthrough in interactive world models—capable of generating playable 3D environments from a single image or text description. Unlike traditional video generation that creates fixed sequences, Genie 3 produces controllable, interactive worlds where users can navigate and interact in real-time.

Key capabilities:

- **Image-to-World**: Upload a single image → explore it as a playable 3D environment
- **Text-to-World**: Describe a scene → generate an interactive world from scratch
- **Real-time Control**: WASD navigation, camera control, physics simulation
- **Temporal Consistency**: Maintains coherent world state across extended interactions

!!! info "Mote: Interactive Ecosystem Simulation"

    **[Mote](https://www.youtube.com/watch?v=Hju0H3NHxVI){target=_blank}** is an interactive ecosystem simulation that combines elements from games and research, creating a sandbox for computational biology, machine learning, and physics. It uses a custom GPU-based physics engine (1:07) to model many simple behaviors at a massive scale, leading to emergent phenomena.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Hju0H3NHxVI?si=V_W2ype1224ccRp2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## AI Platform Comparison

The AI landscape now includes dozens of platforms, each optimized for different use cases. Rather than duplicate extensive comparison tables here, we've consolidated all platform comparisons into a single comprehensive guide:

**📊 [Choosing the Right AI Platform](choose.md)** includes:

- **Platform Comparison Tables** by use case (Chat, Research, Code, Image/Video)
- **Agentic Browsers** - AI-powered web browsers (Perplexity Comet, Dia, Fellou, etc.)
- **API Pricing for Developers** - Token-level costs for Claude, Gemini, OpenAI, Mistral, etc.
- **Educational Platforms** - IXL, Khan Academy, Codecademy, Duolingo, and more
- **Student Discounts** - Special pricing for students and educators
- **Federal Restrictions** - Important compliance information for US-based researchers

All pricing verified **May 2026**.

### Quick Recommendations

**For Academic Research:**

- **Literature Review**: Perplexity, Claude, ScholarAI, Consensus
- **Data Analysis**: Claude (long-context), ChatGPT (Advanced Data Analysis)
- **Writing Assistance**: Claude (strong reasoning), ChatGPT Plus (plugins)
- **Citation Management**: NotebookLM (RAG capabilities)

**For Education:**

- **Students (Budget)**: Free options - HuggingFace Chat, Google AI Pro (1 yr free for verified students), Perplexity Education (discounted rate, see [choose.md](choose.md))
- **Teachers**: GitHub Copilot (free for educators), Claude (strong pedagogy), ChatGPT
- **Tutoring**: Khan Academy (free AI tutor Khanmigo), Claude, ChatGPT

**For Coding:**

- **IDE Integration**: [Claude Code](claude-code.md), GitHub Copilot, Cursor, OpenCode, ClawCode
- **Learning to Code**: ChatGPT (interactive execution), Replit AI
- **Code Review**: Claude (strong analysis), GitHub Copilot
- **See also**: Our [Vibe Coding guide](vibe.md) for detailed agentic coding workflows

**For Creative Work:**

- **Images**: Midjourney (quality), ChatGPT Image (convenience), Stable Diffusion (control)
- **Video**: Sora (OpenAI), Veo (Google), Runway
- **Music**: Suno, Udio
- **Writing**: Claude (creative writing), ChatGPT, Jasper (marketing)

---

## How AI Tools Are Accessed

The user experience for AI is changing fast. The same Claude or Gemini model is now reachable through a half-dozen surfaces, each with different trade-offs around convenience, privacy, file access, and how much autonomy you grant the AI. Most workshop participants will end up using more than one — knowing what each surface is good for is half the value of this workshop.

### Browser chat (the entry point)

Most people first meet AI in a web browser tab — [claude.ai](https://claude.ai), [chatgpt.com](https://chatgpt.com), [gemini.google.com](https://gemini.google.com), [perplexity.ai](https://www.perplexity.ai). Zero install, free tier, instant. The cost: every prompt and uploaded file leaves your machine and is processed by the vendor. Acceptable for non-sensitive work; check institutional and grant policies before uploading research data — see [Transparency](transparency.md) and [Legal](legal.md) for the questions to ask.

### Browser widgets, side-panels, and AI-native browsers

The next step is AI baked into the page you're already on:

- **Side-panel extensions** in Chrome / Edge / Firefox (Claude, ChatGPT, Perplexity, etc.) put a chat next to whatever you're reading
- **AI-native browsers** ([Perplexity Comet](https://www.perplexity.ai/comet), [Dia](https://www.diabrowser.com/), [Fellou](https://fellou.ai/), [Edge Copilot](https://www.microsoft.com/edge), [Brave Leo](https://brave.com/leo/)) build the assistant into the address bar and let it act on tabs
- **Search-with-AI** (Google AI Overviews, Bing Copilot, Perplexity) reshapes web search itself

### IDE extensions and plugins

For developers, the most common surface is an extension inside the editor:

- **[GitHub Copilot](copilot.md)** — the original; ships in VS Code, JetBrains, Neovim, Visual Studio
- **[Cline](vibe.md), [Roo Code](vibe.md)** — open-source agentic extensions for VS Code with multi-provider support
- **In-editor chat panels** in [Cursor](https://www.cursor.com/), [Antigravity](https://antigravity.google/), and Claude Code's VS Code integration

In-editor AI sees your repo and edits files, but stays scoped to the editor session.

### CLI agents (terminal + filesystem)

Command-line agents take the same idea further: they run in your terminal, read and write files anywhere on disk, and execute shell commands. Because they share the filesystem and process model with the rest of your dev environment, they fit naturally into git workflows, build scripts, and remote shells (SSH, CyVerse, HPC clusters).

- **[Claude Code](claude-code.md)** (Anthropic) — CLI agent with MCP support
- **[Codex CLI](https://github.com/openai/codex)** (OpenAI), **[Gemini CLI](https://geminicli.com/)** (Google)
- **Open-source**: [OpenCode](https://opencode.ai/), [ClawCode](https://claw-code.codes/) (clean-room rewrite of Claude Code in Rust + Python)

This surface is the most powerful and the riskiest — see [AI Sandboxes](ai_sandboxes.md) for how to bound what an agent can touch.

### Desktop apps (hybrid IDE + CLI)

A new category of "agent OS" desktop apps blurs the line between chat client, IDE, and CLI. They ship as native applications with file-picker UIs *and* terminal access, MCP server orchestration, and rich rendering of code, diagrams, and documents:

- **[Claude Desktop](https://claude.ai/download)** — the reference example; rich MCP support
- **Codex Desktop** (OpenAI) — agentic computer-use surface for power-user productivity
- **[Cursor](https://www.cursor.com/)** — a VS Code fork that's effectively a desktop agent IDE
- **[Antigravity](https://antigravity.google/)** (Google) — Gemini-driven IDE with agent-mode by default

Desktop apps are typically the easiest path for researchers who aren't comfortable in a terminal but still need on-disk file access and tool use.

### Productivity-suite integration

AI is now embedded in the office software most institutions already license:

- **[Microsoft 365 Copilot](microsoft.md)** — drafting in Word, formula help in Excel, slide generation in PowerPoint, summaries in Outlook and Teams
- **Google Workspace AI** ("Help me write" in Docs, "Help me organize" in Sheets, generative slides in Slides, Gemini in Gmail and Meet) — see [Gemini](gemini.md)

These are often the *first* AI surface most non-developer staff encounter, because they don't require any new tool — the AI is just a button in software you've used for years. Confirm with your IT department how data flows when you click that button: many institutional licenses route data differently than personal accounts. The [Transparency](transparency.md) and [Legal](legal.md) pages cover what to look for.

### AI for documents, design, and presentations

A newer wave of products targets the work researchers and educators actually do all day — collaborative writing, design, slides, and dataset exploration:

- **Claude Cowork** — collaborative document workspace with Claude as a teammate, not a chat window
- **Claude Design** — Anthropic's AI-native design surface for layouts, slides, and visual communication
- **Codex** (OpenAI) — agentic computer-use that drives apps the way a human would, including office and design tools
- **[Perplexity Computer](https://www.perplexity.ai/comet)** — Perplexity's agentic interface that researches, browses, and acts on your behalf

These tools shift the question from "can I prompt an AI?" to "can my AI use the same software I do?" — a meaningful change for non-technical staff who never wanted to learn a CLI.

### Agentic AI, subagents, and what's actually changing

All of the surfaces above increasingly run **agents** rather than single-turn chatbots — see [The Age of Agentic AI](#the-age-of-agentic-ai) below for the formal taxonomy. The shift that matters for this workshop:

- **Subagents** let one agent spawn focused helpers (research, drafting, review) and stitch the results back together. A non-engineer can now ask for "a marketing report" and the orchestrator delegates a literature-review subagent, a chart-making subagent, and a fact-check subagent without any code being written by hand.
- **Coding is becoming more accessible to non-developer careers.** A scientist with no formal CS background can use [Vibe Coding](vibe.md) inside Claude Desktop to build a working data dashboard in an afternoon. That's a real shift — not a hype claim — and one this workshop is designed to make tangible.
- **The same shift creates new responsibilities.** When an agent acts on your behalf, *you* are accountable for what it does. See [Ethics](ethics.md), [Bias](bias.md), and [Transparency](transparency.md) — these aren't optional reading anymore; they're how you keep the trust of your colleagues, students, and IRB.

!!! warning "Where to be careful"
    Each surface has its own data-handling model. Web chat sends prompts to the vendor; IDE extensions send selected code; CLI agents and desktop apps can read your whole disk; productivity-suite Copilots see institutional data covered by your employer's license. Before using any surface for sensitive research, FERPA-protected student data, IRB-restricted records, or unpublished work, confirm the data flow with your institution's IT/security team. The [Legal](legal.md) page lists the regulatory frameworks (EU AI Act, FERPA, HIPAA, NIST RMF) that matter most for academic users.

---

## The Age of Agentic AI

The most significant shift in the AI landscape over the past two years has been the evolution from **conversational AI** to **agentic AI**—systems that don't just respond to questions but take autonomous actions to accomplish goals.

### What Makes AI "Agentic"?

| Traditional Chatbot | Agentic AI System |
|---------------------|-------------------|
| Responds to questions | Pursues goals |
| Single-turn interactions | Multi-step planning |
| Text-only output | Uses tools (search, code, APIs) |
| Stateless | Maintains memory across sessions |
| Reactive | Proactive |
| Requires explicit instructions for each step | Breaks down complex tasks autonomously |

**Example Comparison:**

- **Chatbot**: "How do I fix a bug in my Python code?" → Explains debugging steps
- **Agent**: "Fix the bug in checkout.py" → Searches codebase, identifies issue, implements fix, runs tests, commits changes

### The Agent Capability Spectrum

Agentic AI systems operate across five levels of autonomy:

#### Level 1: Conversational AI
Basic question-answering chatbots like early ChatGPT, Gemini web interface, or Claude without tools.

**Capabilities**: Answer questions, summarize text, explain concepts

**Limitations**: Cannot take actions or use external tools

#### Level 2: Tool-Using LLMs
AI assistants that can search the web, execute code, or access plugins when prompted.

**Capabilities**: Web search, calculations, code execution (sandboxed), API calls

**Examples**: ChatGPT with plugins, Claude with MCP, Gemini with search

#### Level 3: Autonomous Task Completion
Single agents that can complete multi-step tasks independently.

**Capabilities**: Break down goals, iterate on solutions, use multiple tools in sequence

**Examples**: Claude Code, ClawCode, OpenCode, GitHub Copilot Workspace, Cursor agent mode

**Use Cases**:
- Writing and deploying a feature from a description
- Conducting research and compiling a report
- Debugging an application end-to-end

#### Level 4: Multi-Agent Collaboration
Multiple specialized agents working together on complex tasks.

**Capabilities**: Task decomposition, specialization, inter-agent communication

**Frameworks**: CrewAI, AutoGen, LangGraph

**Examples**:
- Software team simulation (product manager + engineers + QA)
- Research team (literature review + data analysis + writing)
- Business workflow automation

#### Level 5: Self-Evolving Systems
Agents that improve their own capabilities through experience.

**Capabilities**: Self-optimization, lifelong learning, capability expansion

**Status**: Research frontier (2025-present)

**Examples**: Experimental systems from [EvoAgentX](https://github.com/EvoAgentX){target=_blank}, academic research

**Where are we today?** Most commercial AI platforms (ChatGPT, Claude, Gemini) operate at Levels 2-3. Developer frameworks enable Level 4. Level 5 remains primarily in research labs.

### Agentic Platforms in 2026

Several platforms now offer agentic capabilities beyond simple chat:

**[Claude Code](claude-code.md)** (Anthropic)

- CLI and IDE integration for autonomous coding
- Can read files, execute commands, make multi-file edits
- Integrated with [Model Context Protocol (MCP)](mcp.md) for tool extensibility
- Best for: Complex refactoring, feature implementation, debugging

**GitHub Copilot Workspace**

- Agentic coding environment in GitHub
- Plans implementation, edits multiple files, creates PRs
- Best for: Issue resolution, feature development

**ChatGPT with Canvas / Projects**

- Artifact-based interaction for iterative creation
- Can maintain context across sessions with Projects
- Best for: Writing, planning, iterative document creation

**Perplexity Comet / Dia / Fellou** (Agentic Browsers)

- Browsers with AI agents that can navigate, extract data, complete forms
- See [Agentic Browsers comparison](choose.md#agentic-browsers-ai-powered-web-browsers)

**CrewAI / AutoGen** (Multi-Agent Frameworks)

- Developer tools for building multi-agent systems
- Best for: Custom workflows, specialized automation

**Open-source agentic coding tools**

The same agent-driven workflow as Claude Code, but with full source-code transparency and provider choice:

- **[OpenCode](https://opencode.ai/)** — terminal-first OSS agent built around an editable plan/diff loop; provider-agnostic
- **[ClawCode](https://claw-code.codes/)** — clean-room rewrite of Claude Code in Rust + Python (`ultraworkers/claw-code`); multi-provider
- **[Cline](vibe.md#cline)** — open-source VS Code extension with agent-mode coding; supports Claude, ChatGPT, local models
- **[Roo Code](vibe.md#roo-code)** — community fork of Cline with additional workflow customization

For detailed guidance on using agentic coding tools, see our [Vibe Coding documentation](vibe.md).

### The Model Context Protocol (MCP)

A key enabler of agentic AI is the **[Model Context Protocol (MCP)](mcp.md)**—an open standard developed by Anthropic that allows AI assistants to securely connect to external tools and data sources.

MCP enables agents to:

- Access local file systems and databases
- Execute terminal commands
- Interact with Git repositories
- Connect to web APIs and services
- Query cloud services (GitHub, Slack, Google Drive, etc.)

**Security Note**: MCP runs locally with explicit user permission for each connection. See our [MCP documentation](mcp.md) for setup instructions.

---

## Industry Landscape Resources

**[Matt Turck's MAD (ML/AI/Data) Landscape](https://mad.firstmark.com/){target=_blank}**

<iframe
    src="https://mad.firstmark.com/"
    frameborder="0"
    width="800"
    height="400"
></iframe>

An annually updated overview of the machine learning, AI, and data ecosystem—covering infrastructure, tools, applications, and industry trends.

**[HuggingFace Arena LLM Leaderboard](https://lmarena.ai/leaderboard){target=_blank}**

A community-driven leaderboard ranking AI models based on blind human evaluations (users vote on responses without knowing which model generated them).

---

## Glossary

!!! Info "External Glossaries"

    [:simple-google: Google's Machine Learning Glossary](https://developers.google.com/machine-learning/glossary){target=_blank}

    [:simple-nvidia: NVIDIA's Data Science Glossary](https://www.nvidia.com/en-us/glossary){target=_blank}

**Agentic AI:**
AI systems that use reasoning and iterative planning to autonomously solve complex, multi-step problems. Agentic systems can break down tasks, use tools, and make decisions to achieve goals with minimal human intervention. See: [Agentic AI documentation](agentic.md).

**AI Agent:**
An AI system that can perceive its environment, make decisions, and take actions to achieve specified goals. Unlike chatbots, agents use tools, maintain memory across interactions, and execute multi-step plans autonomously.

**Attention Mechanism:**
A neural network technique that allows models to focus on relevant parts of input data when processing information. The foundation of transformer architectures used in modern LLMs.

**Chain-of-Thought (CoT):**
A prompting technique that encourages AI models to break down complex problems into intermediate reasoning steps, improving accuracy on tasks requiring logic and multi-step reasoning.

**Context Window:**
The maximum amount of text (measured in tokens) that an LLM can process at once, including both input and output. Modern frontier models offer context windows from hundreds of thousands to over 1 million tokens (Gemini Pro and Claude's largest tier).

**Diffusion Models:**
A class of generative models that create images by iteratively denoising random noise. Used in Stable Diffusion, DALL-E, and Midjourney for text-to-image generation.

**Embeddings:**
Numerical vector representations of data (text, images, audio) that capture semantic meaning and relationships. Used for search, clustering, recommendations, and RAG systems.

**Few-Shot Learning:**
The ability of an AI model to learn new tasks from just a few examples in the prompt, without additional training or fine-tuning.

**Fine-Tuning:**
The process of further training a pre-trained model on a specific dataset or task to specialize its capabilities for particular domains or use cases.

**Foundation Models:**
Large-scale AI models (LLMs, vision models, multimodal models) trained on massive datasets. They serve as a base for many downstream tasks via transfer learning and rapid adaptation. Examples: GPT, Claude, Gemini, Llama, Qwen, DeepSeek, Mistral.

**Hallucination:**
When an AI model generates false, nonsensical, or unfaithful information presented as fact. A key challenge in LLM reliability, especially for factual domains.

**Interactive Generative Video (IGV):**
AI systems that generate video content in real-time based on user input, combining video generation with interactive control. Unlike passive video generation (Sora, Runway), IGV systems respond to user actions in real-time, enabling gaming, simulation, and embodied AI applications.

**Large Language Models (LLMs):**
A subset of foundation models trained on extensive text corpora, enabling them to generate human-like text, summarize information, reason about topics, and perform various NLP tasks. Examples: GPT, Claude, Gemini, Llama, Qwen, DeepSeek, Mistral.

**Lifelong Learning:**
The capability of an AI system to continuously learn and adapt from new experiences after initial training, accumulating knowledge over time. Enables agents to improve through environmental feedback and adapt to changing contexts without catastrophic forgetting.

**LoRA (Low-Rank Adaptation):**
An efficient fine-tuning technique that modifies only a small subset of model parameters, reducing computational costs while maintaining performance for specialized tasks.

**MCP (Model Context Protocol):**
An open standard protocol developed by Anthropic for connecting AI assistants to external data sources and tools. Enables LLMs to access databases, APIs, and live information while maintaining security and privacy. See: [MCP documentation](mcp.md).

**Mixture of Experts (MoE):**
A neural network architecture that uses multiple specialized sub-models (experts) and activates only relevant ones for each input, improving efficiency and scalability in large models.

**Multimodal Models:**
AI systems that can process and generate multiple types of data (text, images, audio, video) in combination. Examples: GPT with vision, Gemini, Claude.

**Multi-Agent System:**
An AI architecture where multiple specialized agents collaborate to complete complex tasks, with each agent handling specific subtasks and coordinating with others. Examples: CrewAI, AutoGen frameworks.

**Parameters:**
The trainable values within a neural network that determine the model's learned behavior. Model size is often described by parameter count (e.g., 7B, 70B, 405B parameters).

**Prompt Engineering:**
The practice of crafting, refining, and optimizing instructions (prompts) given to AI models to guide their outputs toward desired results.

**Quantization:**
A technique that reduces the precision of model weights (e.g., from 16-bit to 4-bit) to decrease memory usage and computational requirements, enabling deployment on resource-constrained devices.

**RAG (Retrieval-Augmented Generation):**
A technique that enhances LLM responses by retrieving relevant information from external knowledge bases or documents before generating answers, reducing hallucinations and improving factual accuracy. See: [RAG documentation](rag.md).

**RLHF (Reinforcement Learning from Human Feedback):**
A training method that uses human preferences to fine-tune AI models, improving their alignment with human values and desired behaviors. Used extensively in ChatGPT and Claude development.

**Self-Evolving Agent:**
An AI agent capable of improving its own performance through experience, optimizing aspects like behavior strategies, prompts, memory systems, or tool usage without explicit human retraining. Represents the frontier of agentic AI research.

**System Prompt:**
Initial instructions given to an AI model that define its role, behavior, constraints, and capabilities for a conversation or task. Often invisible to end users but shapes all responses.

**Temperature:**
A parameter controlling randomness in AI-generated outputs. Lower temperatures (0.0-0.3) produce deterministic responses; higher temperatures (0.7-1.0) increase creativity and variability.

**Token:**
A fundamental unit of text—often a word, subword, or character—that LLMs process. Pricing and context limits are typically measured in tokens.

**Transformer:**
The neural network architecture that powers modern LLMs, introduced in "Attention is All You Need" (2017). Uses attention mechanisms to process sequences efficiently.

**Vector Database:**
A specialized database optimized for storing and querying high-dimensional embedding vectors, enabling fast semantic search and similarity matching for RAG applications.

**Zero-shot Learning:**
The capability of an AI model to perform tasks it has never been explicitly trained on, often made possible by large-scale pretraining on diverse datasets.

---

## Further Reading

**Foundation Model Evolution:**

- [Yang et al. 2023: Harnessing the Power of LLMs in Practice](https://arxiv.org/abs/2304.13712){target=_blank}
- [Attention is All You Need (Transformer paper)](https://arxiv.org/abs/1706.03762){target=_blank}

**Agentic AI Research:**

- [Fang et al. 2025: A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407){target=_blank}
- [Awesome Self-Evolving Agents](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents){target=_blank} - Collection of 100+ papers

**Interactive Generative Video:**

- [Yu et al. 2025: A Survey of Interactive Generative Video](https://arxiv.org/abs/2504.21853){target=_blank}

**Agentic Frameworks:**

- [EvoAgentX](https://github.com/EvoAgentX){target=_blank} - Framework for automated evolving agentic workflows
- [MASLab](https://github.com/microsoft/MASLab){target=_blank} - Unified codebase for LLM-based multi-agent systems
- [CrewAI](https://www.crewai.com/){target=_blank} - Framework for orchestrating role-playing autonomous AI agents
- [AutoGen](https://microsoft.github.io/autogen/){target=_blank} - Microsoft's multi-agent conversation framework
