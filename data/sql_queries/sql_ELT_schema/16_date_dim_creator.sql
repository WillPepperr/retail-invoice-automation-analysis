CREATE OR REPLACE TABLE DIM_DATE AS 
SELECT
    date_id,
    TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD') AS full_date,

    YEAR(TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD'))      AS year,
    MONTH(TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD'))     AS month, 
    TO_CHAR(TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD'), 'DY')    AS day_name_abbrev,
    DAYOFWEEK(TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD'))   AS day_of_week,
    IFF(DAYOFWEEK(TO_DATE(TO_VARCHAR(date_id), 'YYYYMMDD')) IN (1,7), TRUE, FALSE) AS is_weekend
FROM(
    SELECT DISTINCT date_id
    FROM VENDOR_INVOICES
)
ORDER BY full_date;

/*
Date Ran: Dec 14 2025
*/
