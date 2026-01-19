# Gradio

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## What is Gradio?

[Gradio](https://gradio.app/){target=_blank} is an open-source Python library that makes it easy to create interactive web interfaces for machine learning models, data science applications, and AI tools. With just a few lines of code, you can build shareable demos that allow users to interact with your work through a web browser.

**Why Gradio Matters for Researchers:**

- **Share your work:** Create interactive demos of your research for papers, presentations, or collaborators
- **No web development required:** Build interfaces using only Python - no HTML, CSS, or JavaScript needed
- **Rapid prototyping:** Test and iterate on AI applications quickly
- **Accessibility:** Make your models accessible to non-technical colleagues and stakeholders
- **Reproducibility:** Package your research into interactive, shareable applications

!!! tip "Gradio and Hugging Face"
    Gradio is developed by [Hugging Face](huggingface.md) and integrates seamlessly with the Hugging Face ecosystem. Most interactive demos you see on [Hugging Face Spaces](https://huggingface.co/spaces){target=_blank} are built with Gradio. This makes it easy to deploy your Gradio apps to the cloud with a single command.

## Installation

### Basic Installation

=== "pip"

    ```bash
    pip install gradio
    ```

=== "conda"

    ```bash
    conda install -c conda-forge gradio
    ```

### Installation with Additional Dependencies

For working with Hugging Face models:

```bash
pip install gradio transformers torch
```

For working with audio and images:

```bash
pip install gradio numpy pillow soundfile
```

### Verify Installation

```python
import gradio as gr
print(gr.__version__)
```

As of early 2026, the current stable version is Gradio 5.x.

## Quick Start: Your First Gradio App

Let's build a simple interface that takes text input and returns a greeting:

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}! Welcome to Gradio."

# Create the interface
demo = gr.Interface(
    fn=greet,              # The function to wrap
    inputs="text",         # Input type
    outputs="text",        # Output type
    title="Simple Greeter",
    description="Enter your name to receive a greeting."
)

# Launch the app
demo.launch()
```

When you run this code, Gradio will:

1. Start a local web server (typically at `http://127.0.0.1:7860`)
2. Open your default browser to display the interface
3. Provide a shareable link if you set `share=True`

!!! info "Running in Jupyter Notebooks"
    Gradio works seamlessly in Jupyter notebooks. The interface will display inline within the notebook cell. This is perfect for iterative development and demonstrations.

## Core Concepts

### The Interface Class

`gr.Interface` is the simplest way to create a Gradio app. It wraps any Python function with a user interface:

```python
gr.Interface(
    fn=your_function,       # Required: The function to call
    inputs=input_components, # Required: Input component(s)
    outputs=output_components, # Required: Output component(s)
    title="App Title",      # Optional: Display title
    description="Description", # Optional: Help text
    examples=[["example1"], ["example2"]]  # Optional: Example inputs
)
```

### Common Input/Output Components

Gradio provides many component types:

| Component | Description | Example Use |
|-----------|-------------|-------------|
| `gr.Textbox` | Text input/output | Questions, prompts, responses |
| `gr.Number` | Numeric input | Parameters, scores |
| `gr.Slider` | Range selection | Temperature, confidence thresholds |
| `gr.Dropdown` | Selection from options | Model selection, categories |
| `gr.Checkbox` | Boolean toggle | Enable/disable features |
| `gr.Image` | Image upload/display | Vision models, image processing |
| `gr.Audio` | Audio upload/playback | Speech recognition, synthesis |
| `gr.File` | File upload | Document processing |
| `gr.Dataframe` | Tabular data | Data analysis results |
| `gr.Plot` | Charts and graphs | Visualizations |
| `gr.Markdown` | Formatted text | Instructions, results |

## Building Practical Applications

### Example 1: Text Summarization Interface

This example creates a tool for summarizing academic papers or long documents:

```python
import gradio as gr

def summarize_text(text, max_length, style):
    """
    A placeholder summarization function.
    In practice, you would connect this to an LLM.
    """
    # Simulate summarization
    word_count = len(text.split())
    summary = f"[{style} summary of {word_count} words, max {max_length} words]"

    # In real use, you would call an API or model here:
    # from transformers import pipeline
    # summarizer = pipeline("summarization")
    # result = summarizer(text, max_length=max_length)

    return summary

demo = gr.Interface(
    fn=summarize_text,
    inputs=[
        gr.Textbox(
            label="Text to Summarize",
            placeholder="Paste your article, paper abstract, or document here...",
            lines=10
        ),
        gr.Slider(
            minimum=50,
            maximum=500,
            value=150,
            step=10,
            label="Maximum Summary Length (words)"
        ),
        gr.Dropdown(
            choices=["Brief", "Detailed", "Technical", "Simplified"],
            value="Brief",
            label="Summary Style"
        )
    ],
    outputs=gr.Textbox(label="Summary", lines=5),
    title="Academic Text Summarizer",
    description="Paste text from papers, articles, or documents to generate a summary.",
    examples=[
        ["Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.", 100, "Brief"],
    ]
)

demo.launch()
```

### Example 2: Image Classification with Hugging Face Models

This example demonstrates how to connect Gradio to a Hugging Face model. For more on accessing Hugging Face models, see the [Hugging Face documentation](huggingface.md).

```python
import gradio as gr
from transformers import pipeline

# Load a pre-trained image classification model from Hugging Face
# See https://huggingface.co/models?pipeline_tag=image-classification
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

def classify_image(image):
    """Classify an uploaded image and return top predictions."""
    if image is None:
        return "Please upload an image."

    # Run classification
    predictions = classifier(image)

    # Format results
    results = "\n".join([
        f"{pred['label']}: {pred['score']:.2%}"
        for pred in predictions[:5]
    ])

    return results

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Textbox(label="Classification Results", lines=6),
    title="Image Classifier",
    description="Upload an image to classify its contents using a Vision Transformer model from Hugging Face.",
    examples=[
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"]
    ]
)

demo.launch()
```

!!! note "First Run Download"
    The first time you run this code, the `transformers` library will download the model from Hugging Face. This may take a few minutes depending on your internet connection. Subsequent runs will use the cached model.

### Example 3: Question Answering with Context

This example creates a research assistant that answers questions based on provided context:

```python
import gradio as gr
from transformers import pipeline

# Load a question-answering model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(context, question):
    """Answer a question based on the provided context."""
    if not context or not question:
        return "Please provide both context and a question."

    result = qa_model(question=question, context=context)

    answer = result['answer']
    confidence = result['score']

    return f"**Answer:** {answer}\n\n**Confidence:** {confidence:.2%}"

demo = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(
            label="Context",
            placeholder="Paste the text passage that contains the answer...",
            lines=8
        ),
        gr.Textbox(
            label="Question",
            placeholder="Ask a question about the text above..."
        )
    ],
    outputs=gr.Markdown(label="Answer"),
    title="Research Document Q&A",
    description="Paste a passage from a paper or document, then ask questions about it.",
    examples=[
        [
            "The transformer architecture was introduced in the paper 'Attention Is All You Need' by Vaswani et al. in 2017. It revolutionized natural language processing by replacing recurrent neural networks with self-attention mechanisms, enabling much faster training through parallelization.",
            "When was the transformer architecture introduced?"
        ],
        [
            "CRISPR-Cas9 is a genome editing technology that allows scientists to make precise changes to DNA. It works by using a guide RNA to direct the Cas9 enzyme to a specific location in the genome, where it makes a cut. The cell's natural repair mechanisms then make the desired edit.",
            "How does CRISPR-Cas9 work?"
        ]
    ]
)

demo.launch()
```

### Example 4: Multi-Modal Interface with Blocks

For more complex layouts, use `gr.Blocks` instead of `gr.Interface`:

```python
import gradio as gr

def analyze_data(file, analysis_type):
    """Placeholder for data analysis function."""
    if file is None:
        return "Please upload a file.", None

    # In practice, you would process the file here
    # import pandas as pd
    # df = pd.read_csv(file.name)

    summary = f"Analysis type: {analysis_type}\nFile uploaded successfully."

    # Generate a placeholder plot
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label='Sample Data')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title(f'{analysis_type} Results')
    ax.legend()

    return summary, fig

# Create a more complex layout with Blocks
with gr.Blocks(title="Research Data Analyzer") as demo:
    gr.Markdown("# Research Data Analyzer")
    gr.Markdown("Upload your data file and select an analysis type.")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="Upload Data File (CSV, Excel)")
            analysis_dropdown = gr.Dropdown(
                choices=["Descriptive Statistics", "Correlation Analysis",
                         "Trend Analysis", "Outlier Detection"],
                label="Analysis Type",
                value="Descriptive Statistics"
            )
            analyze_btn = gr.Button("Run Analysis", variant="primary")

        with gr.Column(scale=2):
            output_text = gr.Textbox(label="Analysis Summary", lines=5)
            output_plot = gr.Plot(label="Visualization")

    analyze_btn.click(
        fn=analyze_data,
        inputs=[file_input, analysis_dropdown],
        outputs=[output_text, output_plot]
    )

demo.launch()
```

## Connecting to Large Language Models

### Using Hugging Face Inference API

Connect to models hosted on Hugging Face without downloading them locally:

```python
import gradio as gr
from huggingface_hub import InferenceClient

# Initialize the client (requires HF_TOKEN environment variable or explicit token)
# See the Hugging Face documentation for setting up authentication:
# https://huggingface.co/docs/huggingface_hub/quick-start#authentication
client = InferenceClient()

def chat_with_model(message, history, system_prompt, model_name):
    """Chat with a Hugging Face model via the Inference API."""

    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})

    # Add current message
    messages.append({"role": "user", "content": message})

    # Generate response
    response = client.chat_completion(
        model=model_name,
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(
    fn=chat_with_model,
    additional_inputs=[
        gr.Textbox(
            value="You are a helpful research assistant specializing in academic writing.",
            label="System Prompt",
            lines=2
        ),
        gr.Dropdown(
            choices=[
                "meta-llama/Llama-3.2-3B-Instruct",
                "mistralai/Mistral-7B-Instruct-v0.3",
                "Qwen/Qwen2.5-7B-Instruct"
            ],
            value="meta-llama/Llama-3.2-3B-Instruct",
            label="Model"
        )
    ],
    title="Research Assistant Chatbot",
    description="Chat with open-source LLMs from Hugging Face. Select a model and customize the system prompt."
)

demo.launch()
```

!!! warning "API Rate Limits"
    The Hugging Face Inference API has rate limits for free users. For heavy usage, consider a [Hugging Face Pro subscription](https://huggingface.co/pricing){target=_blank} or running models locally with [Ollama](ollama.md).

### Using Local Models with Ollama

Connect Gradio to locally-running models via [Ollama](ollama.md):

```python
import gradio as gr
import requests
import json

def chat_with_ollama(message, history, model_name):
    """Chat with a local Ollama model."""

    # Build conversation context
    full_prompt = ""
    for human, assistant in history:
        full_prompt += f"User: {human}\nAssistant: {assistant}\n"
    full_prompt += f"User: {message}\nAssistant:"

    # Call Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model_name,
            "prompt": full_prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"

demo = gr.ChatInterface(
    fn=chat_with_ollama,
    additional_inputs=[
        gr.Dropdown(
            choices=["llama3.2", "mistral", "qwen2.5", "deepseek-r1:8b"],
            value="llama3.2",
            label="Local Model (Ollama)"
        )
    ],
    title="Local AI Chat",
    description="Chat with AI models running locally on your machine via Ollama."
)

demo.launch()
```

## Deploying to Hugging Face Spaces

[Hugging Face Spaces](https://huggingface.co/spaces){target=_blank} provides free hosting for Gradio applications. This is the easiest way to share your work with collaborators or the public.

### Method 1: Deploy from the Command Line

1. **Install the Hugging Face CLI:**

    ```bash
    pip install huggingface_hub
    ```

2. **Log in to Hugging Face:**

    ```bash
    huggingface-cli login
    ```

3. **Create your app file (`app.py`):**

    ```python
    import gradio as gr

    def my_function(input_text):
        return f"You said: {input_text}"

    demo = gr.Interface(fn=my_function, inputs="text", outputs="text")
    demo.launch()
    ```

4. **Create a `requirements.txt` file:**

    ```
    gradio
    transformers
    torch
    ```

5. **Deploy using the Gradio CLI:**

    ```bash
    gradio deploy
    ```

    Follow the prompts to name your Space and configure settings.

### Method 2: Create a Space on the Web

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space){target=_blank}
2. Choose "Gradio" as the SDK
3. Name your Space and set visibility (public or private)
4. Upload your `app.py` and `requirements.txt` files
5. The Space will automatically build and deploy

### Method 3: Use the Share Feature

For quick sharing without permanent hosting:

```python
demo.launch(share=True)
```

This creates a temporary public URL (valid for 72 hours) that anyone can access.

!!! tip "Space Hardware"
    Free Hugging Face Spaces run on basic CPU hardware. For GPU-accelerated models, you can upgrade to paid hardware tiers. See [Hugging Face Spaces documentation](https://huggingface.co/docs/hub/spaces-overview){target=_blank} for options.

## Best Practices

### For Academic Applications

1. **Add clear documentation:** Use `gr.Markdown` to explain what your tool does and how to use it
2. **Provide examples:** Include representative examples that demonstrate the tool's capabilities
3. **Handle errors gracefully:** Validate inputs and provide helpful error messages
4. **Include citations:** Add references to papers or methods your tool is based on

### Performance Tips

1. **Cache expensive operations:**
    ```python
    from functools import lru_cache

    @lru_cache(maxsize=100)
    def expensive_computation(input_data):
        # This result will be cached
        return process(input_data)
    ```

2. **Use queuing for concurrent users:**
    ```python
    demo.launch(enable_queue=True)
    ```

3. **Stream long outputs:**
    ```python
    def generate_text(prompt):
        for word in long_response.split():
            yield word + " "

    demo = gr.Interface(fn=generate_text, inputs="text", outputs="text")
    ```

### Security Considerations

- Never expose API keys in your code - use environment variables
- Be cautious with file uploads - validate file types and sizes
- Consider rate limiting for public applications
- Review Gradio's [security guidelines](https://www.gradio.app/guides/sharing-your-app#security-and-file-access){target=_blank}

## Further Resources

- **Gradio Documentation:** [https://www.gradio.app/docs/](https://www.gradio.app/docs/){target=_blank}
- **Gradio Guides:** [https://www.gradio.app/guides/](https://www.gradio.app/guides/){target=_blank}
- **Hugging Face Spaces:** [https://huggingface.co/spaces](https://huggingface.co/spaces){target=_blank}
- **Example Spaces Gallery:** [https://huggingface.co/spaces](https://huggingface.co/spaces){target=_blank} (browse for inspiration)
- **Gradio GitHub:** [https://github.com/gradio-app/gradio](https://github.com/gradio-app/gradio){target=_blank}

## Related Workshop Materials

- **[Hugging Face](huggingface.md):** Learn how to find and use pre-trained models for your Gradio apps
- **[Ollama](ollama.md):** Run local models that can power your Gradio interfaces
- **[Jupyter AI](jupyter.md):** Integrate AI assistants into your notebook workflows
- **[Code Execution](execution.md):** Understand safe practices for running code in AI applications
