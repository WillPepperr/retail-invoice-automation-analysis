-- Generate fact table to transfer unnormalized table to star schema for better BI performance.

CREATE OR REPLACE TABLE FACT_INVOICE AS
SELECT
    transaction_id,
    store_id,
    vendor_id,
    date_id,
    sku_count,
    total_items,
    invoice_amount,
    invoice_initiated_ts,
    invoice_finished_ts,
    ROUND(DATEDIFF('second', invoice_initiated_ts, invoice_finished_ts) / 60.0, 2) AS process_minutes
FROM VENDOR_INVOICES_2024

UNION ALL

SELECT
    transaction_id,
    store_id,
    vendor_id,
    date_id,
    sku_count,
    total_items,
    invoice_amount,
    invoice_initiated_ts,
    invoice_finished_ts,
    ROUND(DATEDIFF('second', invoice_initiated_ts, invoice_finished_ts) / 60.0, 2) AS process_minutes
FROM VENDOR_INVOICES_2025;

/* 
Ran:  12/10/25
*/
