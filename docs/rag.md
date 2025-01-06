# Retrieval Augmented Generation (RAG)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

One of the more recent applications of GPTs is the use of vector databases with specific documentation text or imagery. 

Retrieval Augmented Generation (RAG) can be used to search through large corpuses of text, or specific texts for data mining and research applications.

Real world examples of Agentic AI include self-driving vehicles, warehouse robots, and high frequency trading bots. 

## How it works

RAG databases allow you to host your own private data

Open Source projects like [Weaviate](https://weaviate.io/developers/weaviate) or [Pinecone](https://docs.pinecone.io/guides/get-started/overview) allow you to self-host private data.

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

## NotebookLM

