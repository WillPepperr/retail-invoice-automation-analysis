# Overview of SQL queries 

## Cleaning/Validating

###  Data overview (01_data_overview.sql)
    -I started by getting a high-level understanding of the invoice data—how much there is, what time period it covers, and how many vendors, stores, and categories appear. This set the baseline for everything that followed.

### Invoice volume by month (02_invoice_histogram.sql)
Next, I looked at invoice counts over time to make sure the data was complete and behaved as expected, and to spot any missing months or unusual spikes early on.

### Last-year data view
I created a consistent “last year” view of the data so that all later analysis would use the same time window instead of re-defining dates repeatedly.

### Vendor name validation
Before grouping or reporting by vendor, I checked for inconsistent or duplicate vendor names that could split results and distort analysis.

### Vendor dimension creation
I then created a clean vendor table with one row per vendor and a stable ID, so vendors could be referenced consistently across all data.

### Vendor ID cleanup in invoices
After defining a standard vendor ID, I updated the invoice data to use it, ensuring vendor reporting would be accurate and reliable.

### Clean last-year view with normalized vendors
I rebuilt the last-year view using the cleaned vendor IDs so all downstream analysis reflected the corrected vendor structure.

### Labor cost analysis
I used processing timestamps to estimate labor time and cost, adding an operational perspective to the financial data.

### Labor time validation
I checked for unusually short or long processing times to confirm that the labor calculations were based on reasonable data.

### Fact table creation
I consolidated the cleaned invoice data into a central fact table to make analysis and reporting simpler and faster.

### Vendor dimension refinement
I finalized the vendor dimension to ensure it aligned cleanly with the fact table and supported consistent joins.

### Store dimension creation
I created a store dimension to separate store attributes from transactions and improve clarity in reporting.

### Date dimension creation
I added a date dimension to support consistent time-based analysis and make trends easier to query.