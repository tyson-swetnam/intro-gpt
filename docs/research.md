# Overview

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Introduction

GPTs excel at scientific research, but become specialized rapidly depending upon their application. GPTs and LLMs also fit as a cog within the larger AI ecosystem of natural language processing, and machine learning.

When deployed privately into secure data enclaves, GPTs can be used with sensitive and secure data (e.g., FERPA, HIPAA, or CUI) without the risk of data breaches or interception over internet traffic. 

| Generative AI | Predictive AI |
|---------------|---------------|
| Generative Adversarial Networks (GANs) | Linear Regression |
| Variational Autoencoders (VAEs) | Logistic Regression |
| Generative Pretrained Transformers (GPTs) | Decision Trees |
| Diffusion Models | Random Forest |
| Autoregressive Models | Support Vector Machines (SVMs) |

**Generative AI and Academic Research**

Generative AI has revolutionized academic research by enabling the creation of synthetic data, accelerating drug discovery, and aiding in the development of new materials. 

* **Synthetic Data Generation:** GANs can create realistic synthetic datasets, addressing privacy concerns and data scarcity.
* **Drug Discovery:** Generative models can design novel drug molecules with desired properties.
* **Material Science:** AI-powered generative design can optimize material properties for specific applications.

**Predictive AI and Climate Modeling**

Predictive AI plays a crucial role in climate modeling by analyzing historical data to forecast future climate patterns.

* **Climate Change Prediction:** Machine learning models can predict temperature changes, sea-level rise, and extreme weather events.
* **Climate Impact Assessment:** AI-powered tools can assess the impact of climate change on ecosystems and human societies.

**Predictive AI and Protein Folding**

Predictive AI has made significant strides in protein folding, a fundamental challenge in biology.

* **Protein Structure Prediction:** Deep learning models like AlphaFold can accurately predict protein structures from amino acid sequences.
* **Drug Design:** Understanding protein structures enables the design of targeted drugs.

**Generative AI and Language Models**

Generative AI, particularly GPTs, has significantly advanced Natural Language Processing (NLP). These models are trained on massive amounts of text data and can generate human-quality text, translate languages, write different kinds of creative content, and answer your questions in an informative way.

**Generative AI and Retrieval Augmented Generation**

Retrieval Augmented Generation (RAG) combines the strengths of generative AI and information retrieval. It allows models to access and incorporate relevant information from external sources, improving the quality and factual accuracy of generated text.

**Predictive AI and Machine Learning**

Predictive AI is a subset of machine learning that focuses on forecasting future trends and outcomes. It leverages statistical techniques and algorithms to analyze historical data and make predictions.

**Predictive AI and Transformers**

Transformers, a type of neural network architecture, have revolutionized predictive AI. They are particularly effective in tasks like time series forecasting, natural language processing, and computer vision.

**Predictive AI, Stable Diffusion, and Generative AI**

While Stable Diffusion is a powerful generative AI model, it is not directly related to predictive AI. Generative AI, on the other hand, can be used to generate synthetic data for training predictive models, enhancing their performance and robustness.

## Workshop Lessons

Specific to this workshop, we focus on code interpreters and code execution using GPTs, but we will also touch upon the creation and deployment of custom AI applications and how to use commercial and open source GPTs for each.

In a future workshop we will cover the deployment of secure private GPTs and LLMs in data enclaves 

!!! Question "Why use GPTs for research?"

    !!! Success "Advantages"

        * **Increased Efficiency and Productivity:** perhaps the most obvious and enticing reason for using GPTs is to automate tedious and repetitive tasks, creating more time for analyses and research.

        * **Accuracy & Objectivity:** GPTs analyze data without human bias. 

        * **Pattern Recogition:** GPTs may identify patterns and connections in data that a human cannot.

    !!! Failure "Disadvantages"

        * **Human Oversight:** GPTs should not be used to replace human expertise. Researchers must always evaluate and ensure GPT output are factual and align with published research artifacts.

        * **Bias:** GPTs can reduce human bias, but suffer from their own training biases.
        
        * **Potential Misuse:** GPTs can be used to fabricate scientific research papers or manipulate data, undermining the integrity of science.  

## Literature Review and Synthesis

GPTs are excellent summarization tools. When coupled with large corpuses of published research they can be invaluable for literature review and synthesis. 

[Perplexity.ai](https://perplexity.ai){target=_blank} has established itself as a popular GPT for search and summary of existing web-based material. 

[Google Deep Research](https://gemini.google.com/app) is positioning itself as a platform for in depth prompts on specific topics.

[Google NotebookLM](https://notebooklm.google) allows you to personalize your research by providing your own literature or knowledge (files, images, audio).

### Custom ChatGPTs for Literature Review

#### ScholarAI 

[ScholarAI](https://chatgpt.com/g/g-L2HknCZTC-scholar-ai) is the most highly starred :star: ai research assistant on custom GPTs on ChatGPT for research.

#### ScholarGPT

[ScholarGPT](https://chatgpt.com/g/g-kZ0eYXlJe-scholar-gpt){target=_blank} was one of the early custom GPTs created on ChatGPT and has many millions of resources embedded within it. 

#### Semantic Scholar

[Semantic Scholar](https://www.semanticscholar.org/) is a free, AI-powered research tool for scientific literature, based at Ai2.

### :hugging: HuggingFace 

HuggingFace is the dominant registry for AI models and model data. 

## Data Analysis


??? Abstract "Linux Guru"

    ChatGPT is trained on common data science languages, like Python, Julia, and R. Use ChatGPT to help develop basic code or to explain and debug code you're trying to write. 

    Using ChatGPT can be a time savings, reducing the time it takes to look for the answers yourself over conventional search.

    ```markdown
    I want you to act as a humble data scientist who works a lot with Python and scientific visualization

    Create a Python script which generates a visually pleasing and compelling heat map for a CSV dataset
    ```

    You can also use it to summarize code or to help explain its operation

    ```markdown
    I want you to act as a humble data scientist who works a lot with Linux 

    Explain to me what the following code does:

    $ find /home/www \( -type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i 's/subdomainA\.example\.com/subdomainB.example.com/g'
    ```

    Other valuable uses:
    
    * Change variable names and file names! When you have a large dataset with many files and folder names, you can ask ChatGPT to help design a schema for renaming your project's content

    * Regular Expressions, or `regex` is a bane of many programmers. ChatGPT can write, edit, and explain complex `regex`

    ```markdown
    I want you to act as a regex generator. Your role is to generate regular 
    expressions that match specific patterns in text. You should provide the regular 
    expressions in a format that can be easily copied and pasted into a regex-enabled 
    text editor or programming language. Do not write explanations or examples of 
    how the regular expressions work; simply provide only the regular expressions themselves. 

    remove any numbers from a string and replace them with a capital X
    

### Hypothesis generation


Examples of roles you might ask for are: a domain science expert, an IT or DevOps engineer, software programmer, journal editor, paper reviewer, mentor, teacher, or student. You can even instruct ChatGPT to respond as though it were a Linux [terminal](https://www.engraved.blog/building-a-virtual-machine-inside/){target=_blank}, a web browser, a search engine, or language interpreter.

??? Abstract "Data Scientist"

    Let's try an example prompt with role-playing to help write code in the R programming language.

    ```markdown
    I want you to act as a data scientist with complete knowledge of the R language, 
    the TidyVerse, and RStudio. 
    
    Write the code required to create a new R project environment,
    Download and load the Palmer Penguins dataset, and plot regressions of body mass, 
    bill length, and width for the species of Penguins in the dataset. 

    Your response output should be in R and RMarkDown format 
    with text and code delineated with ``` blocks.

    At the beginning of new file make sure to install any 
    RStudio system dependencies and R libraries that Palmer Penguins requires.
    ```

    Example can use `GPT o1` or `Gemini 2.0` 

??? Abstract "Talk to Dead Scientists"

    Try to ask a question with and without Internet access enabled:

    ```markdown
    I want you to respond as though you are the mathematician Benoit Mandelbrot

    Explain the relationship of lacunarity and fractal dimension for a self-affine series

    Show your results using mathematical equations in LaTeX or MathJax style format
    ```
    Again, there is no guarantee that the results ChatGPT provides are factual, but it does greatly improve the odds that they are relevant to the prompt. Most importantly, these extensions provide citations for their results, allowing you to research the results yourself. 

### Feedback


### Example 3: Programming help

Another impressive application of ChatGPT is in the field of programming. You can use it as a coding assistant, where it can help write code, debug issues, or explain complex code snippets. By asking it to convert your high-level descriptions into code, or to suggest improvements for existing code, you can significantly enhance your programming productivity.

#### Coding Assistant

Suppose you're working on a Python program to perform data analysis, but you're not sure how to write a function to calculate the median from a list of numbers. You might use ChatGPT like this:

??? example "Python median function"

    ```
    I'm trying to write a Python function that takes a list of numbers as an argument and returns the median. I'm not sure about the best way to implement this. Could you help me write the code?
    ```

ChatGPT could then provide you with a suitable Python function, demonstrating the logic to calculate the median from a list of numbers.

#### Debugging

Let's say you're having trouble with a piece of JavaScript code that's not behaving as expected. You could ask ChatGPT for help as follows:

!!! example "Debugging JavaScript"

    ```
    my JavaScript code to add event listeners to buttons isn't working as expected. Here's the code:
    ```
    ```javascript
    let buttons = document.querySelectorAll('.btn');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function() {
            console.log('Button ' + i + ' clicked');
        });
    }
    ```
    ```
    When I click a button, it always logs 'Button 5 clicked', no matter which button I click. What's going wrong, and how can I fix it?"
    ```

ChatGPT could then explain the issue (in this case, a common pitfall with JavaScript closures) and suggest a corrected version of your code.

!!! warning "Limitations"
    Remember, while ChatGPT is knowledgeable in many programming languages and concepts, it doesn't replace a full Integrated Development Environment (IDE) or debugger and should be used as a supplementary tool for coding assistance.

### Popular Uses of Prompt Engineering in Research (Data Science and Code Interpreters)

*   **Data Cleaning and Preprocessing:** Automate the process of cleaning and preparing data for analysis, including handling missing values, data normalization, and outlier detection.
*   **Code Generation:** Generate code snippets for specific data analysis tasks, such as statistical tests, data visualization, and machine learning model implementation.
*   **Algorithm Selection and Design:** Suggest appropriate algorithms or models based on the characteristics of the data and the research question.
*   **Automated Report Writing:** Generate summaries of data analysis results, including key findings, visualizations, and interpretations.
*   **Literature Review Assistance:** Quickly find and summarize relevant research papers, identify key concepts, and extract important information.
*   **Hypothesis Generation:** Explore potential research questions and hypotheses based on existing data and literature.
*   **Experimental Design:** Assist in designing experiments, including determining sample sizes, selecting appropriate variables, and suggesting control measures.


