#  Data Transformation (ELT)

After loading the origional Parquet file into Snowflake, I transformed the wide transactional dataset into a clean, analytics-ready star schema using SQL. The source data combined store, vendor, date, and invoice attributes in a single table, which I normalized by separating descriptive fields into dedicated dimension tables (store, vendor, and date) while retaining transactional metrics in a central fact table. This ELT approach reduced redundancy, enforced consistent keys, and improved query performance, in preperation for being loaded into Power BI.

<table>
  <tr>
    <td align="center">
      <img src="/visuals/origional_data_format.png" width="450"/>
      <br/> 
      <strong>Origional Structure</strong>
    </td>
    <td align="center">
      <img src="/visuals/star_schema_diagram.png"/>
      <br/>
      <strong>Transformed Star Schema</strong>
    </td>
  </tr>
</table>                              

#### Table creation queries: 
  [Fact Table](/data/sql_queries/sql_ELT_schema/13_fact_table_creator.sql)
  [Vendor Dim](/data/sql_queries/sql_ELT_schema/14_vendor_dim_table_creator.sql)
  [Store Dim](/data/sql_queries/sql_ELT_schema/15_store_dim_table_creator.sql)
  [Date Dim](/data/sql_queries/sql_ELT_schema/16_date_dim_creator.sql)