# Retail Invoice Analysis

## Table of Contents
- [Scenario](#scenario)
- [Executive Summary](#executive-summary)
- [Data Structure](#data-structure)
- [Deep-Dive Analysis](#key-operational-metrics)
- [Recommended Next Steps](#recommended-next-steps)
- [Scenario Modeling & Controls](#scenario-modeling--controls)
- [Data Schema](/data/data_structure.md)

## Project Context

- **Organization Type:** National grocery retailer
- **Store Count:** 290 locations
- **Time Period Analyzed:** Prior 12 months
- **Primary Audience:** Operations leadership
- **Secondary Stakeholders:** Finance, Vendor Management, IT Transformation
- **Objective:** Quantify labor savings opportunity from automated invoice receiving

## Scenario
A national grocery retailer with 290 stores is implementing a new inventory management system that applies ML/AI interfaces to support more effective purchasing and inventory management. It seamlessly integrates with the current corporate ERP, Inventory management, and SCM systems, and is estimated to save over $45 million annually by anticipating and preventing product shrinkage, as well as making auto pricing adjustments to meet dynamic market conditions. The vendor providing the system is offering an additional automated receiving system, promising to automate inventory check-ins by both local and national vendors. It requires vendor agreement to use, but it can eliminate the need for a user to be present, as 80% of transactions can be performed autonomously. This system also eliminates the need for physical invoices to be manually photocopied, which saves substantial labor costs.

<table>
  <tr>
    <td align="center">
      <img src="visuals/current_process.png" width="450"/>
      <br/> 
      <strong>Current Process</strong>
    </td>
    <td align="center">
      <img src="visuals/proposed_process.png" width="450"/>
      <br/>
      <strong>Proposed Process</strong>
    </td>
  </tr>
</table>

## Business Questions

### 1.) How much would be saved, in labor cost, if recieving at retail stores was automated for all vendors?

### 2.) Given the system is adopted, which vendors and regions are priority to accept the new recieving system?

### 3.) Executives speculate at least $2M in annual cost savings are needed to justify implementation, which senerios of vendors accepting this new system would be needed? 

#### Assumptions:
> - Every store utalizes the technology, and every vendor adopts and accepts its use
> - Labor costs $20 an hour on average, 5 minutes of overhead productivity are lost while photocopying invoices on average
> - 80% effective at making the process autonomous, and 20% will have to be applied manually and would take the same amount of time as the old system to validate, effectively reducing savings by 20% compared to perfect conditions

#### Caveats & Considerations
> - Vendor participation is voluntary
> - Automation effectiveness may vary by vendor and delivery type
> - Labor rates vary by region but are modeled at an average rate
> - Invoice complexity and exception handling are not explicitly modeled

---

## Executive Summary

Based on invoice activity over the most recent 12-month period, total estimated labor cost associated with manual invoice check-in is \$7.14M annually across 290 stores. Under the assumed conditions—an average labor rate of \$20/hr and 80% automation effectiveness—the estimated achievable labor savings total \$5.71M annually, exceeding the $2M executive justification threshold by a wide margin.

**Invoice-Level Averages**
- **Total labor time:** 8.98 minutes
- **Check-in time:** 3.98 minutes
- **Labor cost per invoice:** $2.99

These findings indicate invoice processing is a meaningful and repeatable operational cost center suitable for automation.

--- 

## Data Structure

- Invoice-level fact data
- Vendor and vendor-category dimensions
- Date dimension for time-based aggregation
- See [Data Schema](data/data_structure.md) for technical details

![Alt text](visuals/star_schema_diagram.png)

--- 

## Analysis Deep Dive

## Key Operational Metrics

### Invoice Processing Efficiency
- **Average Check-in Time:** 3.98 minutes  
- **Average Total Labor Time per Invoice:** 8.98 minutes  
- **Average Labor Cost per Invoice:** $2.99  

Check-in activities alone account for approximately **44% of total invoice labor time**, reinforcing the value of automation even when partial manual intervention remains necessary.

## Vendor Cost Concentration

### Annual Labor Cost by Vendor
- **Total vendor invoice labor cost:** $7.14M
- **Vendors > \$100K:** 76% ($5.4M)
- **\$20K–\$80K vendors:** 13% ($0.9M)
- **< \$20K vendors:** 11% ($0.8M)

Labor cost is highly concentrated among a small subset of vendors, making targeted adoption strategies viable and impactful.

## Vendor Category Insights

### Labor Cost Distribution
- **Produce:** $2.3M (32%)
- **Bread:** $2.0M (29%)
- **Dairy:** $1.2M (17%)
- **Liquor, Beverages, Frozen, Snacks:** $1.7M combined (22%)

Produce and bread alone account for over **60% of total labor cost**, supporting category-led rollout strategies.

## Geographical Impact 

## Temporal Trends

Invoice labor costs remain **stable month-over-month** with no significant seasonality, supporting predictable annualized savings projections and reduced implementation risk.

## Adoption Threshold Analysis

- **Top 32 vendors:** \$110K–\$190K annual labor cost each
- **14–17 vendors adopted nationally** exceed the $2M savings threshold
- Full national adoption materially exceeds required ROI

This supports phased vendor rollout strategies.

## Operational Complexity Considerations

### Check-in Time by Delivery Size
- **Large deliveries:** ~4.3 minutes
- **Medium deliveries:** ~3.9 minutes
- **Small deliveries:** ~3.2 minutes

Automation benefits apply broadly across delivery sizes.

## Implications for Operations Leadership

- Invoice processing is a recurring, structural labor cost
- Savings are predictable and concentrated
- Partial adoption yields strong returns
- Regional or category-led rollouts accelerate value realization
- Automation reduces non-value-added labor without disrupting store operations

## Recommended Next Steps
- Pilot automated receiving with top 10–15 national vendors
- Validate labor time reductions in live store environments
- Incorporate regional wage variance into savings model

## Scenario Modeling & Controls

The BI dashboard supports real-time scenario analysis through:
- Adjustable wage rate assumptions
- Variable date ranges
- Vendor category and cost-tier filtering
- Automation effectiveness slider

These controls allow stakeholders to validate savings under conservative or aggressive assumptions.

### Scenerio Analysis Dashboard
![Alt text](visuals/bi_preview.gif)

### Deep-Dive Analysis View
![Alt text](visuals/deep_dive_bi_visualization.png)
---
                              