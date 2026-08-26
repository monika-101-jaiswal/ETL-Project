<div align="center">

# ⚡ Smart Meter ETL & Analytics Dashboard

### End-to-End Data Engineering & Analytics Project

<p>
  <b>🐍 Python</b> •
  <b>🗄️ PostgreSQL</b> •
  <b>🐼 Pandas</b> •
  <b>🔢 NumPy</b> •
  <b>📊 Streamlit</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-blue?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical-orange?style=for-the-badge&logo=numpy">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit">
</p>

</div>

---

# 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) and Analytics workflow** for large-scale smart meter data.

The application extracts data from **PostgreSQL**, processes large datasets using **Python and Pandas**, performs data cleaning and transformation, applies business-based classification logic, loads the processed data, generates analytical summaries, and presents the results through an interactive **Streamlit dashboard**.

### 🚀 Key Features

- 🐍 Python-based ETL
- 🗄️ PostgreSQL database integration
- 📥 SQL-based data extraction
- 🧹 Data cleaning and preprocessing
- 🔄 Business rule-based transformation
- 📊 Data aggregation and pivot analysis
- 📈 KPI generation
- 📥 Processed data loading
- 🖥️ Interactive Streamlit dashboard
- 🔎 Dynamic filters
- 📤 CSV export

---

# 🔄 ETL Workflow

<div align="center">

<table>
<tr>

<td align="center">

<h2>🗄️</h2>

<b>POSTGRESQL</b>

<br>

Source Data

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>📥</h2>

<b>EXTRACT</b>

<br>

SQL + Python

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>🧹</h2>

<b>CLEAN</b>

<br>

Pandas

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>🔄</h2>

<b>TRANSFORM</b>

<br>

Mapping + Rules

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>📥</h2>

<b>LOAD</b>

<br>

Database / CSV

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>📊</h2>

<b>ANALYTICS</b>

<br>

KPIs + Pivot

</td>

<td align="center">

<h2>➡️</h2>

</td>

<td align="center">

<h2>⚡</h2>

<b>STREAMLIT</b>

<br>

Dashboard

</td>

</tr>
</table>

</div>

---

# 📥 1. EXTRACT

<div align="center">

## 🗄️ PostgreSQL → Python

</div>

Data is extracted from PostgreSQL using SQL queries and Python.

### Extraction Process

```text
PostgreSQL
     ↓
SQL Query
     ↓
Psycopg2
     ↓
Batch Fetching
     ↓
Pandas DataFrame
