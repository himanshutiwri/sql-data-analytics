
---

# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

**End-to-end project leveraging SQL, Python, and Power BI** to evaluate vendor performance, optimize inventory, and drive strategic retail decisions.

---

## 📌 Table of Contents

* [Overview](#overview)
* [Business Problem](#business-problem)
* [Dataset](#dataset)
* [Tools & Technologies](#tools--technologies)
* [Data Cleaning & Preparation](#data-cleaning--preparation)
* [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
* [Key Insights](#key-insights)
* [Recommendations](#recommendations)
* [Download Dataset](#download-dataset)
* [Author & Contact](#author--contact)

---

## Overview

This project assesses **vendor efficiency and retail inventory dynamics** to deliver actionable insights for purchasing, pricing, and inventory optimization.
It includes a **complete end-to-end workflow**:

* **SQL** for ETL and data aggregation
* **Python** for data analysis, visualization, and statistical testing
* **Power BI** for interactive dashboards and business reporting

The aim is to enable **data-driven decisions** that enhance profitability and operational efficiency.

---

## Business Problem

Retail businesses face challenges such as:

* Identifying **underperforming brands** requiring pricing or promotional adjustments
* Understanding vendor contributions to sales and profits
* Evaluating the **impact of bulk purchasing**
* Managing **slow-moving inventory**
* Statistically validating differences in vendor profitability

This project addresses these problems using structured analysis and actionable recommendations.

---

## Dataset

* Multiple CSV files stored in the `/dataset/` folder (sales, vendors, inventory,purchase)
* Summary tables generated from raw data for analysis

---

## Tools & Technologies

* **SQL:** Common Table Expressions (CTEs), Joins, Filtering
* **Python:** Pandas, Matplotlib, Seaborn, SciPy
* **Power BI:** Interactive dashboards and visualizations

---

## Data Cleaning & Preparation

* Removed invalid transactions:

  * Gross Profit ≤ 0
  * Profit Margin ≤ 0
  * Sales Quantity = 0
* Created summary tables with **vendor-level metrics**
* Handled outliers, converted data types, merged lookup tables

---

## Exploratory Data Analysis (EDA)

**Negative/Zero Values Detected:**

* Gross Profit: Min -52,002.78 (loss-making sales)
* Profit Margin: Min -∞ (sales at zero or below cost)
* Unsold inventory highlights slow-moving stock

**Outliers Identified:**

* High freight costs (up to 257K)
* Large purchase/actual prices

**Correlation Insights:**

* Weak correlation between Purchase Price & Profit
* Strong correlation between Purchase Quantity & Sales Quantity (0.999)
* Negative correlation between Profit Margin & Sales Price (-0.179)

---

## Key Insights

* **Brands for Promotions:** 198 brands with low sales but high profit margins
* **Top Vendors:** Top 10 vendors account for 65.69% of purchases → risk of over-reliance
* **Bulk Purchasing:** Large orders achieve up to 72% cost savings per unit
* **Inventory Turnover:** $2.71M worth of unsold inventory indicates slow-moving stock

---

## Recommendations

* Diversify the vendor base to **reduce operational risk**
* Optimize **bulk purchasing strategies** for cost efficiency
* Reprice **slow-moving, high-margin brands**
* Strategically clear unsold inventory
* Implement targeted **marketing for underperforming vendors**

---

## Download Dataset

The **large dataset** for this project is available as a ZIP archive:

[📥 Download Dataset](https://drive.google.com/file/d/18AvO6pNTGgEM_NGm_0bUhNkAUouwVDH9/view?usp=sharing)

> The project is **end-to-end**, including **Python scripts, SQL queries, Power BI dashboards, and the full analysis report**.

---

Go to screenshot folder to catch some snapshots.
