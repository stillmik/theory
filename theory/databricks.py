"""
Q:: Layers of data
A:: 
    🧠 Landing - This is where data first lands. Data is ingested as-is.
    
    🥉 Bronze Layer - This is where data lands in not clean non-processed format, 
        but prepard for working with it. Data is ingested as-is. No filtering, no cleaning 😭
    Can include:
    - missing values
    - duplicates
    - weird formats
    - broken records
    💡 Purpose: Preserve original data (super important for debugging or reprocessing)
    
    🥈 Silver Layer (Cleaned + structured)
    How data looks like:
        - Data is cleaned and validated
        - Duplicates removed
        - Formats standardized (dates, numbers, etc.)
        - Basic joins happen here
    💡 Purpose: Make data usable and consistent.

    🥇 Gold Layer (Business-ready, polished)
    How data looks like:
        - Data is aggregated and shaped for use
        - Designed for:
            - dashboards
            - analytics
            - ML features
    💡 Purpose: Answer real questions without extra work



Q:: 🌊 What is an ETL pipeline?
A:: ETL = Extract → Transform → Load
    It's just a process that moves data from one place to another... but makes it actually usable on the way.

cars stream data into kinesis data stream, which is the landing zone.
"""