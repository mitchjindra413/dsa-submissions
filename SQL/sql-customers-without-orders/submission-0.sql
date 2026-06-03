-- Write your query below
SELECT customers.name
FROM customers
WHERE customers.id NOT IN (
    SELECT customer_id
    FROM orders
)