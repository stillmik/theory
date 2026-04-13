"""
Q:: Index in vector databases
A:: - In vector databases, an index is a data structure that allows for efficient searching 
        and retrieval of high-dimensional vectors.
    - It organizes the vectors in a way that enables fast similarity searches, using 
        approximate nearest neighbor search (ANN). Instead of iterating through all vectors, 
        the index allows you to quickly find the most similar.


Q:: ANN
A:: 1) select 2 random points
    2) build separate line for them
    3) do that N times till max_bucket_size <= K
    4) now you can build a tree to estimate to which bucket your new point belong to:
        at each step you just cal is a point above or below the line

        
Q:: ANN forest
A:: 1) build an ANN tree
    2) build a forest
    3) a point now belongs to intersection region of this trees 


   
"""