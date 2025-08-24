# Roadmap — airflow-provider-ibm-db2

This document outlines the planned evolution of the **Apache Airflow provider for IBM Db2**.  
It is meant as a living document — contributions, issues, and feedback are welcome!

---

## ✅ Current status
- [x] **Initial MVP** published on PyPI (`0.1.0`)
- [x] Basic `Db2Hook` with driver auto-detection (`ibm_db_dbi` → `pyodbc`)
- [x] Operators for SQL, Stored Procedures, and basic Checks
- [x] Example DAG and unit tests

---

## 🟦 Next milestones

### `0.2.x` — Quality & Compatibility
- [ ] Expand unit tests (mocked connections and operators)
- [ ] Improve CI with matrix for Python 3.9–3.12, Airflow 2.7–2.9
- [ ] Enhance connection handling (DSN strings, advanced SSL options)
- [ ] Improve logging and error messages

---

### `0.3.x` — New Operators
- [ ] **Db2ToParquetOperator** — export query results to Parquet/CSV
- [ ] **Db2ToPostgresOperator** — replicate/query-transfer to Postgres
- [ ] **Db2BulkLoadOperator** — leverage `ADMIN_CMD('LOAD FROM ...')`
- [ ] **Db2UnloadOperator** — export large volumes (unload pattern)

---

### `0.4.x` — Data Quality & Observability
- [ ] **Db2CheckOperator** with richer conditions (`row_count > 0`, `sum(col) = expected`)
- [ ] **Db2ValueCheckOperator** — validate a query returns expected value
- [ ] **Db2IntervalCheckOperator** — compare values across time periods
- [ ] Structured logging of queries and execution times

---

### `0.5.x` — Community Extras
- [ ] Sensible defaults: query timeout, retry policy, isolation levels
- [ ] Richer connection extras (`keepAlive`, CLI flags, etc.)
- [ ] Async hooks (experimental, asyncio-based)
- [ ] Documentation with multiple DAG examples

---

### `1.0.0` — Stable Release
- [ ] Compatibility matrix for **IBM Db2 LUW 11.1, 11.5, 12.x**
- [ ] CI with official IBM Db2 container for integration testing
- [ ] Verified with Airflow 2.7–3.0
- [ ] Migration guide for users
- [ ] Semantic versioning and long-term support

---

## 🤝 How to contribute
- Open issues to suggest features or report bugs
- Submit PRs with enhancements
- Comment on Discussions to help shape priorities

---

## 📌 Notes
- Roadmap items are tentative and may be re-prioritized based on community needs.
- Suggestions are always welcome!