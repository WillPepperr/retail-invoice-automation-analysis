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
Data source: NATIONAL_VENDOR_INVOICES_2025, NATIONAL_VENDOR_INVOICES_2024 (fy_2025 vide)

Returns vendor_ids with multiple vendor_name values

Notes:
	- Duplicate vendor_name values were identified for some vendor_ids
	- After discussing with data team, the vendor numbers are arbitrary and can be reformed 
	  to any reasonable value


*/
