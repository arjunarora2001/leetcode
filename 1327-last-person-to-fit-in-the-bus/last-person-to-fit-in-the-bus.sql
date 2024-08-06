# Only need to print out the last name
# Select the top value
/*
Create a subquery to sort Queue by turns
Find the cumulative weights
Don't select any turn that exceeds the cumulative weight
Sort overall results in descending order of turn and return top result
*/

SELECT person_name
FROM (
    SELECT person_name, (SUM(weight) OVER (ORDER BY turn)) AS total_weight
    FROM Queue) AS cumulative_table
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1