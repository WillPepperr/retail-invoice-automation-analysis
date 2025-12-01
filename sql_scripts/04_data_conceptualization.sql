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
Data source: NATIONAL_VENDOR_INVOICES_2025, NATIONAL_VENDOR_INVOICES_2024 (via LAST_YEAR view)

ensures data values

 | Date      |
 |-----------|
 | 2024-10-01|
 | 2025-09-30|

Notes:
	- Created view combing table data between 2024 and 2025 filtering between fiscal Q2 2024 through Q1
	- Calculations needed: checkin_minutes
*/
