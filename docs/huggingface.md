# Hugging Face

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## What is Hugging Face?

[Hugging Face](https://huggingface.co){target=_blank} is the central hub for the open-source AI community. Think of it as "GitHub for AI models" - a platform where researchers and developers share:

- **Models:** Pre-trained AI models ready to download and use
- **Datasets:** Training and evaluation data for machine learning
- **Spaces:** Interactive demos and applications
- **Documentation:** Model cards, papers, and usage guides

For researchers and academics, Hugging Face provides access to state-of-the-art models without needing to train them from scratch, saving significant computational resources and time.

??? Info "Create a Hugging Face Account"

    **:hugging: Hugging Face**

    Follow these instructions to sign up for Hugging Face:

    1. Visit the Hugging Face website: [https://huggingface.co](https://huggingface.co/){target=_blank}

    2. Click on the "Sign Up" button in the top-right corner of the page.

    3. Fill in your email address, username, and password in the respective fields.

    4. Check the box to agree to Hugging Face's terms and conditions, then click "Sign Up."

    5. You'll receive an email to confirm your account. Click on the confirmation link in the email.

    6. Once your account is confirmed, sign in to access Hugging Face's features.

    For more information, visit the Hugging Face documentation: [https://huggingface.co/docs](https://huggingface.co/docs){target=_blank}

## Navigating the Hub

### Finding Models

The [Model Hub](https://huggingface.co/models){target=_blank} hosts over 1 million models. To find what you need:

1. **Browse by Task:** Filter by what you want to do (text generation, image classification, translation, etc.)
2. **Sort by Downloads:** Popular models are well-tested and documented
3. **Filter by License:** Important for academic and commercial use
4. **Check the Model Card:** Every model should have documentation explaining its capabilities and limitations

**Popular Model Categories for Researchers:**

| Category | Example Models | Use Cases |
|----------|---------------|-----------|
| Text Generation | Llama 3, Mistral, Qwen | Writing assistance, code generation, analysis |
| Embeddings | BGE, E5, GTE | Document search, similarity matching, RAG |
| Vision-Language | LLaVA, Qwen-VL | Image analysis, chart interpretation |
| Speech | Whisper, Wav2Vec2 | Transcription, audio analysis |

### Finding Datasets

The [Dataset Hub](https://huggingface.co/datasets){target=_blank} hosts datasets for training and evaluation:

1. **Search by Domain:** Academic papers, code, images, audio, etc.
2. **Check Size and Format:** Ensure it fits your storage and processing capabilities
3. **Review the License:** Some datasets have restrictions on use

## Installing the Hugging Face CLI

The `huggingface_hub` library provides tools for downloading and managing models.

### Installation

=== "pip"

    ```bash
    pip install huggingface_hub
    ```

=== "conda"

    ```bash
    conda install -c conda-forge huggingface_hub
    ```

### Authentication (Required for Some Models)

Some models (especially Llama and other gated models) require you to accept license terms and authenticate:

1. **Create an Access Token:**
   - Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens){target=_blank}
   - Click "New token" and create a token with "Read" access
   - Copy the token (you will only see it once)

2. **Login via CLI:**
   ```bash
   huggingface-cli login
   ```
   Paste your token when prompted.

3. **Accept Model License (for gated models):**
   - Visit the model page (e.g., [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct){target=_blank})
   - Click "Access repository" and accept the license terms

!!! warning "Token Security"
    Treat your Hugging Face token like a password. Do not commit it to version control or share it publicly.

## Downloading Models

### Method 1: Using Ollama (Recommended for Beginners)

The easiest way to run Hugging Face models locally is through [Ollama](ollama.md), which handles all the complexity:

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.com/install.sh | sh

# Run popular models directly
ollama run llama3.2
ollama run mistral
ollama run qwen2.5
```

Ollama automatically downloads optimized versions of models from Hugging Face.

### Method 2: Using huggingface-cli

For more control, download models directly:

```bash
# Download a specific model
huggingface-cli download microsoft/Phi-3-mini-4k-instruct

# Download to a specific directory
huggingface-cli download microsoft/Phi-3-mini-4k-instruct --local-dir ./models/phi3

# Download only specific files (useful for large models)
huggingface-cli download meta-llama/Llama-3.2-1B --include "*.safetensors"
```

### Method 3: Using Python

```python
from huggingface_hub import snapshot_download

# Download entire model repository
model_path = snapshot_download(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    local_dir="./models/phi3"
)

print(f"Model downloaded to: {model_path}")
```

## Running Models Locally

Once downloaded, you can run models using various frameworks.

### Option 1: Transformers Library (Most Flexible)

The `transformers` library from Hugging Face is the standard for working with models:

```bash
pip install transformers torch accelerate
```

**Basic Text Generation Example:**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use half precision to save memory
    device_map="auto"           # Automatically use GPU if available
)

# Generate text
prompt = "Explain the process of photosynthesis in simple terms:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Option 2: llama.cpp (Efficient CPU/GPU Inference)

For running models efficiently on consumer hardware, `llama.cpp` provides optimized inference:

```bash
# Install llama-cpp-python
pip install llama-cpp-python

# Or with GPU support (CUDA)
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python
```

**Using GGUF Format Models:**

```python
from llama_cpp import Llama

# Download a GGUF model from Hugging Face
# Example: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF

llm = Llama(
    model_path="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=4096,      # Context window
    n_threads=8,     # CPU threads
    n_gpu_layers=35  # Layers to offload to GPU (0 for CPU-only)
)

output = llm(
    "What are the key differences between supervised and unsupervised learning?",
    max_tokens=300,
    temperature=0.7,
    echo=False
)

print(output["choices"][0]["text"])
```

### Option 3: Text Generation Web UI

For a graphical interface, [text-generation-webui](https://github.com/oobabooga/text-generation-webui){target=_blank} provides a ChatGPT-like experience for local models.

## Recommended Models for Beginners

Here are well-tested models suitable for different hardware configurations:

### Small Models (4-8GB RAM)

| Model | Size | Best For |
|-------|------|----------|
| [Phi-3-mini](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct){target=_blank} | 3.8B | General tasks, runs on laptops |
| [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct){target=_blank} | 3B | Multilingual, good reasoning |
| [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct){target=_blank} | 1B | Very fast, basic tasks |

### Medium Models (16-32GB RAM)

| Model | Size | Best For |
|-------|------|----------|
| [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct){target=_blank} | 3B | Balanced performance |
| [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3){target=_blank} | 7B | Excellent general purpose |
| [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct){target=_blank} | 7B | Strong reasoning, coding |

### Large Models (GPU Required)

| Model | Size | Best For |
|-------|------|----------|
| [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct){target=_blank} | 70B | Near-frontier performance |
| [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct){target=_blank} | 72B | State-of-the-art open model |
| [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1){target=_blank} | 671B | Advanced reasoning (requires cluster) |

!!! tip "Quantized Models"
    For running larger models on limited hardware, look for quantized versions (GGUF format). These reduce memory requirements with minimal quality loss. Search for model names with "GGUF" or visit [TheBloke](https://huggingface.co/TheBloke){target=_blank} for quantized versions.

## Downloading Datasets

### Using the datasets Library

```bash
pip install datasets
```

**Load a Dataset:**

```python
from datasets import load_dataset

# Load a dataset from the Hub
dataset = load_dataset("squad")  # Stanford Question Answering Dataset

# View dataset structure
print(dataset)
print(dataset["train"][0])  # First training example
```

**Download for Offline Use:**

```python
from datasets import load_dataset

# Download and cache locally
dataset = load_dataset(
    "scientific_papers",
    "arxiv",
    cache_dir="./data/scientific_papers"
)

# Save to disk in a specific format
dataset.save_to_disk("./data/arxiv_papers")
```

### Popular Academic Datasets

| Dataset | Description | Size |
|---------|-------------|------|
| [arxiv-papers](https://huggingface.co/datasets/nick007x/arxiv-papers){target=_blank} | ArXiv papers | 4.6TB of papers |
| [wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia){target=_blank} | Wikipedia articles | Multiple languages |
| [pile](https://huggingface.co/datasets/EleutherAI/pile){target=_blank} | Diverse text corpus | 800GB |
| [code_search_net](https://huggingface.co/datasets/code-search-net/code_search_net){target=_blank} | Code from GitHub | 6M functions |

## Spaces: Interactive Demos

[Hugging Face Spaces](https://huggingface.co/spaces){target=_blank} hosts interactive applications built with models:

- **Try before you download:** Test models in your browser
- **Share your work:** Deploy demos for papers or projects
- **Learn from examples:** See how others implement solutions

Most Spaces are built using [Gradio](gradio.md), an open-source Python library for creating web interfaces for ML models. You can build and deploy your own Gradio apps to Spaces with just a few lines of code. See our [Gradio documentation](gradio.md) for tutorials and examples.

**Notable Spaces for Researchers:**

- [Whisper](https://huggingface.co/spaces/openai/whisper){target=_blank} - Audio transcription
- [Document Question Answering](https://huggingface.co/spaces/impira/docquery){target=_blank} - Extract information from documents
- [Stable Diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion){target=_blank} - Image generation

## Best Practices

### Storage Management

Models can be large. Manage your cache:

```bash
# View cache usage
huggingface-cli scan-cache

# Delete unused models
huggingface-cli delete-cache
```

### Model Selection Tips

1. **Start small:** Begin with smaller models to test your workflow
2. **Check benchmarks:** Review model cards for performance on relevant tasks
3. **Consider licensing:** Ensure the license fits your use case (research vs. commercial)
4. **Read the limitations:** Model cards describe known issues and biases

### For Academic Use

- **Cite properly:** Model cards include citation information
- **Document your setup:** Record model versions and parameters for reproducibility
- **Check data provenance:** Understand what data was used to train the model

## Further Resources

- **Hugging Face Documentation:** [https://huggingface.co/docs](https://huggingface.co/docs){target=_blank}
- **Transformers Library:** [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers){target=_blank}
- **Hugging Face Course:** [https://huggingface.co/learn](https://huggingface.co/learn){target=_blank} (Free NLP course)
- **Model Hub:** [https://huggingface.co/models](https://huggingface.co/models){target=_blank}
- **Dataset Hub:** [https://huggingface.co/datasets](https://huggingface.co/datasets){target=_blank}
- **Spaces:** [https://huggingface.co/spaces](https://huggingface.co/spaces){target=_blank}
- **Gradio (for building Spaces):** See our [Gradio documentation](gradio.md) for tutorials on building interactive demos

!!! note "Hugging Face vs. Ollama"
    For most workshop participants, we recommend starting with [Ollama](ollama.md) for running local models. It handles model downloading and optimization automatically. Use Hugging Face directly when you need:

    - Access to specific model versions or configurations
    - Fine-tuning or training capabilities
    - Datasets for research
    - Models not available in Ollama's library
