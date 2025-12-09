# Retail Invoice Analysis

## Scenerio
A large grocery retailer with 290 stores is implementing a new inventory management system which applies ML/AI interfaces to support better ordering and inventory management. It connects seemlessly to the current corporate ERP, and is estimated to save over $45 million by anticipating and preventing product shrinkage, and auto pricing adjustments to meet dynamic market conditions. The vendor providing the system is offing an additional AI recieving system, promising to automate inventory checkins possible by both local and national vendors. It requires vendor agreement to use, but can eliminate the need for a user to be present with a success rate of 80%. 


## (actor use diagrams go here) 




## Business Question

### How much would be saved, in labor cost, if recieving at retail stores was automated for vendors?

#### Assumptions: 
    - Every store utalizes the technology, and every vendor adopts and accepts its use
    - Labor costs $20 an hour on average, 5 minutes of overhead productivity are lost on average per invoice 
    - 80% effective at making the process autonomous, and 20% will have to be applied manually, effectively reducing savings by 20%


### Given the system is adopted, which vendors are priority to accept the new recieving system?
#### Assumptions:
    - Vendors with higher volume and longer check-in times are prioritized to maximize cost savings
    - 80% of invoices will be autonomus 

### Executives speculate at least $2M in annual cost savings are needed to justify implementation, which senerios of vendors accepting this new system would be needed? 
#### Assumptions:
    - 80% of invoices will be autonomous 


## What I want to showcase

### UML diagrams describing each system and how they operate using MS Viso ✅
### Data pipeline in analysis, the systematic apporach I took to solve the problem
{
    ELT Method:
    Transformded 2 CSV files -> Parquet 
    Uploaded parquet files -> Snowflake
    Take data in Snowflake (maybe make in star schema?) -> Clean performative dataset for BI 
    Clean Snowflake data -> PowerBI report
    
}
### Data cleaning records, showcasing documentation done for data cleaning ✅ 
### Results derived and supported by the data. Actionable recomendaitons for adopting, not addopting, and strategy for adoption using other systems 
### Active invoice dashboard to monitor invoice entries from snowflake
