-- Created vendor dimention table, and assigned unique arbitrary IDs.

CREATE TABLE RETAIL_ANALYTICS.CLEAN.DIM_VENDOR AS 
WITH all_vendors AS 
(
    SELECT DISTINCT vendor_name FROM RETAIL_ANALYTICS.CLEAN.VENDOR_INVOICES_2024
    UNION
    SELECT DISTINCT vendor_name FROM RETAIL_ANALYTICS.CLEAN.VENDOR_INVOICES_2025
)

SELECT
    DENSE_RANK() OVER (ORDER BY vendor_name) AS new_vendor_id,
    vendor_name
FROM all_vendors
;



/*
Run date: 2025-12-01
*/
