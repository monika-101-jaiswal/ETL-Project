<div align="center">

# ⚡ Smart Meter ETL & Analytics Dashboard

### End-to-End Data Engineering & Analytics Project

<p>
  <b>Python</b> •
  <b>PostgreSQL</b> •
  <b>Pandas</b> •
  <b>NumPy</b> •
  <b>Streamlit</b>
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-blue?style=for-the-badge&logo=pandas">
<img src="https://img.shields.io/badge/NumPy-Numerical-orange?style=for-the-badge&logo=numpy">
<img src=["https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit"](https://github.com/monika-101-jaiswal/ETL-Project/blob/0ff046530b7f0eeab21afa4615ac0419f4092895/Screenshot%202026-08-16%20173519.png)>

</div>

---

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) and analytics workflow** for large-scale smart meter data.

The application extracts data from **PostgreSQL**, processes large datasets in batches using **Python and Pandas**, performs data cleaning and transformation, applies business-based classification logic, generates analytical summaries, and presents the processed results through an interactive **Streamlit dashboard**.

The project demonstrates practical implementation of:

- 🐍 Python-based ETL
- 🗄️ SQL & PostgreSQL
- 📊 Data Analytics
- 🔄 Data Transformation
- 📈 Data Aggregation
- 🖥️ Streamlit Dashboard Development

---

# 🔄 ETL Workflow

<div align="center">

<table>
<tr>

<td align="center">
<h3>🗄️</h3>
<b>PostgreSQL</b><br>
Source Data
</td>

<td>➡️</td>

<td align="center">
<h3>📥</h3>
<b>EXTRACT</b><br>
SQL + Python
</td>

<td>➡️</td>

<td align="center">
<h3>🐍</h3>
<b>PROCESS</b><br>
Pandas
</td>

<td>➡️</td>

<td align="center">
<h3>🔄</h3>
<b>TRANSFORM</b><br>
Clean + Map + Classify
</td>

<td>➡️</td>

<td align="center">
<h3>📊</h3>
<b>AGGREGATE</b><br>
Pivot + KPIs
</td>

<td>➡️</td>

<td align="center">
<h3>⚡</h3>
<b>STREAMLIT</b><br>
Dashboard
</td>

</tr>
</table>

</div>

---

# 📥 1. Data Extraction

Data is extracted from PostgreSQL using SQL queries and processed in batches using Python.

### Key Techniques

- SQL-based data extraction
- PostgreSQL connectivity using Psycopg2
- Batch processing using `fetchmany()`
- Large dataset handling

<div align="center">

</div>

---

# 🔄 2. Data Transformation

After extraction, the data goes through multiple transformation steps using Pandas and NumPy.

### Transformation Steps

- Remove unnecessary spaces
- Standardize text values
- Convert numeric columns
- Handle missing values
- Map Supply Type
- Apply classification rules
- Generate analytical categories

<div align="center">

### 🔹 Transformation Logic

<img src="screenshots/02-data-transformation.png" width="90%">

</div>

---

# 📊 3. Data Aggregation & Analytics

The transformed data is aggregated to generate meaningful analytical summaries.

### Analytics Generated

- Category-wise counts
- Status-wise counts
- Type-wise distribution
- Category vs Status analysis
- Pivot summaries

<div align="center">

### 🔹 Aggregation & Analytics

<img src="screenshots/03-data-aggregation.png" width="90%">

</div>

---

# 🖥️ 4. Streamlit Dashboard

The processed results are passed to a Streamlit application for interactive visualization.

### Dashboard Components

<div align="center">

<table>
<tr>
<td align="center">📌<br><b>KPI Cards</b></td>
<td align="center">📊<br><b>Category Analysis</b></td>
<td align="center">📋<br><b>Status Analysis</b></td>
<td align="center">📥<br><b>CSV Export</b></td>
</tr>
</table>

</div>

<div align="center">

### 🔹 Streamlit Application

<img src="screenshots/04-streamlit-code.png" width="90%">

</div>

---

# 🚀 5. Final Dashboard

The final processed output is presented through an interactive Streamlit dashboard.

<div align="center">

<img src="screenshots/05-dashboard.png" width="95%">

</div>

---

# 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|:---:|:---|
| 🐍 **Python** | ETL & Data Processing |
| 🐼 **Pandas** | Data Cleaning & Transformation |
| 🔢 **NumPy** | Numerical Operations & Classification |
| 🗄️ **PostgreSQL** | Database & SQL Queries |
| 🔌 **Psycopg2** | PostgreSQL Connectivity |
| 📊 **Streamlit** | Interactive Dashboard |
| 📗 **Excel** | Reference / Mapping Data |

</div>

---

# ⚙️ Data Processing Pipeline

## 1️⃣ Extract

Data is extracted from PostgreSQL using SQL queries.

## 2️⃣ Clean

Data is standardized and prepared for transformation.

```text
Raw Data
   ↓
Remove Spaces
   ↓
Standardize Text
   ↓
Handle Missing Values
   ↓
Convert Numeric Fields
