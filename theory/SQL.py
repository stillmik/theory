"""
Q:: NoSQL
A:: NoSQL trades structure for scalability + flexibility.
    
    - Redis(unreal speed), MongoDB (unstructured), Cassandra(r\w)
    - No joins
    - memory lowers, speep goes up


Q:: Horizontal scaling
A:: more machines, not more memory


Q:: JOIN types
A:: - INNER JOIN returns only the rows that have matching values in both tables. If there is no match, 
        the row is not included in the result.
    - The LEFT JOIN returns all rows from the left table (the first table), and the matched rows from 
        the right table (the second table)
    - The RIGHT JOIN is the opposite of a LEFT JOIN. It returns all rows from the right table, 
        and the matched rows from the left table.
    -  The FULL JOIN returns all rows from both tables. If there is a match between the columns being joined, 
        it will combine the matching rows. 
    - A SELF JOIN (pseudo join) is a join where a table is joined with itself. This is useful when you need to 
        compare rows within the same table (e.g., finding employees who are managers of other employees).

        
Q:: table_1 has 2 entries, table_3 has 3. Min / max number of entries if we perform LEFT/RIGHT/INNER JOIN.
    In general what's the maximul amount of entries we're able to obtain?
A:: INNER JOIN: min - 0 (if no rows match), max - 2
    LEFT JOIN: min - 2, max - 6 (if every row in table_1 matches with every row in table_3).
    RIGHT JOIN: min - 3, max - 6 (if every row in table_1 matches with every row in table_3).


Q:: WHERE vs HAVING
A:: 1) Filters rows before any aggregation happens.
    2) Filters grouped data after aggregation happens.

    
Q:: LIKE
A:: LIKE is used for simple pattern matching in WHERE clauses
    - '%' Matches any number of characters
    - '_' Matches exactly one character
    ---------------------------------------------------------
    SELECT * FROM users WHERE name LIKE 'A%';
    🔹 Matches: Alice, Andrew, Ava
    🔹 Doesn't match: Ben, Charlie
    SELECT * FROM users WHERE name LIKE 'J____';
    🔹 Matches: James, Jacob, Jonah
    🔹 Doesn't match: John, Jennifer


_ Q:: PIVOT
A:: PIVOT in SQL - Transform Rows into Columns 🚀
    Imagine you have a sales table like this:
    Year	Product	Sales
    2023	Apples	100
    2023	Bananas	200
    2024	Apples	150
    2024	Bananas	250
    ------------------------------------------------
    But you want each product as a column, like this:
    Year	Apples	Bananas
    2023	100	    200
    2024	150	    250
    That's where PIVOT comes in! 🔥
    PostgreSQL doesn't have a built-in PIVOT function like SQL Server, 
    but you can achieve the same effect using FILTER with SUM:
    SELECT 
        year,
        SUM(CASE WHEN product = 'Apples' THEN sales ELSE 0 END) AS apples,
        SUM(CASE WHEN product = 'Bananas' THEN sales ELSE 0 END) AS bananas
    FROM sales
    GROUP BY year
    ORDER BY year;

 
Q:: EXPLAIN / EXPLAIN ANALYZE
A:: 1) Shows the query execution plan without actually running the query.
        EXPLAIN SELECT * FROM purchases WHERE client_id = 123;
        - Does it execute the query? ❌ No.
    2) What it does: Runs the query and shows the actual execution plan with real execution times.
        EXPLAIN ANALYZE SELECT * FROM purchases WHERE client_id = 123;
        - Does it execute the query? ✅ Yes.


Q:: DELETE vs TRUNCATE
A:: 1) DELETE
        - Removes rows from a table one by one and logs each row's deletion in the transaction log. 
            This operation can be slow if you're deleting many rows.
        - You can roll back the deletion if you use a transaction.
        - If there are any triggers defined for DELETE (e.g., AFTER DELETE), they will be fired.
        - Slower, especially for large tables because it deletes rows individually and logs each action.
    2) TRUNCATE
        - Removes all rows from the table instantly, bypassing row-by-row deletion. 
            It's more like a "bulk wipe" that deallocates the data pages.
        - It is not fully rollback-able
        - Does not activate any triggers.
        - Much faster than DELETE because it doesn't log individual row deletions.

        
Q:: CTE in SQL
A:: A CTE (Common Table Expression) is a temporary result set that you can reference within a SQL query.
    WITH cte_name AS (
        SELECT column1, column2 FROM table WHERE condition
    )
    SELECT * FROM cte_name;
    - cte_name is the temporary name for the result set.
    - The CTE is only available for the query that follows it.
    - It improves readability and avoids subquery nesting.


Q:: SQL vs noSQL
A:: 1) 💥 Need structured data & strong consistency? → Go SQL!
        - Stores data in tables, Follows a fixed schema
        - Uses Structured Query Language (SQL) 💡 
        - SQL → Vertically Scalable 📈. Not great for massive distributed systems.
        - ✔️ Financial & Banking Systems 🏦
    ------------------------------------------------------------------------------
    2) 💥 Need flexibility, speed & scalability? → Go NoSQL!
        - Stores data in key-value pairs, documents, graphs. Schema is dynamic
        - Uses different query languages (varies by type) 🌀
            (db.users.find({ "age": { "$gt": 18 } }))
        - Handles more load by adding more servers (horizontal).
        - ✔️ Real-time Big Data apps (Social Media, IoT) 📡
        

Q:: aggregation(SQL)
A:: - Aggregation functions in SQL are used to perform calculations on multiple rows of a table's column 
        to return a single value. These are often used with GROUP BY to group rows based on one 
        or more columns.
    - SELECT COUNT(*) FROM employees;
"""