SELECT
    EXTRACT(YEAR FROM date) AS year,
    COUNT(*) AS count_2024
FROM
    national_vendor_invoices_2024
GROUP BY EXTRACT(YEAR FROM date)

UNION ALL 

SELECT
    EXTRACT(YEAR FROM date) AS year,
    COUNT(*) AS count_2025
FROM 
    national_vendor_invoices_2025 
GROUP BY EXTRACT(YEAR FROM date)
;


/*
Run date: 2025-12-01
Data source: national_vendor_invoices_2025, national_vendor_invoices_202

Total invoices from national vendors by year:

 | Year  | invoice_count|
 |-------|--------------|
 | 2024  | 8443032      |
 | 2025  | 6760290      |

Notes:
 - 15M+ national invoices processed across the 300 stores in past 2 years
 - Needs a view for annual analysis, fiscal Q2 2024 - fiscal Q2 2025(Octoeber 2024 - October 2025) 


*/
