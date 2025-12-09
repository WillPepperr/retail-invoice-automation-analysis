SELECT
    COUNT(*)                                AS invoice_count,
    MIN(DATE)                               AS min_date,
    MAX(DATE)                               AS max_date,
    COUNT(DISTINCT STORE_ID)                AS store_count,
    COUNT(DISTINCT VENDOR_ID)               AS vendor_count,
    COUNT(DISTINCT VENDOR_CATEGORY)         AS vendor_category_count,
    COUNT(DISTINCT REGION)                  AS region_count
FROM NATIONAL_VENDOR_INVOICES_LAST_YEAR;



/*
Run date: 2025-12-01
*/
