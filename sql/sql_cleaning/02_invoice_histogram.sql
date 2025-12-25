SELECT
	COUNT(transaction_id) AS transaction_count,
	YEAR(date) AS year, 
	MONTH(date) AS month
FROM VENDOR_INVOICES
GROUP BY YEAR, MONTH 
ORDER BY YEAR, MONTH
