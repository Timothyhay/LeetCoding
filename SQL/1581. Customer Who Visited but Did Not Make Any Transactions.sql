-- LEFT JOIN
SELECT v.customer_id, COUNT(*) count_no_trans
FROM Visits v LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id
-- To get the final output, we want to COUNT the number of such visits associated with each customer_id,
-- and have the aggregated value grouped at the customer_id level.