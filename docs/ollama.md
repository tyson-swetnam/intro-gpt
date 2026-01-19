# Ollama

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## What is Ollama?

[Ollama](https://ollama.com/){target=_blank} is an open-source tool that makes it simple to run large language models (LLMs) locally on your own computer. Think of it as a "Docker for AI models" - it handles all the complexity of downloading, configuring, and running AI models so you can focus on using them.

**Why Run AI Models Locally?**

| Benefit | Description |
|---------|-------------|
| **Privacy** | Your data never leaves your computer - ideal for sensitive research, patient data, or proprietary information |
| **No API Costs** | After initial setup, unlimited usage with no per-token charges |
| **Offline Access** | Work without internet connectivity once models are downloaded |
| **Customization** | Fine-tune models, adjust parameters, and create custom configurations |
| **No Rate Limits** | Generate as much content as your hardware can handle |
| **Reproducibility** | Lock down specific model versions for reproducible research |

**When to Use Ollama vs. Cloud Services:**

- **Use Ollama** when: privacy is paramount, you have adequate hardware, you need offline access, or you want to experiment freely without cost concerns
- **Use Cloud Services** (ChatGPT, Claude, etc.) when: you need the most capable models, lack powerful hardware, or need multimodal capabilities like vision

!!! info "Hardware Requirements"
    Running local models requires computational resources. As a general guideline:

    - **Small models (1-3B parameters):** 8GB RAM minimum, runs on most modern laptops
    - **Medium models (7-8B parameters):** 16GB RAM recommended, GPU acceleration helpful
    - **Large models (13B+ parameters):** 32GB+ RAM or dedicated GPU with 8GB+ VRAM

    Apple Silicon Macs (M1/M2/M3/M4) are particularly well-suited for local AI due to unified memory architecture.

## Installation

### macOS

**Option 1: Download the App (Recommended)**

1. Visit [ollama.com/download](https://ollama.com/download){target=_blank}
2. Download the macOS installer
3. Open the downloaded file and drag Ollama to your Applications folder
4. Launch Ollama from Applications - it will appear as a llama icon in your menu bar
5. The Ollama service now runs in the background

**Option 2: Homebrew**

```bash
brew install ollama
```

After installation, start the Ollama service:

```bash
ollama serve
```

### Linux

**One-Line Install Script:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This script:

- Detects your Linux distribution (Ubuntu, Debian, Fedora, CentOS, Arch, etc.)
- Installs Ollama to `/usr/local/bin`
- Sets up a systemd service for automatic startup
- Configures GPU support if NVIDIA drivers are detected

**Manual Installation (Alternative):**

```bash
# Download the binary
curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama

# Make it executable
chmod +x ollama

# Move to system path
sudo mv ollama /usr/local/bin/

# Start the service
ollama serve
```

**Start Ollama on Boot:**

```bash
# Enable the systemd service
sudo systemctl enable ollama

# Start the service now
sudo systemctl start ollama

# Check service status
sudo systemctl status ollama
```

### Windows

**Option 1: Windows Installer (Recommended)**

1. Visit [ollama.com/download](https://ollama.com/download){target=_blank}
2. Download the Windows installer (`.exe`)
3. Run the installer and follow the prompts
4. Ollama will start automatically and appear in the system tray

**Option 2: Windows Subsystem for Linux (WSL)**

If you prefer a Linux-like environment on Windows:

```bash
# First, ensure WSL2 is installed and updated
wsl --install

# Then in your WSL terminal:
curl -fsSL https://ollama.com/install.sh | sh
```

### Docker

For containerized deployments or server environments:

```bash
# Pull and run the Ollama container
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# With NVIDIA GPU support
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### Verify Installation

After installation, verify Ollama is working:

```bash
# Check Ollama version
ollama --version

# List available models (will be empty initially)
ollama list

# Test the API endpoint
curl http://localhost:11434/api/tags
```

## Downloading and Managing Models

### The Model Library

Ollama maintains a curated library of optimized models at [ollama.com/library](https://ollama.com/library){target=_blank}. These models are:

- Pre-quantized for efficient memory usage
- Tested for compatibility with Ollama
- Available in multiple size variants
- Automatically configured for optimal performance

### Downloading Models

**Basic Download:**

```bash
# Download a model (happens automatically when you run it)
ollama pull llama3.2

# Or run directly - it will download if not present
ollama run llama3.2
```

**Specify Model Size/Variant:**

Models often come in multiple sizes. Use tags to select:

```bash
# Llama 3.2 variants
ollama pull llama3.2:1b      # 1 billion parameters (~1GB)
ollama pull llama3.2:3b      # 3 billion parameters (~2GB)
ollama pull llama3.2         # Default (usually the balanced option)

# Qwen 2.5 variants
ollama pull qwen2.5:0.5b     # Tiny - very fast
ollama pull qwen2.5:1.5b     # Small
ollama pull qwen2.5:3b       # Medium
ollama pull qwen2.5:7b       # Large - best quality
ollama pull qwen2.5:14b      # Extra large
ollama pull qwen2.5:32b      # Very large - requires significant RAM/VRAM
ollama pull qwen2.5:72b      # Massive - requires high-end GPU

# DeepSeek R1 distilled models
ollama pull deepseek-r1:1.5b # Smallest reasoning model
ollama pull deepseek-r1:7b   # Good balance
ollama pull deepseek-r1:8b   # Llama-based distillation
ollama pull deepseek-r1:14b  # Higher quality
ollama pull deepseek-r1:32b  # Best distilled quality
ollama pull deepseek-r1:70b  # Full-size distillation
```

### Managing Downloaded Models

```bash
# List all downloaded models
ollama list

# Example output:
# NAME              ID              SIZE      MODIFIED
# llama3.2:latest   a3e4c7e8d9f0    2.0 GB    2 hours ago
# qwen2.5:7b        b5f6c8d9e0a1    4.4 GB    1 day ago
# deepseek-r1:8b    c7d8e9f0a1b2    4.9 GB    3 days ago

# Show detailed information about a model
ollama show llama3.2

# Delete a model to free disk space
ollama rm llama3.2:1b

# Copy a model (useful for creating variants)
ollama cp llama3.2 my-llama
```

### Model Storage Location

Models are stored in:

- **macOS:** `~/.ollama/models`
- **Linux:** `~/.ollama/models` or `/usr/share/ollama/.ollama/models`
- **Windows:** `C:\Users\<username>\.ollama\models`

To change the storage location, set the `OLLAMA_MODELS` environment variable:

```bash
# Linux/macOS
export OLLAMA_MODELS=/path/to/your/models

# Windows PowerShell
$env:OLLAMA_MODELS = "D:\ollama\models"
```

## Running Models

### Interactive Chat

The simplest way to use Ollama is through interactive chat:

```bash
ollama run llama3.2
```

This opens an interactive session where you can type prompts and receive responses. Use `/bye` or Ctrl+C to exit.

**Chat Session Commands:**

| Command | Description |
|---------|-------------|
| `/bye` | Exit the chat session |
| `/clear` | Clear conversation history |
| `/set parameter value` | Change model parameters |
| `/show info` | Display model information |
| `/show license` | Show model license |
| `/load <model>` | Load a different model |
| `/save <name>` | Save current session |

### Single-Prompt Execution

For scripting and automation, pass the prompt directly:

```bash
# Single prompt with immediate response
ollama run llama3.2 "What is photosynthesis?"

# Pipe input from a file
cat essay.txt | ollama run llama3.2 "Summarize this text:"

# Save output to a file
ollama run llama3.2 "Write a haiku about machine learning" > haiku.txt
```

### Model Parameters

Adjust model behavior with parameters:

```bash
# In interactive mode
/set temperature 0.7
/set num_predict 500

# Or set when starting
ollama run llama3.2 --verbose
```

**Common Parameters:**

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| `temperature` | Creativity/randomness | 0.8 | 0.0-2.0 |
| `top_p` | Nucleus sampling threshold | 0.9 | 0.0-1.0 |
| `top_k` | Limit vocabulary sampling | 40 | 1-100 |
| `num_predict` | Maximum tokens to generate | 128 | -1 (unlimited) to n |
| `num_ctx` | Context window size | 2048 | Model-dependent |
| `repeat_penalty` | Penalty for repetition | 1.1 | 0.0-2.0 |
| `seed` | Random seed for reproducibility | Random | Any integer |

### Multiline Input

For complex prompts, use multiline input:

```bash
ollama run llama3.2 """
You are an expert historian. Please analyze the following event
and provide context about its significance:

The signing of the Treaty of Westphalia in 1648.

Include:
1. Historical context
2. Key provisions
3. Long-term impact on international relations
"""
```

## Using the Ollama API

Ollama provides a REST API that enables integration with other applications. The API runs on `http://localhost:11434` by default.

### Generate Completions

**Basic Generation:**

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Explain quantum computing in simple terms",
  "stream": false
}'
```

**With Parameters:**

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Write a creative story about a robot learning to paint",
  "stream": false,
  "options": {
    "temperature": 0.9,
    "num_predict": 500,
    "top_p": 0.95
  }
}'
```

### Chat API (Conversational)

For multi-turn conversations:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {"role": "system", "content": "You are a helpful research assistant."},
    {"role": "user", "content": "What are the main causes of climate change?"},
    {"role": "assistant", "content": "The main causes include greenhouse gas emissions..."},
    {"role": "user", "content": "How can individuals help reduce these emissions?"}
  ],
  "stream": false
}'
```

### Streaming Responses

For real-time output, enable streaming:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Write a detailed explanation of neural networks",
  "stream": true
}'
```

Each response chunk is a JSON object. Parse them line by line for real-time display.

### API Endpoints Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/generate` | POST | Generate text completion |
| `/api/chat` | POST | Chat with conversation history |
| `/api/tags` | GET | List available models |
| `/api/show` | POST | Show model information |
| `/api/pull` | POST | Download a model |
| `/api/delete` | DELETE | Remove a model |
| `/api/copy` | POST | Copy a model |
| `/api/embeddings` | POST | Generate embeddings |

## Python Integration

### Using the Official Ollama Python Library

```bash
pip install ollama
```

**Basic Usage:**

```python
import ollama

# Simple generation
response = ollama.generate(
    model='llama3.2',
    prompt='What is machine learning?'
)
print(response['response'])
```

**Chat Conversation:**

```python
import ollama

# Multi-turn chat
messages = [
    {'role': 'system', 'content': 'You are a helpful coding assistant.'},
    {'role': 'user', 'content': 'Write a Python function to calculate factorial'}
]

response = ollama.chat(
    model='llama3.2',
    messages=messages
)

print(response['message']['content'])
```

**Streaming Responses:**

```python
import ollama

# Stream responses for better UX
stream = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Explain the water cycle'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

**Generate Embeddings:**

```python
import ollama

# Generate embeddings for semantic search or RAG
embedding = ollama.embeddings(
    model='nomic-embed-text',  # or any embedding model
    prompt='The quick brown fox jumps over the lazy dog'
)

print(f"Embedding dimension: {len(embedding['embedding'])}")
```

### Using with LangChain

[LangChain](https://langchain.com/){target=_blank} provides a powerful framework for building LLM applications:

```bash
pip install langchain langchain-ollama
```

```python
from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(model="llama3.2")

# Simple invocation
response = llm.invoke("What are the benefits of exercise?")
print(response)
```

**Chat Model with History:**

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOllama(model="llama3.2", temperature=0.7)

messages = [
    SystemMessage(content="You are a research assistant specializing in biology."),
    HumanMessage(content="Explain CRISPR gene editing.")
]

response = chat.invoke(messages)
print(response.content)
```

**Building a Simple RAG System:**

```python
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Initialize components
llm = OllamaLLM(model="llama3.2")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Sample documents (in practice, load from files)
documents = [
    "Machine learning is a subset of artificial intelligence...",
    "Neural networks are inspired by biological neurons...",
    "Deep learning uses multiple layers of neural networks..."
]

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = text_splitter.create_documents(documents)

# Create vector store
vectorstore = Chroma.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()

# Create RAG chain
template = """Answer based on the context:
Context: {context}
Question: {question}
Answer:"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Query
response = rag_chain.invoke("What is deep learning?")
print(response)
```

For more on RAG systems, see our [RAG documentation](rag.md).

### Using with Requests (Direct API)

For simple integrations without additional dependencies:

```python
import requests
import json

def query_ollama(prompt, model="llama3.2", stream=False):
    """Simple function to query Ollama API."""
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': stream
        }
    )

    if stream:
        # Handle streaming response
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                yield chunk.get('response', '')
    else:
        return response.json()['response']

# Usage
result = query_ollama("What is the capital of France?")
print(result)

# Streaming usage
for chunk in query_ollama("Tell me a story", stream=True):
    print(chunk, end='', flush=True)
```

## Jupyter Notebook Integration

Ollama integrates seamlessly with Jupyter notebooks for interactive research:

### Basic Notebook Usage

```python
# Cell 1: Install and import
!pip install ollama

import ollama

# Cell 2: List available models
models = ollama.list()
for model in models['models']:
    print(f"{model['name']}: {model['size'] / 1e9:.1f} GB")

# Cell 3: Interactive chat
response = ollama.generate(
    model='llama3.2',
    prompt='Explain the difference between correlation and causation'
)
print(response['response'])
```

### Building a Research Assistant

```python
import ollama

class ResearchAssistant:
    """A simple research assistant using Ollama."""

    def __init__(self, model='llama3.2'):
        self.model = model
        self.conversation = []

    def set_context(self, context):
        """Set the research context/system prompt."""
        self.conversation = [{
            'role': 'system',
            'content': context
        }]

    def ask(self, question):
        """Ask a question and get a response."""
        self.conversation.append({
            'role': 'user',
            'content': question
        })

        response = ollama.chat(
            model=self.model,
            messages=self.conversation
        )

        assistant_message = response['message']['content']
        self.conversation.append({
            'role': 'assistant',
            'content': assistant_message
        })

        return assistant_message

    def summarize_paper(self, abstract):
        """Summarize a research paper abstract."""
        prompt = f"""Please analyze this research abstract and provide:
1. Main research question
2. Methodology used
3. Key findings
4. Potential implications

Abstract:
{abstract}"""

        return self.ask(prompt)

# Usage in notebook
assistant = ResearchAssistant(model='llama3.2')
assistant.set_context("You are an expert in computational biology.")

response = assistant.ask("What are the latest advances in protein folding prediction?")
print(response)
```

For more on Jupyter AI integration, see our [Jupyter AI documentation](jupyter.md).

## Creating Custom Models with Modelfiles

Modelfiles allow you to create customized versions of models with specific behaviors, system prompts, or parameters.

### Basic Modelfile Structure

Create a file called `Modelfile` (no extension):

```dockerfile
# Base model to customize
FROM llama3.2

# Set model parameters
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
PARAMETER top_p 0.9

# Set the system prompt
SYSTEM """You are a helpful research assistant specializing in academic writing.
You help researchers improve their papers by:
- Suggesting clearer phrasing
- Identifying logical gaps
- Recommending relevant citations
- Improving overall structure

Always be constructive and specific in your feedback."""

# Optional: Add custom template
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}<|end|>
{{ end }}{{ if .Prompt }}<|user|>
{{ .Prompt }}<|end|>
{{ end }}<|assistant|>
{{ .Response }}<|end|>
"""
```

### Create and Use the Custom Model

```bash
# Create the custom model
ollama create research-assistant -f Modelfile

# Run your custom model
ollama run research-assistant
```

### Modelfile Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `FROM` | Base model (required) | `FROM llama3.2` |
| `PARAMETER` | Set model parameters | `PARAMETER temperature 0.7` |
| `SYSTEM` | Set system prompt | `SYSTEM "You are helpful..."` |
| `TEMPLATE` | Custom prompt template | `TEMPLATE "..."` |
| `ADAPTER` | Apply LoRA adapter | `ADAPTER ./lora.gguf` |
| `LICENSE` | Specify license | `LICENSE "MIT"` |
| `MESSAGE` | Add example messages | `MESSAGE user "Hello"` |

### Example: Academic Discipline-Specific Assistants

**Biology Research Assistant:**

```dockerfile
FROM llama3.2

PARAMETER temperature 0.3
PARAMETER num_ctx 8192

SYSTEM """You are an expert biology research assistant with deep knowledge of:
- Molecular biology and genetics
- Cell biology and biochemistry
- Evolutionary biology
- Ecology and environmental science

When answering questions:
1. Use precise scientific terminology
2. Cite relevant concepts and theories
3. Distinguish between established facts and current hypotheses
4. Suggest relevant experimental approaches when applicable"""
```

**Statistics Tutor:**

```dockerfile
FROM qwen2.5:7b

PARAMETER temperature 0.2
PARAMETER num_ctx 4096

SYSTEM """You are a patient statistics tutor helping graduate students understand
statistical concepts. When explaining:

1. Start with intuitive explanations before formal definitions
2. Use concrete examples from research contexts
3. Show step-by-step calculations when relevant
4. Explain assumptions and when methods are appropriate
5. Suggest R or Python code for implementation

Always check for understanding and offer to clarify further."""
```

**Code Review Assistant:**

```dockerfile
FROM deepseek-r1:8b

PARAMETER temperature 0.1
PARAMETER num_ctx 8192

SYSTEM """You are a senior software engineer conducting code reviews.
For each piece of code you review:

1. Identify potential bugs or errors
2. Suggest performance improvements
3. Recommend better naming or structure
4. Check for security vulnerabilities
5. Ensure code follows best practices

Be constructive and explain the reasoning behind each suggestion."""
```

## GPU Configuration and Performance

### Automatic GPU Detection

Ollama automatically detects and uses available GPUs. Check your GPU status:

```bash
ollama run llama3.2 --verbose
# Look for "gpu" in the output
```

### NVIDIA GPU Setup (Linux)

Ensure you have the NVIDIA drivers and CUDA toolkit:

```bash
# Check NVIDIA driver
nvidia-smi

# The Ollama install script usually handles CUDA setup
# If needed, install CUDA toolkit:
# sudo apt install nvidia-cuda-toolkit
```

### Apple Silicon Optimization

Apple M1/M2/M3/M4 Macs use Metal for GPU acceleration automatically. Ollama is highly optimized for Apple Silicon:

```bash
# Check Metal usage (models should show "metal" backend)
ollama run llama3.2 --verbose
```

### Memory Management

**Control GPU Memory Usage:**

```bash
# Set maximum VRAM usage (in MB)
OLLAMA_GPU_MEMORY=8192 ollama serve

# Or in environment
export OLLAMA_GPU_MEMORY=8192
```

**CPU-Only Mode:**

```bash
# Disable GPU acceleration
CUDA_VISIBLE_DEVICES="" ollama serve
```

### Performance Tuning Parameters

| Environment Variable | Description | Example |
|---------------------|-------------|---------|
| `OLLAMA_NUM_PARALLEL` | Number of parallel requests | `4` |
| `OLLAMA_MAX_LOADED_MODELS` | Models to keep in memory | `2` |
| `OLLAMA_GPU_MEMORY` | Max GPU memory (MB) | `8192` |
| `OLLAMA_HOST` | API bind address | `0.0.0.0:11434` |
| `OLLAMA_KEEP_ALIVE` | Model unload timeout | `5m` |

### Monitoring Performance

```bash
# Watch GPU memory usage (NVIDIA)
watch -n 1 nvidia-smi

# Monitor Ollama logs
journalctl -u ollama -f  # Linux with systemd
```

## Model Recommendations

### By Hardware Capability

=== "Laptop (8GB RAM)"

    | Model | Size | Best For |
    |-------|------|----------|
    | `llama3.2:1b` | ~700MB | Quick responses, basic tasks |
    | `qwen2.5:1.5b` | ~1GB | Multilingual, reasoning |
    | `phi3:mini` | ~2GB | Coding, analysis |
    | `deepseek-r1:1.5b` | ~1GB | Reasoning tasks |

=== "Workstation (16-32GB RAM)"

    | Model | Size | Best For |
    |-------|------|----------|
    | `llama3.2:3b` | ~2GB | Balanced performance |
    | `qwen2.5:7b` | ~4.5GB | Strong reasoning, coding |
    | `mistral:7b` | ~4GB | General purpose |
    | `deepseek-r1:8b` | ~5GB | Advanced reasoning |
    | `codellama:13b` | ~7GB | Specialized coding |

=== "GPU Server (24GB+ VRAM)"

    | Model | Size | Best For |
    |-------|------|----------|
    | `llama3.3:70b` | ~40GB | Near-frontier capability |
    | `qwen2.5:32b` | ~20GB | Strong all-around |
    | `deepseek-r1:70b` | ~40GB | Best open reasoning |
    | `mixtral:8x7b` | ~26GB | Mixture of experts |

### By Use Case

**Academic Writing and Research:**

```bash
# For writing assistance and analysis
ollama pull qwen2.5:7b

# For reasoning-heavy tasks
ollama pull deepseek-r1:8b
```

**Coding and Development:**

```bash
# General coding
ollama pull deepseek-coder:6.7b

# Code review and debugging
ollama pull codellama:13b

# Fast completions
ollama pull starcoder2:3b
```

**Data Analysis:**

```bash
# Statistical reasoning
ollama pull qwen2.5:7b

# Code generation for analysis
ollama pull deepseek-coder:6.7b
```

**Teaching and Tutoring:**

```bash
# Patient explanations
ollama pull llama3.2:3b

# Math and science tutoring
ollama pull qwen2.5:7b
```

**Embeddings and RAG:**

```bash
# Text embeddings
ollama pull nomic-embed-text

# Multilingual embeddings
ollama pull mxbai-embed-large
```

## Integration with Other Tools

### Open WebUI

[Open WebUI](https://github.com/open-webui/open-webui){target=_blank} provides a ChatGPT-like interface for Ollama:

```bash
# Run with Docker
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

Access at `http://localhost:3000`. Open WebUI automatically detects your Ollama installation.

### VS Code Integration

Install the [Continue](https://continue.dev/){target=_blank} extension for AI-assisted coding with Ollama:

1. Install the Continue extension from VS Code marketplace
2. Configure to use Ollama in settings:

```json
{
  "models": [
    {
      "title": "Ollama",
      "provider": "ollama",
      "model": "deepseek-coder:6.7b"
    }
  ]
}
```

### Obsidian Integration

Use the [Ollama plugin for Obsidian](https://github.com/hinterdupfinger/obsidian-ollama){target=_blank} for note-taking with AI assistance.

### API-Compatible Services

Ollama's API is compatible with the OpenAI API format. Many tools that support OpenAI can work with Ollama:

```python
# Using OpenAI library with Ollama
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'  # Ollama doesn't require a key, but the library needs something
)

response = client.chat.completions.create(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': 'Hello!'}
    ]
)

print(response.choices[0].message.content)
```

## Troubleshooting

### Common Issues and Solutions

??? failure "Model fails to load - Out of Memory"

    **Symptoms:** Error messages about memory allocation, system becomes unresponsive

    **Solutions:**

    1. Try a smaller model variant:
        ```bash
        # Instead of
        ollama run llama3.2

        # Try
        ollama run llama3.2:1b
        ```

    2. Close other memory-intensive applications

    3. Reduce context window:
        ```bash
        ollama run llama3.2 --num-ctx 2048
        ```

    4. Use quantized versions (look for `q4_0` or `q4_K_M` tags)

??? failure "Ollama service not running"

    **Symptoms:** Connection refused errors, `curl: (7) Failed to connect`

    **Solutions:**

    1. Start the service:
        ```bash
        # macOS/Windows: Launch the Ollama app
        # Linux:
        ollama serve
        # Or with systemd:
        sudo systemctl start ollama
        ```

    2. Check if another process is using port 11434:
        ```bash
        lsof -i :11434
        ```

    3. Use a different port:
        ```bash
        OLLAMA_HOST=127.0.0.1:11435 ollama serve
        ```

??? failure "Slow generation speed"

    **Symptoms:** Model runs much slower than expected

    **Solutions:**

    1. Verify GPU is being used:
        ```bash
        ollama run llama3.2 --verbose
        # Look for "gpu" or "metal" in output
        ```

    2. Check GPU drivers are up to date

    3. Ensure sufficient VRAM:
        ```bash
        nvidia-smi  # For NVIDIA GPUs
        ```

    4. Try a smaller model or quantization

??? failure "Model gives poor quality responses"

    **Symptoms:** Responses are incoherent, repetitive, or off-topic

    **Solutions:**

    1. Adjust temperature:
        ```bash
        /set temperature 0.7
        ```

    2. Increase context window for complex tasks:
        ```bash
        /set num_ctx 4096
        ```

    3. Try a larger model variant

    4. Be more specific in your prompts

??? failure "Cannot connect from other devices"

    **Symptoms:** API works on localhost but not from other machines

    **Solutions:**

    1. Bind to all interfaces:
        ```bash
        OLLAMA_HOST=0.0.0.0:11434 ollama serve
        ```

    2. Check firewall settings:
        ```bash
        # Linux
        sudo ufw allow 11434
        ```

    3. Verify network connectivity

### Getting Help

- **Official Documentation:** [github.com/ollama/ollama](https://github.com/ollama/ollama){target=_blank}
- **Discord Community:** [discord.gg/ollama](https://discord.gg/ollama){target=_blank}
- **GitHub Issues:** [github.com/ollama/ollama/issues](https://github.com/ollama/ollama/issues){target=_blank}

## Academic Use Cases

### Literature Review Assistance

```python
import ollama

def analyze_abstract(abstract):
    """Analyze a research paper abstract."""
    prompt = f"""Analyze this research abstract and provide:
1. Research question or hypothesis
2. Methodology
3. Key findings
4. Limitations mentioned
5. Potential follow-up questions

Abstract:
{abstract}
"""

    response = ollama.generate(model='qwen2.5:7b', prompt=prompt)
    return response['response']

# Example usage
abstract = """
We present a novel approach to protein structure prediction using
graph neural networks. Our method achieves state-of-the-art results
on the CASP14 benchmark, outperforming existing methods by 15% in
GDT-TS score. We demonstrate that incorporating evolutionary
information through multiple sequence alignments significantly
improves prediction accuracy.
"""

analysis = analyze_abstract(abstract)
print(analysis)
```

### Grant Writing Support

```python
import ollama

def improve_grant_section(text, section_type):
    """Suggest improvements for grant application sections."""
    prompt = f"""You are an experienced grant reviewer. Review this {section_type}
section and provide specific suggestions to strengthen it:

{text}

Please provide:
1. Strengths of the current text
2. Areas that need improvement
3. Specific rewrite suggestions
4. Questions a reviewer might ask"""

    response = ollama.generate(model='qwen2.5:7b', prompt=prompt)
    return response['response']
```

### Teaching Assistant

```python
import ollama

def create_quiz_questions(topic, difficulty, num_questions):
    """Generate quiz questions on a topic."""
    prompt = f"""Create {num_questions} {difficulty}-level multiple choice questions
about {topic}. For each question:
1. Provide the question
2. Give 4 options (A, B, C, D)
3. Indicate the correct answer
4. Explain why the correct answer is right

Format clearly with separators between questions."""

    response = ollama.generate(model='llama3.2', prompt=prompt)
    return response['response']

# Generate quiz
quiz = create_quiz_questions(
    topic="the scientific method",
    difficulty="intermediate",
    num_questions=5
)
print(quiz)
```

### Data Analysis Helper

```python
import ollama

def suggest_analysis(data_description):
    """Suggest statistical analyses for a dataset."""
    prompt = f"""Based on this data description, suggest appropriate statistical
analyses and explain the rationale:

{data_description}

Please provide:
1. Recommended statistical tests/methods
2. Assumptions to check
3. Python/R code snippets for implementation
4. How to interpret potential results"""

    response = ollama.generate(model='qwen2.5:7b', prompt=prompt)
    return response['response']
```

## Further Resources

- **Ollama Website:** [ollama.com](https://ollama.com/){target=_blank}
- **Model Library:** [ollama.com/library](https://ollama.com/library){target=_blank}
- **GitHub Repository:** [github.com/ollama/ollama](https://github.com/ollama/ollama){target=_blank}
- **API Documentation:** [github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md){target=_blank}
- **Discord Community:** [discord.gg/ollama](https://discord.gg/ollama){target=_blank}

## Related Workshop Materials

- **[Hugging Face](huggingface.md):** Find and download models for use with Ollama
- **[Gradio](gradio.md):** Build web interfaces for your Ollama-powered applications
- **[RAG](rag.md):** Implement retrieval-augmented generation with local models
- **[Jupyter AI](jupyter.md):** Integrate AI assistance into your research notebooks
- **[Agentic AI](agentic.md):** Build autonomous AI agents with local models
- **[MCP](mcp.md):** Connect Ollama to external tools and data sources

!!! tip "Getting Started Recommendation"
    If you're new to running local AI models, start with these steps:

    1. Install Ollama using the method for your operating system
    2. Download a small model: `ollama pull llama3.2:3b`
    3. Try interactive chat: `ollama run llama3.2:3b`
    4. Experiment with the Python library for programmatic access
    5. Create a custom Modelfile for your specific use case

    Once comfortable, explore larger models and integrations with tools like Open WebUI or LangChain.
