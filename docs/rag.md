# Retrieval Augmented Generation (RAG)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

One of the more recent applications of GPTs is the use of vector databases with specific documentation text or imagery. 

Retrieval Augmented Generation (RAG) can be used to search through large corpuses of text, or specific texts for data mining and research applications.

Real world examples of Agentic AI include self-driving vehicles, warehouse robots, and high frequency trading bots. 

## How it works

RAG databases allow you to host your own private data

Open Source projects like [Weaviate](https://weaviate.io/developers/weaviate) or [Pinecone](https://docs.pinecone.io/guides/get-started/overview) allow you to self-host private data.

Table: Popular RAG database software:



### Embeddings

Text passages (or other data, like images) are transformed into numerical representations known as “embeddings.” These embeddings capture semantic meaning, so similar concepts end up being close together in vector space.

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


### Vector Database

A vector database stores embeddings efficiently, often using specialized data structures to handle large-scale, high-dimensional searches.

[OpenAI Platform](https://platform.openai.com/docs/overview) allows you to upload your own data to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores) and [file search](https://platform.openai.com/docs/assistants/tools/file-search) in custom assistants

### 

## Google NotebookLM

[Google NotebookLM](https://notebooklm.google/){target=_blank} is a notebook style GPT designed to help you better understand and work with your own data and information. NotebookLM can summarize documents, answer questions, brainstorm ideas, all based on your uploaded files or shared Google Drive.

**Use NotebookLM for:**

  * **Knowledge Synthesis:**  Quickly grasp the core concepts of dense documents.
  * **Information Extraction:**  Find specific details and answers within your notes.
  * **Creative Exploration:**  Generate new ideas and connections from your sources.

**1. General Productivity:**

  * **Meeting Preparation:** Upload meeting agendas, pre-reads, and background documents. NotebookLM can summarize key discussion points, identify action items, and prepare you for productive meetings.
  * **Document Management:**  Process lengthy reports, articles, or legal documents efficiently. Get instant summaries, extract key arguments, and quickly locate specific information without tedious reading.
  * **Content Creation:**  Use NotebookLM to analyze research materials, synthesize information from multiple sources, and brainstorm outlines for articles, presentations, or reports.
  * **Personal Knowledge Base:**  Upload notes, articles, and documents on topics you're learning about.  NotebookLM can help you connect ideas, identify knowledge gaps, and deepen your understanding over time.

**2. Teaching in Classrooms:**

  * **Curriculum Planning:**  Upload syllabi, learning objectives, and resource materials. NotebookLM can help teachers identify key themes, suggest connections between topics, and generate lesson plan ideas.
  * **Assessment Design:**  Analyze past exams, rubrics, and student work samples. NotebookLM can help teachers identify areas for improvement in assessment design and generate new question types.
  * **Providing Personalized Feedback:**  Teachers can upload student essays or assignments and use NotebookLM to identify common areas of strength and weakness, enabling more targeted and efficient feedback.
  * **Creating Learning Resources:**  Quickly generate summaries of complex texts, create quizzes based on uploaded materials, and develop study guides for students.

**3. Learning in Classrooms:**

  * **Understanding Complex Materials:**  Students can upload lecture notes, textbook chapters, or research articles. NotebookLM can help them summarize key concepts, identify areas of confusion, and formulate questions for clarification.
  * **Active Reading and Note-Taking:**  Engage more deeply with reading materials by using NotebookLM to ask questions, extract key arguments, and make connections between different sources.
  * **Research and Project Work:**  Students can upload research papers, articles, and data sets. NotebookLM can assist in literature reviews, data analysis, and brainstorming project ideas.
  * **Collaborative Learning:**  Students can share notebooks and work together to analyze materials, synthesize information, and prepare for group projects or discussions.

**4. Research:**

  * **Literature Reviews:**  Upload research papers, articles, and conference proceedings. NotebookLM can quickly identify key themes, summarize findings, and highlight gaps in the existing literature, significantly speeding up the literature review process.
  * **Data Analysis:**  Analyze qualitative data like interview transcripts or open-ended survey responses by identifying patterns, themes, and key quotes.
  * **Hypothesis Generation:**  Explore connections between different research sources and brainstorm new research questions or hypotheses based on synthesized knowledge.
  * **Grant Proposal Writing:**  Organize background research, synthesize relevant literature, and identify key arguments to strengthen grant proposals.
  * **Staying Up-to-Date:** Researchers can continuously upload new publications in their field and use NotebookLM to stay informed about the latest advancements and emerging trends.
