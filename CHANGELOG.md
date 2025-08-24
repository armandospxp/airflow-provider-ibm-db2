# Changelog — airflow-provider-ibm-db2

All notable changes to this project will be documented in this file.  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added
- Roadmap for upcoming features (`ROADMAP.md`)
- Initial structure for CHANGELOG

---

## [0.1.1] — 2025-08-24
### Fixed
- Build and publish workflow adjustments for PyPI Trusted Publishing
- Pinned hatchling version to ensure compatibility with PyPI metadata validation

### Changed
- Updated project metadata in `pyproject.toml`

---

## [0.1.0] — 2025-08-23
### Added
- Initial MVP release on PyPI
- `Db2Hook` with driver auto-detection (`ibm_db_dbi` → `pyodbc` fallback)
- Basic operators:
  - `Db2SqlOperator`
  - `Db2StoredProcedureOperator`
  - `Db2CheckOperator`
- Example DAG in `example_dags/`
- Unit tests with `pytest`
