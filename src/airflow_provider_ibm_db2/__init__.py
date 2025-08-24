from __future__ import annotations

__version__ = "0.1.0"

def get_provider_info():
    return {
        "package-name": "airflow-provider-ibm-db2",
        "name": "IBM Db2 provider",
        "description": "Hook + Operators for IBM Db2 (ibm_db_dbi / pyodbc fallback)",
        "hook-class-names": [
            "airflow_provider_ibm_db2.hooks.db2.Db2Hook",
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow_provider_ibm_db2.hooks.db2.Db2Hook",
                "connection-type": "db2",
            }
        ],
        "versions": [__version__],
    }
