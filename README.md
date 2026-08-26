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

**PostgreSQL → Extract → Process → Transform → Aggregate → Streamlit Dashboard**

| Stage | Technology | Purpose |
|---|---|---|
| 🗄️ Source | PostgreSQL | Source Data |
| 📥 Extract | SQL + Python | Data Extraction |
| 🐍 Process | Pandas | Data Processing |
| 🔄 Transform | Pandas + NumPy | Cleaning, Mapping & Classification |
| 📊 Aggregate | Pandas | Pivot Tables & KPIs |
| ⚡ Dashboard | Streamlit | Interactive Analytics |

---

# 📥 1. Data Extraction

Data is extracted from PostgreSQL using SQL queries and processed in batches using Python.

### Key Techniques

- SQL-based data extraction
- PostgreSQL connectivity using Psycopg2
- Batch processing using `fetchmany()`
- Large dataset handling

### Extraction Process

```text
PostgreSQL
    ↓
SQL Query
    ↓
Psycopg2 Connection
    ↓
Batch Fetching
    ↓
Pandas DataFrame
