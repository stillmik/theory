"""

Q:: Crawl4AI
A:: Crawl4AI creates smart markdown attached to original contents of HTML.
    - very efficient
    - concise informative markdown
    - removes HTML, ads, 
    - BM25 to remain what we care about
    - allows on parallel execution


Q:: how to crawl entire website
A:: /sitemap.xml


Q:: typical RAG with Internet Crawling
A:: Encoding::
        1) get URLs from sitemap
        2) for each URL get markdown
        3) for each makrdown chunk it
            3.1) for each chunk make short description (summary) or other metadata.
        4) for each chunk embed it
        5) for eachchunk insert it into database with metainfo (example: Supabase)
    Retrieval::
        1) Encode users question with openAI embeddings
        2) Retrieve from DB relevant info (exp: 5 chunks filtered out by pydantic_doc) (tool)
        3) Retrieveinfo from website using atached links.


Q:: Ways to enhance RAG performance
A:: 1) Query over condensed summaries. Each summary has an extension, link to broader explanation.
        NN can refer to this links to get more comprehensive responce.
    2) Folder approach
    

Q:: hallucinations
A:: answers which seem being real, confident, but actually completely made up. 
    Like asking about a book which was never read but LLM gives confident AF unreal
    answer on it.


Q:: chain of thought vs ___
A:: - ___ = single completion


Q:: Indexes in Pinecone
A:: | Concept   | SQL DB | Pinecone          |
    | --------- | ------ | ----------------- |
    | Container | Table  | Index             |
    | Row       | Record | Vector            |
    | Column    | Field  | Metadata          |
    | Query     | SQL    | Similarity search |


Q:: Reranking
A:: We retrieve most relevant chunks, and a top of them rerank them with reranker model
    1) Cross encoder (BERT-based) 
        - Takes both query and candidate as input
        - Outputs a relevance score (class token) for pair
        - Attention mechanism allows it to consider interactions between query and candidate
    2) Late interaction (Siamese)
        - take query and candidate, break them down into tokens
        - each Q token is compared to each C token
        - max() + avg() to get relevance score
        - the highest similarity is used as relevance score


Q:: Knowledge Graphs
A:: - Introduces a graph structure to represent relationships between entities.
        By introducing a graph structure, we can capture complex relationships and dependencies 
        between entities.
    - Main entities: Entities (nodes), Relationships (connections), Communities (clusters of nodes).
    - Flow:
        1) Load text and split into chunks
        2) Extract entities (name, mb type, description), relationships (source, target, description) using LLMs.
        3) Community detection (clustering related entities together)
        4) create embeddings of nodes and store them in 


Q:: Knowledge Graphs search types
A:: 1) Local search: use cos similarity to detect relevant nodes, then identify relarionships and related nodes.
    2) Global search: use cos similarity to detect relevant communities based on community reports embeddings.
        Then goes reranking + map reduce.
    3) Drift search: uses both of them. From initial query, we generate follow-up questions to explore related topics.


Q:: Advanced chunking techniques
A:: 1) Letter chunking -> Token chunking
    2) Recursive chunking:
        - Looking for natural text splitters to split the text in best possible way.
        1) Split text into chunks based on \n\n. 
        2) If chunk is too big, split it by \n.
        3) If chunk is still too big, split it by '!''?''.'
        4) If chunk is still too big, split it by ','
        5) etc.
    3) Cluster semantic chunks (MVP):
        - Split text into small chunks (50 tokens)
        - Embed them and build confusion matrix (cos similarity between chunks)
        - Group most similar chunks together to create bigger chunks with more semantic meaning.
        - This way we can find natural breakpoints
    4) LLM chunking (MVP):
        - Give text to LLM and ask it to split it into chunks.


Q:: Recursive LLM
A:: 
