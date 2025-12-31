-- Create store dimention for star schema and Power BI performance

CREATE OR REPLACE TABLE DIM_STORE AS 

SELECT 
    store_id,
    city,
    state,
    region

FROM 
    VENDOR_INVOICES


/*
Ran: 12/17/25
*/
