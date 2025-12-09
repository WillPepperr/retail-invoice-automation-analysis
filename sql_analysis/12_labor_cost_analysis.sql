-- Finds the labor cost of the time taken checking in invoices
-- Assumes 20$/h fixed rate and 5 minutes of overhead and entering invoice photocopy

SELECT
    transaction_id,
    vendor_name,
    ROUND((DATEDIFF('second', invoice_initiated_ts, invoice_finished_ts) / 60), 2) 
        AS invoice_minutes,
    ROUND(((DATEDIFF('second', invoice_initiated_ts, invoice_finished_ts) + 300) / 3600) * 20, 2)
        AS labor_cost
FROM vendor_invoices_last_year
LIMIT 100
