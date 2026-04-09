"""

Q:: project and files and upload
A:: - navigate to files
    - click create project
    - new -> upload files


Q:: first node in pipeline
A:: - batch pipeline/stream pipeline.  Streaming pipelines for low-latency (< minutes) \
        real-time data ingestion and immediate operational actions (e.g., alerts). 
        Choose Batch pipelines for high-volume, scheduled, or complex analytical processing 
        where speed is less critical than cost and consistency.
    - we click new pipeline and we click upload button and we can upload the data 
        and will appear a new node


Q:: node options
A:: - transform
    - split
    - join
    - union
    - LLM
    - new dataset


Q:: transformations
A:: - extract text from PDF
        - OCR
        - raw text
        - specify column name where we extract
    
    - explode array
    - break field into subfields
    - casting
    - concatenations
    - is null
    - concatenate
    - drop columns

    
Q:: Ontology
A:: - represents real world objects. Is getting created via Ontology manager.
    - new -> object type|link type
    - link is specified via: 2 uid + join table
"""