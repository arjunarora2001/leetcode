# Only need to print out the last name
# Select the top value
/*
Create a subquery to sort Queue by turns
Find the cumulative weights
Don't select any turn that exceeds the cumulative weight
Sort overall results in descending order of turn and return top result
*/


SELECT q1.person_name
FROM Queue q1, Queue q2
WHERE q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY q1.turn DESC
LIMIT 1