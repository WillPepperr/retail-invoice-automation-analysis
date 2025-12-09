-- Finds potential faulty vendor names
-- Used to validate all vendor names were valid and uniform, each only having 1 instance to assign a unique vendor_id

WITH vendors AS (
    SELECT DISTINCT vendor_name
    FROM RETAIL_ANALYTICS.CLEAN.VENDOR_INVOICES_LAST_YEAR
),
pairs AS (
    SELECT
        v1.vendor_name AS name_1,
        v2.vendor_name AS name_2,
        EDITDISTANCE(v1.vendor_name, v2.vendor_name) AS edit_distance
    FROM vendors v1
    JOIN vendors v2
        ON v1.vendor_name < v2.vendor_name  
)
SELECT
    name_1,
    name_2,
    edit_distance
FROM pairs
WHERE edit_distance BETWEEN 1 AND 3 
ORDER BY edit_distance, name_1, name_2
LIMIT 500;


/*
Run date: 2025-12-01
*/
