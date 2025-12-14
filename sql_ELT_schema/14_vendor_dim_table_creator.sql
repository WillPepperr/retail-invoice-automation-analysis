-- Vendor Dimention table for star schema and Power BI performance

CREATE OR REPLACE TABLE RETAIL_ANALYTICS.CLEAN.DIM_VENDOR AS 

SELECT 
    vendor_id,
    vendor_name,
    vendor_size,
    vendor_category 

FROM 
    VENDOR_INVOICES_2024

UNION

SELECT 
    vendor_id,
    vendor_name,
    vendor_size,
    vendor_category 
FROM 
    VENDOR_INVOICES_2025


/* 
Run Date: 12/10/25
*/
