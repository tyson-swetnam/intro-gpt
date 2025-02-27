# Ollama

## Install Ollama

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Run Ollama

Pick a model:

[https://ollama.com/library](https://ollama.com/library){target=_blank}

The smallest distilled model:

```
ollama run deepseek-r1:1.5b
```

Let's use a bigger model, `DeepSeek-R1-Distill-Llama-8B` 

```
ollama run deepseek-r1:8b
```

## Talk to Ollama in the Terminal

Once the program starts running, you can access it from the terminal. 

## Talk to Ollama in a Jupyter Notebook

Open a Notebook using the Pytorch kernel

```
import ollama
```
