#  Data Transformation (ELT)

After loading the origional Parquet file into Snowflake, the transaction table was transformed from the wide transactional dataset into a clean, analytics-ready star schema using SQL. The source data combined store, vendor, date, and invoice attributes in a single table, which were normalized by separating descriptive fields into dedicated dimension tables (store, vendor, and date) while retaining transactional metrics in a central fact table. 

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
