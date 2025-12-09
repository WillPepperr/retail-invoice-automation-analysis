
-- Helps identify and understand the kind of mismatch between COUNT(vendor_id) and COUNT(vendor_name)

WITH pairs AS (
    SELECT DISTINCT
        vendor_id,
        vendor_name
    FROM VENDOR_INVOICES_LAST_YEAR
),
stats AS (
    SELECT
        vendor_id,
        vendor_name,
        COUNT(*) OVER (PARTITION BY vendor_name) AS ids_per_name,
        COUNT(*) OVER (PARTITION BY vendor_id)   AS names_per_id
    FROM pairs
)
SELECT
    vendor_id,
    vendor_name,
    ids_per_name,
    names_per_id,
    CASE
        WHEN ids_per_name = 1 AND names_per_id = 1
            THEN 'clean_1_to_1'
        WHEN ids_per_name > 1 AND names_per_id = 1
            THEN 'name_to_many_ids'
        WHEN ids_per_name = 1 AND names_per_id > 1
            THEN 'id_to_many_names'
        ELSE 'many_to_many'
    END AS mapping_flag
FROM stats
ORDER BY vendor_name, vendor_id
;

/*
Run date: 2025-12-01
*/
