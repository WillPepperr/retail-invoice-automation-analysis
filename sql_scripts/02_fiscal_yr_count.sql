SELECT
    EXTRACT(YEAR FROM date) AS year,
    COUNT(*) AS count_2024
FROM
    NATIONAL_VENDOR_INVOICES_2024
WHERE
    date >= '09/01/2024'
GROUP BY EXTRACT(YEAR FROM date)

UNION ALL 

SELECT
    EXTRACT(YEAR FROM date) AS year,
    COUNT(*) AS count_2025
FROM
    NATIONAL_VENDOR_INVOICES_2025
WHERE
     date < '09/01/2025'
GROUP BY EXTRACT(YEAR FROM date)
;
/*
Run date: 2025-12-01
Data source: NATIONAL_VENDOR_INVOICES_2024, NATIONAL_VENDOR_INVOICES_2025 

Total invoices from national vendors by year:

 | Year  | invoice_count|
 |-------|--------------|
 | 2024  | 2819387      |
 | 2025  | 5990406      |

Notes:
	- ~8.8 million invoices in past year
	- Needs view to query from using this structure
*/
