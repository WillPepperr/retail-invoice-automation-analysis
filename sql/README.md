# Overview of SQL queries 

## Cleaning/Validating

###  Data overview [01_data_overview.sql](sql_cleaning/01_data_overview.sql)
    -I started by getting a high-level understanding of the invoice data—how much there is, what time period it covers, and how many vendors, stores, and categories appear. This set the baseline for everything that followed.

### Invoice volume by month (02_invoice_histogram.sql)
Next, I looked at invoice counts over time to make sure the data was complete and behaved as expected, and to spot any missing months or unusual spikes early on.



### Vendor name validation (06_validate_vendor_names.sql)
Before grouping or reporting by vendor, I checked for inconsistent or duplicate vendor names that could split results and distort analysis.


### Clean last-year view with normalized vendors (09_vendor_last_year_view.sql)
I rebuilt the last-year view using the cleaned vendor IDs so all downstream analysis reflected the corrected vendor structure.

## Analysis 

### Labor cost analysis (12_labor_cost_analysis.sql)
I used processing timestamps to estimate labor time and cost, adding an operational perspective to the financial data.

### Labor time validation (13_labor_time_check.sql)
I checked for unusually short or long processing times to confirm that the labor calculations were based on reasonable data.

## ELT Schema

### Last-year data view (03_last_year_view.sql)
I created a consistent “last year” view of the data so that all later analysis would use the same time window instead of re-defining dates repeatedly.

### Fact table creation (13_fact_table_creator.sql)
I consolidated the cleaned invoice data into a central fact table to make analysis and reporting simpler and faster.

### Vendor dimension refinement (14_vendor_dim_table_creator.sql)
I finalized the vendor dimension to ensure it aligned cleanly with the fact table and supported consistent joins.

### Store dimension creation (15_store_dim_table_creator.sql)
I created a store dimension to separate store attributes from transactions and improve clarity in reporting.

### Date dimension creation (16_date_dim_creator.sql)
I added a date dimension to support consistent time-based analysis and make trends easier to query.