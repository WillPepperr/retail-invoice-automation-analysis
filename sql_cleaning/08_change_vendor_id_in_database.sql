
-- Change vendor IDs to the new IDs Generated in the DIM_VENDOR table

UPDATE RETAIL_ANALYTICS.CLEAN.VENDOR_INVOICES_2024 t
SET vendor_id = d.new_vendor_id
FROM RETAIL_ANALYTICS.CLEAN.DIM_VENDOR d
WHERE t.vendor_name = d.vendor_name;  



UPDATE RETAIL_ANALYTICS.CLEAN.VENDOR_INVOICES_2025 t
SET vendor_id = d.new_vendor_id
FROM RETAIL_ANALYTICS.CLEAN.DIM_VENDOR d
WHERE t.vendor_name = d.vendor_name;


/*
Run date: 2025-12-01
*/
