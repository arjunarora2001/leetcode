# Write your MySQL query statement below
# There should not be a vertex that is greater than the sum of the other two vertices
# Find all results where one vertex > other vertex + other vertex

SELECT *,
(CASE
    WHEN (ABS(x) >= ABS(y) + ABS(z)) THEN "No"
    WHEN (ABS(y) >= ABS(x) + ABS(z)) THEN "No"
    WHEN (ABS(z) >= ABS(x) + ABS(y)) THEN "No"
    ELSE "Yes"
END) AS triangle
FROM Triangle