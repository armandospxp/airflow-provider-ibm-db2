[![PyPI version](https://badge.fury.io/py/airflow-provider-ibm-db2.svg)](https://pypi.org/project/airflow-provider-ibm-db2/)

# airflow-provider-ibm-db2

Provider de **Apache Airflow** para conectarse a **IBM Db2** con `ibm_db_dbi` (nativo) y _fallback_ a `pyodbc`.
Incluye Hook y Operators básicos, ejemplo de DAG, y tests.

> Estado: **MVP inicial** — pensado para evolucionar con tu feedback y PRs.

## Características
- `Db2Hook` con detección de driver: `ibm_db_dbi` → `pyodbc` (fallback).
- `Db2SqlOperator` para ejecutar SQL parametrizado (basado en `SQLExecuteQueryOperator`).
- `Db2StoredProcedureOperator` para invocar `CALL schema.proc(?,?)`.
- `Db2CheckOperator` para chequeos de data quality (conteos/valores).
- `bulk_load()` mediante `SYSPROC.ADMIN_CMD('LOAD/IMPORT ...')` (si el usuario tiene permisos).
- Ejemplo de DAG y tests con `pytest`.

## Instalación (editable)
```bash
pip install -e .[dev]
```

## Configurar conexión en Airflow
Crea una **Connection** con ID `db2_default`:
- **Conn Type**: `Db2` (cadena libre) o `Generic`
- **Host**: `hostname`  | **Port**: `50000`
- **Schema**: `DBNAME`  | **Login**: `user` | **Password**: `******`
- **Extra (JSON)** opcional:
```json
{
  "ssl": true,
  "currentSchema": "DB2ADMIN",
  "securityMechanism": "13"
}
```

## Uso rápido
Mira `src/airflow_provider_ibm_db2/example_dags/example_db2_dag.py`

## Roadmap corto
- [ ] Transfer operators (Db2→Parquet, Db2→Postgres)
- [ ] Sensible defaults de aislamiento y reintentos
- [ ] Matriz de compatibilidad (DB2 LUW 11.1/11.5, Python 3.9–3.12, Airflow ≥2.7)

## Licencia
MIT
