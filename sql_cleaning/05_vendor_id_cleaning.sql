WITH cte AS 
(
SELECT
    vendor_id                               AS vendor_id,
    vendor_name                             AS vendor_name,
    RANK() OVER(
        PARTITION BY vendor_id 
        ORDER BY vendor_name DESC)          AS name_to_id_count
FROM 
    NATIONAL_VENDOR_INVOICES_LAST_YEAR
GROUP BY 
    vendor_id , vendor_name

)

SELECT
    DISTINCT vendor_id,
    name_to_id_count
FROM cte 
WHERE
    name_to_id_count > 1 
ORDER BY 
    name_to_id_count DESC 
;


/* 


/*
Run date: 2025-12-01
*/
