SELECT
    COUNT(*)                                AS invoice_count,
    COUNT(DISTINCT transaction_id)          AS unique_transactions,
    MIN(DATE)                               AS min_date,
    MAX(DATE)                               AS max_date,
    COUNT(DISTINCT STORE_ID)                AS store_count,
    COUNT(DISTINCT STATE)                   AS state_count, 
    COUNT(DISTINCT VENDOR_ID)               AS vendor_count,
    COUNT(DISTINCT VENDOR_CATEGORY)         AS vendor_category_count,
    COUNT(DISTINCT REGION)                  AS region_count
FROM VENDOR_INVOICES
;




/*
Run date: 2025-12-15


INVOICE_COUNT	UNIQUE_TRANSACTIONS		MIN_DATE	MAX_DATE	STORE_COUNT	STATE_COUNT	VENDOR_COUNT	VENDOR_CATEGORY_COUNT	REGION_COUNT
4146565			4146565					2024-01-01	2025-09-30	290			38			12				7						4
*/
