# :simple-posit: Posit (RStudio)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Overview

[Posit](https://posit.co/){target=_blank} (formerly RStudio) is a company dedicated to creating open-source data science tools. Their ecosystem includes:

- **RStudio Desktop/Server** - The classic IDE for R programming
- **Positron** - A next-generation data science IDE built on VS Code
- **Quarto** - A scientific publishing system
- **Shiny** - Web application framework for R and Python
- **tidyverse/tidymodels** - Popular R package collections

Posit has developed powerful LLM integration packages that work across their IDEs:

| Package | Language | Description |
|---------|----------|-------------|
| [ellmer](https://ellmer.tidyverse.org/){target=_blank} | R | Unified interface for 20+ LLM providers |
| [chatlas](https://posit-dev.github.io/chatlas/){target=_blank} | Python | LLM chat framework with streaming and tool calling |

These packages allow researchers to integrate AI assistance directly into their data analysis workflows, from interactive exploration to reproducible reports.

## Why Use Posit Tools for AI?

**For R Users:**

- Native integration with tidyverse workflows
- Seamless use in R Markdown and Quarto documents
- Support for both cloud APIs and local models via Ollama
- Interactive chat within the IDE console

**For Python Users:**

- Model-agnostic design for easy provider switching
- Automatic streaming in notebooks and consoles
- Tool calling for agentic capabilities
- Async support for scalable applications

**For Academic Research:**

- Reproducible AI-assisted analysis pipelines
- Local model support for sensitive data
- Easy switching between providers for cost optimization
- Integration with Quarto for publishable documents

---

## Installation: Positron (Beta)

[Positron](https://github.com/posit-dev/positron){target=_blank} is Posit's next-generation data science IDE. Built on VS Code's foundation, it provides native support for Python, R, and AI-assisted coding with a familiar interface for data scientists.

!!! info "Current Version: 2026.01.0-147 (January 2026)"
    Positron is in active beta development. While stable for daily use, expect continued improvements and occasional breaking changes.

### System Requirements

| Platform | Requirement |
|----------|-------------|
| **Windows** | Windows 10 or 11 (x64) |
| **macOS** | macOS 11.0+ (Apple Silicon or Intel) |
| **Linux** | Ubuntu 20+ or RHEL 9 |

### macOS Installation

=== "Apple Silicon (M1/M2/M3/M4)"

    1. Download [Positron-2026.01.0-147-arm64.dmg](https://positron.posit.co/download){target=_blank} (~598 MB)
    2. Open the downloaded `.dmg` file
    3. Drag Positron to your Applications folder
    4. Launch Positron from Applications
    5. If prompted about an unidentified developer, go to System Preferences > Security & Privacy and click "Open Anyway"

=== "Intel Mac"

    1. Download [Positron-2026.01.0-147-x64.dmg](https://positron.posit.co/download){target=_blank} (~601 MB)
    2. Open the downloaded `.dmg` file
    3. Drag Positron to your Applications folder
    4. Launch Positron from Applications

### Windows Installation

=== "System-wide (Recommended)"

    1. Download [Positron-2026.01.0-147-Setup-x64.exe](https://positron.posit.co/download){target=_blank} (~315 MB)
    2. Run the installer with administrator privileges
    3. Follow the installation wizard prompts
    4. Launch Positron from the Start menu

=== "User Installation (No Admin)"

    1. Download [Positron-2026.01.0-147-UserSetup-x64.exe](https://positron.posit.co/download){target=_blank} (~315 MB)
    2. Run the installer (no admin rights needed)
    3. Follow the installation wizard prompts
    4. Launch Positron from the Start menu

### Linux Installation

=== "Ubuntu/Debian"

    ```bash
    # Download the .deb package (x64)
    wget https://github.com/posit-dev/positron/releases/download/2026.01.0-147/Positron-2026.01.0-147-x64.deb

    # Install with dpkg
    sudo dpkg -i Positron-2026.01.0-147-x64.deb

    # Fix any dependency issues
    sudo apt-get install -f

    # Launch Positron
    positron
    ```

    For ARM64 systems, download `Positron-2026.01.0-147-arm64.deb` instead.

=== "Fedora/RHEL/CentOS"

    ```bash
    # Download the .rpm package (x64)
    wget https://github.com/posit-dev/positron/releases/download/2026.01.0-147/Positron-2026.01.0-147-x64.rpm

    # Install with dnf (Fedora/RHEL 8+)
    sudo dnf install Positron-2026.01.0-147-x64.rpm

    # Or with yum (older systems)
    sudo yum localinstall Positron-2026.01.0-147-x64.rpm

    # Launch Positron
    positron
    ```

### Positron Key Features

- **Multi-language Console** - Switch between R and Python in the same session
- **Variables Pane** - Inspect data frames, lists, and objects visually
- **Data Viewer** - Explore large datasets with filtering and sorting
- **Plot Pane** - View and export visualizations
- **VS Code Extensions** - Access the full VS Code extension marketplace
- **Quarto Integration** - Native support for scientific publishing

---

## Installation: RStudio Desktop

[RStudio Desktop](https://posit.co/download/rstudio-desktop/){target=_blank} is the classic, mature IDE for R development used by millions of data scientists and researchers.

### macOS Installation

1. Visit [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/){target=_blank}
2. Download the macOS installer (`.dmg`)
3. Open the downloaded file
4. Drag RStudio to your Applications folder
5. Launch RStudio from Applications

!!! note "R Required"
    RStudio requires R to be installed. Download R from [CRAN](https://cran.r-project.org/){target=_blank} before installing RStudio.

### Windows Installation

1. Visit [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/){target=_blank}
2. Download the Windows installer (`.exe`)
3. Run the installer and follow the prompts
4. Launch RStudio from the Start menu

### Linux Installation

=== "Ubuntu/Debian"

    ```bash
    # Install R first (if not already installed)
    sudo apt update
    sudo apt install r-base r-base-dev

    # Download RStudio (check website for latest version)
    wget https://download1.rstudio.org/electron/jammy/amd64/rstudio-2024.12.0-467-amd64.deb

    # Install RStudio
    sudo dpkg -i rstudio-2024.12.0-467-amd64.deb

    # Fix dependencies if needed
    sudo apt-get install -f
    ```

=== "Fedora/RHEL"

    ```bash
    # Install R first
    sudo dnf install R

    # Download RStudio (check website for latest version)
    wget https://download1.rstudio.org/electron/rhel9/x86_64/rstudio-2024.12.0-467-x86_64.rpm

    # Install RStudio
    sudo dnf install rstudio-2024.12.0-467-x86_64.rpm
    ```

---

## Installation: RStudio Server

[RStudio Server](https://posit.co/download/rstudio-server/){target=_blank} provides browser-based access to RStudio, ideal for:

- Shared research computing environments
- HPC cluster access
- Cloud deployments
- Teaching labs

### Ubuntu/Debian Installation

```bash
# Install R
sudo apt update
sudo apt install r-base r-base-dev

# Install RStudio Server dependencies
sudo apt install gdebi-core

# Download RStudio Server
wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2024.12.0-467-amd64.deb

# Install RStudio Server
sudo gdebi rstudio-server-2024.12.0-467-amd64.deb
```

### Fedora/RHEL Installation

```bash
# Install R
sudo dnf install R

# Download RStudio Server
wget https://download2.rstudio.org/server/rhel9/x86_64/rstudio-server-rhel-2024.12.0-467-x86_64.rpm

# Install RStudio Server
sudo dnf install rstudio-server-rhel-2024.12.0-467-x86_64.rpm
```

### Starting and Managing the Server

```bash
# Start RStudio Server
sudo systemctl start rstudio-server

# Enable on boot
sudo systemctl enable rstudio-server

# Check status
sudo systemctl status rstudio-server

# View logs
sudo journalctl -u rstudio-server
```

### Accessing RStudio Server

After installation, access RStudio Server at:

```
http://your-server-ip:8787
```

Log in with your Linux system credentials.

!!! warning "Security Configuration"
    For production deployments, configure:

    - SSL/TLS certificates for HTTPS
    - Firewall rules to restrict access
    - Authentication integration (LDAP, PAM)

    See the [RStudio Server Admin Guide](https://docs.posit.co/ide/server-pro/){target=_blank} for details.

---

## ellmer: R Package for LLMs

[ellmer](https://ellmer.tidyverse.org/){target=_blank} is Posit's R package that makes it easy to use large language models from R. It provides a unified interface for 20+ providers with support for streaming, tool calling, and structured data extraction.

### Installation

```r
# Install from CRAN
install.packages("ellmer")

# Or install development version from GitHub
# install.packages("pak")
pak::pak("tidyverse/ellmer")
```

### Supported Providers

ellmer supports a wide range of LLM providers:

| Provider | Function | Notes |
|----------|----------|-------|
| OpenAI | `chat_openai()` | GPT-4.1, GPT-4o, o3 models |
| Anthropic | `chat_anthropic()` | Claude 4.5 models |
| Google | `chat_google_gemini()` | Gemini models |
| Azure OpenAI | `chat_azure_openai()` | Enterprise Azure deployment |
| AWS Bedrock | `chat_aws_bedrock()` | Multiple models via AWS |
| Ollama | `chat_ollama()` | Local models (free) |
| Mistral | `chat_mistral()` | Mistral models |
| Groq | `chat_groq()` | Fast inference |
| DeepSeek | `chat_deepseek()` | DeepSeek models |
| Hugging Face | `chat_huggingface()` | HF Inference API |
| GitHub Models | `chat_github()` | GitHub model marketplace |
| Perplexity | `chat_perplexity()` | Search-augmented |
| OpenRouter | `chat_openrouter()` | Multi-provider gateway |

### Basic Usage

```r
library(ellmer)

# Create a chat with OpenAI
chat <- chat_openai(
  model = "gpt-4o-mini",
  system_prompt = "You are a helpful data science assistant."
)

# Have a conversation
chat$chat("What is the tidyverse?")

# Continue the conversation (context is retained)
chat$chat("Which packages are included?")

# View token usage
chat$token_usage()
```

### Using Anthropic Claude

```r
library(ellmer)

# Create a chat with Claude
chat <- chat_anthropic(
  model = "claude-sonnet-4-5-20250514",
  system_prompt = "You are an expert R programmer."
)

# Ask about R code
chat$chat("How do I read a CSV file with readr?")
```

### Streaming Responses

```r
library(ellmer)

chat <- chat_openai(model = "gpt-4o-mini")

# Stream the response to the console
chat$chat("Explain the central limit theorem", echo = "all")
```

### Structured Data Extraction

ellmer can extract structured data from text:

```r
library(ellmer)

# Define the structure you want to extract
paper_info <- type_object(
  title = type_string("The paper title"),
  authors = type_array(type_string("Author names")),
  year = type_integer("Publication year"),
  journal = type_string("Journal name")
)

chat <- chat_openai(model = "gpt-4o-mini")

# Extract structured information
result <- chat$extract_data(
  "Smith, J., & Jones, M. (2024). Machine learning in ecology.
   Nature Ecology & Evolution, 8(3), 234-245.",
  type = paper_info
)

print(result)
# $title
# [1] "Machine learning in ecology"
#
# $authors
# [1] "Smith, J." "Jones, M."
#
# $year
# [1] 2024
#
# $journal
# [1] "Nature Ecology & Evolution"
```

### Tool Calling (Function Calling)

Enable the model to call R functions:

```r
library(ellmer)

# Define a tool
get_weather <- function(city) {
  # In practice, this would call a weather API
  paste("The weather in", city, "is sunny and 72F")
}

chat <- chat_openai(
  model = "gpt-4o-mini",
  system_prompt = "You help users with weather information."
)

# Register the tool
chat$register_tool(
  name = "get_weather",
  description = "Get the current weather for a city",
  arguments = list(
    city = type_string("The city name")
  ),
  fn = get_weather
)

# The model will call the function when appropriate
chat$chat("What's the weather like in Phoenix?")
```

---

## chatlas: Python Package for LLMs

[chatlas](https://posit-dev.github.io/chatlas/){target=_blank} is Posit's Python package for building LLM chat applications. It provides automatic streaming, tool calling, and a model-agnostic design.

### Installation

```bash
pip install -U chatlas
```

### Supported Providers

| Provider | Class | Notes |
|----------|-------|-------|
| OpenAI | `ChatOpenAI` | GPT-4.1, GPT-4o models |
| Anthropic | `ChatAnthropic` | Claude 4.5 models |
| Google | `ChatGoogle` | Gemini models |
| Azure OpenAI | `ChatAzureOpenAI` | Enterprise Azure |
| AWS Bedrock | `ChatBedrockAnthropic` | Claude via AWS |
| Ollama | `ChatOllama` | Local models (free) |
| Mistral | `ChatMistral` | Mistral models |
| Groq | `ChatGroq` | Fast inference |
| DeepSeek | `ChatDeepSeek` | DeepSeek models |
| Hugging Face | `ChatHuggingFace` | HF Inference API |
| Any Provider | `ChatAuto` | Auto-detect provider |

### Basic Usage

```python
from chatlas import ChatOpenAI

# Create a chat
chat = ChatOpenAI(
    model="gpt-4o-mini",
    system_prompt="You are a helpful data science assistant."
)

# Have a conversation
chat.chat("What is pandas in Python?")

# Continue the conversation
chat.chat("How do I read a CSV file?")
```

### Using Anthropic Claude

```python
from chatlas import ChatAnthropic

chat = ChatAnthropic(
    model="claude-sonnet-4-5-20250514",
    system_prompt="You are an expert Python programmer."
)

chat.chat("How do I create a scatter plot with matplotlib?")
```

### Tool Calling

```python
from chatlas import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-4o-mini",
    system_prompt="You help users with weather information."
)

# Define a tool as a Python function
def get_current_weather(city: str) -> str:
    """Get the current weather for a city."""
    # In practice, call a weather API
    return f"The weather in {city} is sunny and 72F"

# Register the tool
chat.register_tool(get_current_weather)

# The model will call the function when needed
chat.chat("What's the weather in Tucson?")
```

### Structured Data Extraction

```python
from chatlas import ChatOpenAI
from pydantic import BaseModel

# Define structure with Pydantic
class PaperInfo(BaseModel):
    title: str
    authors: list[str]
    year: int
    journal: str

chat = ChatOpenAI(model="gpt-4o-mini")

# Extract structured data
result = chat.extract_data(
    "Smith, J., & Jones, M. (2024). Machine learning in ecology. "
    "Nature Ecology & Evolution, 8(3), 234-245.",
    data_model=PaperInfo
)

print(result)
# title='Machine learning in ecology' authors=['Smith, J.', 'Jones, M.']
# year=2024 journal='Nature Ecology & Evolution'
```

### Parallel and Batch Processing

```python
from chatlas import ChatOpenAI, parallel_chat_text

chat = ChatOpenAI(model="gpt-4o-mini")

# Process multiple prompts in parallel
prompts = [
    "Summarize the scientific method",
    "Explain photosynthesis",
    "Describe natural selection"
]

results = parallel_chat_text(chat, prompts)
for prompt, result in zip(prompts, results):
    print(f"Q: {prompt}\nA: {result}\n")
```

---

## API Key Setup

Both ellmer and chatlas require API keys for cloud providers. Here's how to set them up securely.

### Setting Environment Variables

!!! warning "Security Best Practices"
    - Never commit API keys to version control (Git)
    - Never hardcode keys in scripts
    - Use environment variables or secure credential management
    - Rotate keys periodically

#### Method 1: .Renviron File (Recommended for R)

Create or edit `~/.Renviron` in your home directory:

```bash
# OpenAI
OPENAI_API_KEY=sk-your-openai-key-here

# Anthropic
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here

# Google
GOOGLE_API_KEY=your-google-api-key-here

# Mistral
MISTRAL_API_KEY=your-mistral-key-here

# Groq
GROQ_API_KEY=your-groq-key-here
```

Restart R/RStudio after editing `.Renviron`.

#### Method 2: .env File (Python)

Create a `.env` file in your project directory:

```bash
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
GOOGLE_API_KEY=your-google-api-key-here
```

Load with `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()

from chatlas import ChatOpenAI
chat = ChatOpenAI()  # Automatically uses OPENAI_API_KEY
```

#### Method 3: Shell Configuration

Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
export OPENAI_API_KEY="sk-your-openai-key-here"
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key-here"
```

Reload your shell: `source ~/.bashrc`

### Obtaining API Keys

| Provider | Where to Get Key | Pricing |
|----------|------------------|---------|
| OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys){target=_blank} | Pay-per-token |
| Anthropic | [console.anthropic.com](https://console.anthropic.com/){target=_blank} | Pay-per-token |
| Google | [aistudio.google.com](https://aistudio.google.com/){target=_blank} | Free tier + paid |
| Mistral | [console.mistral.ai](https://console.mistral.ai/){target=_blank} | Pay-per-token |
| Groq | [console.groq.com](https://console.groq.com/){target=_blank} | Free tier available |

### Verifying Your Setup (R)

```r
library(ellmer)

# Test OpenAI
tryCatch({
  chat <- chat_openai(model = "gpt-4o-mini")
  chat$chat("Say hello!")
  message("OpenAI API key is working!")
}, error = function(e) {
  message("OpenAI API key issue: ", e$message)
})

# Test Anthropic
tryCatch({
  chat <- chat_anthropic(model = "claude-sonnet-4-5-20250514")
  chat$chat("Say hello!")
  message("Anthropic API key is working!")
}, error = function(e) {
  message("Anthropic API key issue: ", e$message)
})
```

### Verifying Your Setup (Python)

```python
from chatlas import ChatOpenAI, ChatAnthropic

# Test OpenAI
try:
    chat = ChatOpenAI(model="gpt-4o-mini")
    chat.chat("Say hello!")
    print("OpenAI API key is working!")
except Exception as e:
    print(f"OpenAI API key issue: {e}")

# Test Anthropic
try:
    chat = ChatAnthropic(model="claude-sonnet-4-5-20250514")
    chat.chat("Say hello!")
    print("Anthropic API key is working!")
except Exception as e:
    print(f"Anthropic API key issue: {e}")
```

---

## Ollama Integration (Local Models)

Both ellmer and chatlas support [Ollama](ollama.md) for running LLMs locally. This is ideal for:

- **Privacy** - Data never leaves your computer
- **Cost** - No API charges after initial setup
- **Offline access** - Work without internet
- **Experimentation** - Unlimited usage for testing

### Prerequisites

1. Install Ollama following our [Ollama guide](ollama.md)
2. Download a model:
   ```bash
   ollama pull llama3.2
   ```
3. Verify Ollama is running:
   ```bash
   curl http://localhost:11434/api/tags
   ```

### Using Ollama with ellmer (R)

```r
library(ellmer)

# List available Ollama models
models_ollama()

# Create a chat with a local model
chat <- chat_ollama(
  model = "llama3.2",
  system_prompt = "You are a helpful research assistant."
)

# Chat with the local model
chat$chat("Explain the difference between correlation and causation")
```

**Custom Ollama Server:**

```r
# Connect to Ollama on a different host
chat <- chat_ollama(
  model = "llama3.2",
  base_url = "http://192.168.1.100:11434"  # Remote Ollama server
)
```

**Available Parameters:**

```r
chat <- chat_ollama(
  model = "llama3.2",
  system_prompt = "You are a statistics tutor.",
  params = params(
    temperature = 0.7,  # Creativity (0-2)
    num_ctx = 4096      # Context window size
  )
)
```

### Using Ollama with chatlas (Python)

```python
from chatlas import ChatOllama

# Create a chat with a local model
chat = ChatOllama(
    model="llama3.2",
    system_prompt="You are a helpful research assistant."
)

# Chat with the local model
chat.chat("What are the assumptions of linear regression?")
```

**Custom Configuration:**

```python
from chatlas import ChatOllama

chat = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",  # Default
    system_prompt="You are an expert statistician.",
    temperature=0.7,
    num_ctx=4096
)
```

### Complete Ollama Workflow Example (R)

```r
library(ellmer)
library(tidyverse)

# 1. Create an Ollama chat for data analysis assistance
analyst <- chat_ollama(
  model = "llama3.2",
  system_prompt = "You are a data analysis expert. Provide R code examples
                   using tidyverse packages. Be concise and practical."
)

# 2. Get help with data manipulation
analyst$chat("How do I group data by multiple columns and calculate
              summary statistics in dplyr?")

# 3. The model provides code - let's use it
mtcars %>%
  group_by(cyl, gear) %>%
  summarise(
    mean_mpg = mean(mpg),
    sd_mpg = sd(mpg),
    n = n(),
    .groups = "drop"
  )

# 4. Ask follow-up questions
analyst$chat("How can I visualize this with ggplot2?")
```

### Complete Ollama Workflow Example (Python)

```python
from chatlas import ChatOllama
import pandas as pd

# 1. Create an Ollama chat for data analysis
analyst = ChatOllama(
    model="llama3.2",
    system_prompt="""You are a data analysis expert. Provide Python code
                     examples using pandas and matplotlib. Be concise."""
)

# 2. Get help with data manipulation
analyst.chat("How do I group data by multiple columns and calculate "
             "summary statistics in pandas?")

# 3. Apply the suggested code
import seaborn as sns
df = sns.load_dataset("tips")

summary = df.groupby(["day", "time"]).agg({
    "total_bill": ["mean", "std", "count"],
    "tip": ["mean", "std"]
}).round(2)

print(summary)

# 4. Ask follow-up questions
analyst.chat("How can I create a grouped bar chart of this summary?")
```

### Recommended Ollama Models for R/Python Work

| Model | Size | Best For |
|-------|------|----------|
| `llama3.2:3b` | ~2GB | Quick responses, basic coding |
| `qwen2.5:7b` | ~4.5GB | Reasoning, data analysis |
| `deepseek-coder:6.7b` | ~4GB | Code generation |
| `deepseek-r1:8b` | ~5GB | Complex reasoning |
| `codellama:13b` | ~7GB | Advanced coding |

```bash
# Download recommended models
ollama pull llama3.2:3b
ollama pull qwen2.5:7b
ollama pull deepseek-coder:6.7b
```

---

## Practical Examples

### Example 1: Literature Review Assistant (R)

```r
library(ellmer)
library(tidyverse)

# Create a specialized assistant
lit_review <- chat_ollama(
  model = "qwen2.5:7b",
  system_prompt = "You are an academic research assistant specializing in
                   literature reviews. Help researchers:
                   1. Identify key themes in abstracts
                   2. Suggest search terms
                   3. Evaluate methodology descriptions
                   Be scholarly but accessible."
)

# Analyze an abstract
abstract <- "This study examines the impact of social media use on
adolescent mental health using a longitudinal design with 5,000 participants
over 3 years. We found significant associations between daily social media
time and symptoms of anxiety and depression, with effect sizes varying by
platform type and usage patterns."

lit_review$chat(paste("Analyze this abstract and identify:",
                      "1. Research question",
                      "2. Methodology strengths",
                      "3. Potential limitations",
                      "4. Related search terms for similar studies",
                      "\n\nAbstract:", abstract))
```

### Example 2: Statistical Analysis Helper (R)

```r
library(ellmer)

# Create a statistics tutor
stats_help <- chat_ollama(
  model = "llama3.2",
  system_prompt = "You are a patient statistics tutor for graduate students.
                   When explaining:
                   1. Start with intuition before formulas
                   2. Use concrete examples
                   3. Show R code for implementation
                   4. Explain when methods are appropriate"
)

# Get help choosing a statistical test
stats_help$chat("I have a dataset with one continuous outcome variable and
                 two categorical predictors (treatment group with 3 levels,
                 and gender with 2 levels). I want to understand if there's
                 an interaction effect. What test should I use and why?")
```

### Example 3: Code Documentation Generator (R)

```r
library(ellmer)

# Create a documentation assistant
doc_helper <- chat_openai(
  model = "gpt-4o-mini",
  system_prompt = "You are an R documentation expert. When given R code,
                   generate roxygen2-style documentation including:
                   @title, @description, @param, @return, @examples"
)

# Generate documentation for a function
my_function <- "
calculate_effect_size <- function(group1, group2, pooled_sd = TRUE) {
  n1 <- length(group1)
  n2 <- length(group2)
  m1 <- mean(group1)
  m2 <- mean(group2)

  if (pooled_sd) {
    s <- sqrt(((n1-1)*var(group1) + (n2-1)*var(group2)) / (n1+n2-2))
  } else {
    s <- sd(c(group1, group2))
  }

  d <- (m1 - m2) / s
  return(list(cohens_d = d, n1 = n1, n2 = n2))
}
"

doc_helper$chat(paste("Generate roxygen2 documentation for this R function:\n",
                      my_function))
```

### Example 4: Data Analysis Pipeline (Python)

```python
from chatlas import ChatOllama
import pandas as pd
import numpy as np

# Create an analysis assistant
analyst = ChatOllama(
    model="llama3.2",
    system_prompt="""You are a data science assistant. When helping with
                     analysis:
                     1. Explain your reasoning
                     2. Provide complete, runnable Python code
                     3. Suggest visualizations when appropriate
                     4. Note potential issues or assumptions"""
)

# Load some data
np.random.seed(42)
df = pd.DataFrame({
    "treatment": np.random.choice(["A", "B", "C"], 100),
    "age": np.random.normal(45, 10, 100),
    "outcome": np.random.normal(50, 15, 100) +
               np.where(np.random.choice(["A", "B", "C"], 100) == "A", 10, 0)
})

# Get analysis suggestions
analyst.chat(f"""I have a dataset with these characteristics:
{df.describe().to_string()}

Columns: treatment (A/B/C), age (continuous), outcome (continuous)

What analysis would you recommend to understand the relationship
between treatment and outcome while controlling for age?""")
```

### Example 5: Quarto Document with AI (R Markdown/Quarto)

Create a Quarto document that uses ellmer for AI-assisted analysis:

````markdown
---
title: "AI-Assisted Data Analysis"
format: html
---

```{r setup, include=FALSE}
library(ellmer)
library(tidyverse)

# Use a local model for reproducibility
chat <- chat_ollama(model = "llama3.2")
```

## Data Overview

```{r}
# Load and summarize data
data(mtcars)
summary(mtcars)
```

## AI-Generated Analysis Suggestions

```{r}
# Ask the AI for analysis suggestions
response <- chat$chat(
  paste("Given a dataset about cars with variables:",
        paste(names(mtcars), collapse = ", "),
        "suggest three interesting analyses and visualizations."),
  echo = FALSE
)
```

The AI suggests the following analyses:

`r response`

## Implementing the Suggestions

```{r}
# Create a visualization based on AI suggestion
ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "MPG vs Weight by Cylinder Count",
       x = "Weight (1000 lbs)",
       y = "Miles per Gallon",
       color = "Cylinders") +
  theme_minimal()
```
````

---

## Other R Packages for AI Integration

Beyond ellmer and chatlas, several other R packages provide AI capabilities:

### tidyllm

[tidyllm](https://edubruell.github.io/tidyllm/){target=_blank} - Tidy interface for LLMs with piped workflows:

```r
# install.packages("tidyllm")
library(tidyllm)

llm_message("Explain linear regression") |>
  openai_chat(model = "gpt-4o-mini") |>
  get_reply()
```

### gptstudio

[gptstudio](https://michelnivard.github.io/gptstudio/){target=_blank} - RStudio addins for AI assistance:

```r
# install.packages("gptstudio")
library(gptstudio)

# Provides RStudio addins for:
# - Code explanation
# - Documentation writing
# - Code commenting
# - Spelling/grammar checking
```

### chattr

[chattr](https://mlverse.github.io/chattr/){target=_blank} - Chat interface in RStudio:

```r
# install.packages("chattr")
library(chattr)

# Opens an interactive chat pane in RStudio
chattr_app()
```

### ollamar

[ollamar](https://hauselin.github.io/ollama-r/){target=_blank} - Direct Ollama API access:

```r
# install.packages("ollamar")
library(ollamar)

# Low-level Ollama API access
list_models()
generate("llama3.2", "Hello!")
```

---

## Troubleshooting

??? failure "API Key Not Found"

    **Symptoms:** Error messages like "API key not set" or "authentication failed"

    **Solutions:**

    1. Verify the key is set correctly:
       ```r
       # R
       Sys.getenv("OPENAI_API_KEY")
       ```
       ```python
       # Python
       import os
       print(os.getenv("OPENAI_API_KEY"))
       ```

    2. Check `.Renviron` has no spaces around `=`

    3. Restart R/RStudio after editing `.Renviron`

    4. Ensure the key is valid at the provider's console

??? failure "Ollama Connection Refused"

    **Symptoms:** "Connection refused" or "Could not connect to Ollama"

    **Solutions:**

    1. Verify Ollama is running:
       ```bash
       curl http://localhost:11434/api/tags
       ```

    2. Start Ollama if needed:
       ```bash
       ollama serve
       ```

    3. Check if using the correct base_url:
       ```r
       chat <- chat_ollama(model = "llama3.2",
                          base_url = "http://localhost:11434")
       ```

??? failure "Model Not Found"

    **Symptoms:** "Model not found" errors

    **Solutions:**

    1. For Ollama, download the model first:
       ```bash
       ollama pull llama3.2
       ```

    2. List available models:
       ```r
       # ellmer
       models_ollama()
       ```

    3. Check exact model name spelling

??? failure "Out of Memory"

    **Symptoms:** R/Python crashes or "out of memory" errors

    **Solutions:**

    1. Use a smaller model:
       ```r
       chat <- chat_ollama(model = "llama3.2:1b")  # 1B instead of 3B
       ```

    2. Reduce context window:
       ```r
       chat <- chat_ollama(model = "llama3.2",
                          params = params(num_ctx = 2048))
       ```

    3. Close other applications to free memory

---

## Further Resources

**Posit Resources:**

- [Posit Website](https://posit.co/){target=_blank}
- [Positron Downloads](https://positron.posit.co/){target=_blank}
- [RStudio Downloads](https://posit.co/download/rstudio-desktop/){target=_blank}

**Package Documentation:**

- [ellmer Documentation](https://ellmer.tidyverse.org/){target=_blank}
- [chatlas Documentation](https://posit-dev.github.io/chatlas/){target=_blank}

**Related Workshop Materials:**

- [Ollama](ollama.md) - Running local LLMs
- [Hugging Face](huggingface.md) - Model hub and downloads
- [Jupyter AI](jupyter.md) - AI in Jupyter notebooks
- [RAG](rag.md) - Retrieval-augmented generation
- [Vibe Coding](vibe.md) - AI-assisted coding IDEs

**Community:**

- [Posit Community Forums](https://forum.posit.co/){target=_blank}
- [RStudio GitHub](https://github.com/rstudio){target=_blank}
- [Positron GitHub](https://github.com/posit-dev/positron){target=_blank}

---

!!! tip "Getting Started Recommendation"
    If you're new to using LLMs with R or Python:

    1. **Install Positron** for the best integrated experience
    2. **Start with Ollama** to avoid API costs while learning
    3. **Install ellmer (R) or chatlas (Python)** depending on your language
    4. **Download a small model:** `ollama pull llama3.2:3b`
    5. **Try the basic examples** in this guide
    6. **Graduate to cloud APIs** (OpenAI, Anthropic) when you need more capability

    For sensitive research data, Ollama provides complete privacy since all processing happens locally on your machine.
