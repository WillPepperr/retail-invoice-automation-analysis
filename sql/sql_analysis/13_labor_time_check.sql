-- Checks for invalid check-in times, under one minute, and over 10 minutes

WITH cte AS 
(
SELECT
    transaction_id,
    vendor_name,
    ROUND((DATEDIFF('second', invoice_initiated_ts, invoice_finished_ts) / 60), 2) 
        AS invoice_minutes
FROM vendor_invoices_last_year
)

SELECT 
    'Less than 1 minute' AS bucket,
    COUNT(transaction_id) AS count 
FROM cte 
WHERE 
    invoice_minutes < 1

UNION ALL

SELECT 
    'More Than 10 minutes' AS bucket,
    COUNT(transaction_id) AS count 
FROM cte 
WHERE 
    invoice_minutes > 10.0

/*
	0 results from this query, infering timestamps were maintained accurately
Run date: 12/01/25

*/
