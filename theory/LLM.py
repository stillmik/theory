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

"""


