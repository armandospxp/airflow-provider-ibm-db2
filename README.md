# airflow-provider-ibm-db2

[![PyPI version](https://badge.fury.io/py/airflow-provider-ibm-db2.svg)](https://pypi.org/project/airflow-provider-ibm-db2/)
[![Python Versions](https://img.shields.io/pypi/pyversions/airflow-provider-ibm-db2.svg)](https://pypi.org/project/airflow-provider-ibm-db2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/YOUR_GITHUB_USERNAME/airflow-provider-ibm-db2/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_GITHUB_USERNAME/airflow-provider-ibm-db2/actions)

**Apache Airflow provider** to connect to **IBM Db2** using `ibm_db_dbi` (native) with a _fallback_ to `pyodbc`.  
Includes basic Hook and Operators, an example DAG, and unit tests.

> Status: **Initial MVP** — designed to evolve with your feedback and contributions.

---

## ✨ Features
- `Db2Hook` with driver auto-detection: `ibm_db_dbi` → `pyodbc` (fallback).
- `Db2SqlOperator` to execute parameterized SQL (based on `SQLExecuteQueryOperator`).
- `Db2StoredProcedureOperator` to invoke `CALL schema.proc(?,?)`.
- `Db2CheckOperator` for data quality checks (counts/values).
- `bulk_load()` via `SYSPROC.ADMIN_CMD('LOAD/IMPORT ...')` (if the user has privileges).
- Example DAG and tests with `pytest`.

---

## ⚡ Installation (editable)
```bash
pip install -e .[dev]
```

---

## 🔧 Airflow Connection Setup
Create a **Connection** with ID `db2_default`:

- **Conn Type**: `Db2` (free text) or `Generic`  
- **Host**: `hostname`  | **Port**: `50000`  
- **Schema**: `DBNAME`  | **Login**: `user` | **Password**: `******`  

- **Optional Extra (JSON)**:
```json
{
  "ssl": true,
  "currentSchema": "DB2ADMIN",
  "securityMechanism": "13"
}
```

---

## 🚀 Quick Start
Check out the example DAG:  
`src/airflow_provider_ibm_db2/example_dags/example_db2_dag.py`

---

## 🗺️ Short-term Roadmap
- [ ] Transfer operators (Db2 → Parquet, Db2 → Postgres)  
- [ ] Sensible defaults for isolation level and retries  
- [ ] Compatibility matrix (DB2 LUW 11.1/11.5, Python 3.9–3.12, Airflow ≥2.7)  

---

## 📜 License
MIT
