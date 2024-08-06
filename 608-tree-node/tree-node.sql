# Use case when

SELECT id, (
    CASE
        WHEN p_id IS null THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT null) THEN 'Leaf'
        ELSE 'Inner'
    END
) as 'type'
FROM Tree