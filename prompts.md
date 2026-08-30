# Prompt Engineering

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

![banner](assets/dailyprod-banner.png){width=1000}

## Introduction to Prompt Engineering

**Prompt Engineering** is a technique of crafting effective instructions using AI large language models. With modern AI-powered tools like Claude Desktop, ChatGPT, Gemini, and NotebookLM offering capabilities to upload documents, search the web, and process multiple file types, mastering prompt engineering has become essential for productive AI interactions.

!!! info "What You'll Learn"
    - **Fundamentals**: How AI models process and respond to prompts
    - **Modern Features**: Leveraging document uploads, web search, and multi-modal inputs
    - **Best Practices**: Structured approaches to writing effective prompts
    - **Advanced Techniques**: Context management, chaining, and custom instructions

## Understanding Modern AI Capabilities

### Core Features of Today's AI Tools

Modern AI assistants have evolved beyond simple text chat:

| Feature | :simple-claude: Claude | :fontawesome-brands-openai: ChatGPT | :simple-googlegemini: Gemini | NotebookLM | :material-microsoft: CoPilot |
|---------|--------|---------|--------|------------|---------|
| **Document Upload** | PDFs, text, code | PDFs, images, data | PDFs, images, GDrive | PDFs, Google Docs | PDFs, OneDrive |
| **Web Search** | Via MCP | Yes | Yes | Yes | Yes |
| **Context Window (tokens)** | 200K | 128K| 2M | Document-based | 128K |
| **File Analysis** | Yes | Yes | Yes | Deep analysis | Yes |
| **Code Execution** | Yes (MCP) | Yes | Yes | No | Yes |

### How AI Models Process Your Input

!!! info "The Processing Pipeline"
    1. **Tokenization**: Your prompt is broken into smaller units (tokens)
    2. **Context Assembly**: Uploaded documents and conversation history are included
    3. **Attention Mechanism**: The model identifies relevant information
    4. **Generation**: Response is produced token by token
    5. **Formatting**: Output is structured according to your specifications

## Getting Started: Basic Prompt Structure

### The Foundation: Clear Instructions

Start with simple, direct prompts before advancing to complex techniques:

```markdown
# Basic Prompt
"Summarize this research paper in 3 bullet points"
```

```markdown
# Better Prompt
"As a research scientist, summarize the key findings from this paper 
in 3 bullet points, focusing on methodology and results"
```

```markdown
# Best Prompt
"You are a research scientist reviewing papers for a journal. 
Summarize the attached PDF in 3 bullet points that cover:
1. Research question and hypothesis
2. Methodology and sample size
3. Key findings and limitations
Format as a bullet list with sub-points for clarity."
```

### Working with Documents

Modern AI tools excel at document analysis. Here's how to maximize their potential:

!!! success "Document Upload Best Practices"
    - **Specify the document**: "In the attached PDF..." or "Based on the uploaded spreadsheet..."
    - **Direct attention**: "Focus on Section 3.2 of the document"
    - **Request specific outputs**: "Create a table comparing the methods described in chapters 2 and 5"
    - **Combine multiple sources**: "Compare the findings in these three papers"

#### Example: Multi-Document Analysis

```markdown
I've uploaded three research papers on climate change. Please:

1. Create a comparison table with columns for:
   - Paper title and authors
   - Methodology
   - Key findings
   - Limitations

2. Identify common themes across all papers

3. Highlight any contradictory findings

Format the response with clear headers and use markdown tables.
```

## The CRAFT Framework

For consistent, high-quality results, use the [CRAFT framework](https://www.geeky-gadgets.com/craft-prompt-framework/){target=_blank}:

### **Context**

Provide background information and set the scene

### **Role**
Define who the AI should act as

### **Action**
Specify exactly what you want done

### **Format**
Describe how the output should be structured

### **Tone**
Indicate the style and voice to use

#### CRAFT Example

```markdown
Context: I'm preparing a grant proposal for NSF funding on AI in education

Role: Act as an experienced grant writer and education researcher

Action: Review my draft introduction and suggest improvements

Format: Provide feedback as tracked changes with explanations

Tone: Professional, constructive, and encouraging
```

## Advanced Techniques

### 1. Custom Instructions and System Prompts

Modern AI platforms allow you to set persistent instructions:

!!! example "'Custom Instructions' or 'System Instructions'"

    Platforms like Gemini and Claude allow you to add "Custom Instructions" or "System Instructions" as prior prompts, which act as a global rule to subsequent prompt chaining.

    For example:

    ```markdown
    # Project Context
    I'm a data scientist working on machine learning projects.
    Always provide Python code examples using scikit-learn and pandas.
    Include docstrings and type hints in all code.
    
    # Response Preferences
    - Be concise but thorough
    - Explain complex concepts with analogies
    - Always cite sources when making factual claims
    ```

### 2. Leveraging Web Search

Most featured GPTs now feature a web browse or search engine capability.

Enabling search allows the GPT to use document retrieval on websites and PDFs when reasoning out its response.

```markdown
Search for the latest research on the public health benefits of vaccination published in 2024. 

Focus on:
- Papers from top conferences (AHA, ASPPH, NRHA, ICFMDP)
- mRNA
- Bird Flu and COVID

Summarize the top 5 papers with links to the originals.

```

### 3. Multi-Modal Prompting

Combine different input types for richer interactions:

```markdown
I've uploaded:
1. A screenshot of my dashboard
2. The underlying data in CSV format
3. Our brand guidelines PDF

Create a redesigned dashboard that:
- Improves data visualization based on best practices
- Adheres to our brand colors and fonts
- Highlights the KPIs mentioned in the data dictionary
```

### 4. Prompt Chaining

Build complex outputs through sequential prompts:

!!! tip "Effective Chaining Strategy"
    1. **Start broad**: "Outline a research paper on sustainable AI"
    2. **Zoom in**: "Expand section 3 on energy-efficient training methods"
    3. **Refine**: "Add citations and make the tone more academic"
    4. **Polish**: "Format according to IEEE standards"

### 5. Using Examples (Few-Shot Learning)

Provide examples to guide the AI's output:

```markdown
I need to classify customer feedback. Here are examples:

"The product arrived damaged" → Category: Shipping Issue
"Can't log into my account" → Category: Technical Support
"Love the new features!" → Category: Positive Feedback

Now classify these:
1. "The app keeps crashing on startup"
2. "Best purchase I've made this year"
3. "Package was left in the rain"
```

## Practical Applications

### Research and Analysis

```markdown
Analyze the attached dataset (CSV) and:
1. Identify statistical patterns and outliers
2. Create visualizations for the top 3 insights
3. Write a methods section describing the analysis
4. Suggest additional analyses based on the data

Use pandas profiling techniques and create matplotlib visualizations.
Include code that I can run locally.
```

### Writing and Editing

```markdown
I've uploaded my draft manuscript. Please:

1. Check for consistency in terminology throughout
2. Ensure all figures are referenced in the text
3. Verify the citation format matches APA 7th edition
4. Highlight any unclear passages
5. Suggest improvements for flow between sections

Provide a tracked-changes version and a summary of major edits.
```

### Code Development

```markdown
Based on the uploaded requirements document:

1. Create a Python class structure for the described system
2. Include comprehensive docstrings and type hints
3. Add unit tests for each method
4. Create a README with installation and usage instructions
5. Follow PEP 8 style guidelines

Use modern Python features (3.10+) and include error handling.
```

## Common Pitfalls and Solutions

### Pitfall 1: Vague Instructions

❌ **Poor**: "Make this better"

✅ **Better**: "Improve this abstract by making it more concise (under 250 words), adding keywords, and ensuring it follows the journal's structure: background, methods, results, conclusions"

### Pitfall 2: Information Overload

❌ **Poor**: Uploading 50 documents without guidance

✅ **Better**: "Focus on documents 1-3 which contain the methodology. Ignore the appendices."

### Pitfall 3: Assuming Knowledge

❌ **Poor**: "Fix the usual issues"

✅ **Better**: "Check for: passive voice, sentences over 25 words, undefined acronyms, and missing Oxford commas"

### Pitfall 4: No Output Format

❌ **Poor**: "Summarize this"

✅ **Better**: "Create an executive summary with: 
- 3-sentence overview
- 5 key points as bullets
- 1 paragraph on implications
- Formatted with markdown headers"

## Quick Reference Card

!!! success "Prompt Engineering Checklist"
    - [ ] **Clear objective**: What do you want to achieve?
    - [ ] **Context provided**: Background information included?
    - [ ] **Role defined**: Who should the AI act as?
    - [ ] **Specific action**: Exact task described?
    - [ ] **Output format**: Structure specified?
    - [ ] **Examples given**: For complex tasks?
    - [ ] **Constraints noted**: Length, style, or content limits?
    - [ ] **Documents referenced**: If using uploads?
    - [ ] **Follow-up planned**: For iterative improvement?

## Assessment Questions

??? question "How do modern AI tools handle uploaded documents?"
    
    !!! success "Answer"

        Modern AI tools process uploaded documents by:

        - Converting them to text (OCR for images/PDFs)

        - Adding them to the context window

        - Allowing specific references ("In section 2.3...")

        - Enabling cross-document analysis
        
        - Maintaining document structure awareness

??? question "What's the most important element of an effective prompt?"
    
    !!! success "Answer"


        **Clarity of instruction** is paramount. The AI needs to understand:

        - What you want done (action)

        - How you want it done (format)

        - Why you want it done (context)
        
        Without clear instructions, even the most advanced AI will produce suboptimal results.

??? question "How can you ensure consistent outputs across multiple sessions?"
    
    !!! success "Answer"

        1. **Use custom instructions** (ChatGPT, Claude) or system prompts

        2. **Create templates** for common tasks

        3. **Save successful prompts** for reuse

        4. **Use platform features** like GPTs or Projects

        5. **Include examples** in your prompts

        6. **Specify exact formats** with templates

??? question "True or False: Longer prompts always produce better results"
    
    !!! failure "False"
        Prompt quality matters more than length. A well-structured, concise prompt often outperforms a lengthy, unfocused one. However, providing sufficient context and clear instructions is important. Aim for:

        - **Completeness** over brevity

        - **Clarity** over complexity

        - **Structure** over stream-of-consciousness

## Further Resources

- [:simple-claude: Anthropic's Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering){target=_blank}

- [:fontawesome-brands-openai: OpenAI's Best Practices](https://platform.openai.com/docs/guides/prompt-engineering){target=_blank}

- [:simple-googlegemini: Google's Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies){target=_blank}

- [:simple-github: Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts){target=_blank}

- [Learn Prompting Online Courses](https://learnprompting.org/){target=_blank}