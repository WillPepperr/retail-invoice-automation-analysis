create or replace view RETAIL_ANALYTICS.ANALYTICS.NATIONAL_VENDOR_INVOICES_LAST_YEAR(
	TRANSACTION_ID,
	STORE_ID,
	CITY,
	STATE,
	REGION,
	VENDOR_ID,
	VENDOR_NAME,
	VENDOR_CATEGORY,
	DATE_ID,
	DATE,
	SKU_COUNT,
	TOTAL_ITEMS,
	INVOICE_AMOUNT,
	VENDOR_SIZE,
	INVOICE_INITIATED_TS,
	INVOICE_FINISHED_TS
) as
SELECT *
FROM NATIONAL_VENDOR_INVOICES_2024
WHERE date >= '2024-10-01'::DATE

UNION ALL

SELECT *
FROM NATIONAL_VENDOR_INVOICES_2025
WHERE date < '2025-10-01'::DATE
;

-- Validate return values of dates

SELECT
    MIN(date)
FROM 
    NATIONAL_VENDOR_INVOICES_LAST_YEAR

UNION ALL 

SELECT
    MAX(date)
FROM 
    NATIONAL_VENDOR_INVOICES_LAST_YEAR
;


/*
Run date: 2025-12-01
Data source: NATIONAL_VENDOR_INVOICES_2025, NATIONAL_VENDOR_INVOICES_2024

Created view for previous year 
Ensured valid dates returning correct min and max datae values

 | Date      |
 |-----------|
 | 2024-10-01|
 | 2025-09-30|

Notes:
	- Created view combing table data between 2024 and 2025 filtering between fiscal Q2 2024 through Q1
	- Calculations needed: checkin_minutes
*/
