-- Create store dimention for star schema and Power BI performance

CREATE OR REPLACE TABLE RETAIL_ANALYTICS.CLEAN.DIM_STORE AS 

SELECT 
    store_id,
    city,
    state,
    region

FROM 
    VENDOR_INVOICES_2024

UNION

SELECT 
    store_id,
    city,
    state,
    region
    
FROM 
    VENDOR_INVOICES_2025
