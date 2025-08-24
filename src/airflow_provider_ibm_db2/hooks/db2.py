from __future__ import annotations

from typing import Any, Iterable, Optional
import logging

from airflow.providers.common.sql.hooks.sql import DbApiHook

log = logging.getLogger(__name__)


class Db2Hook(DbApiHook):
    """
    Minimal Db2 Hook with ibm_db_dbi primary driver and pyodbc fallback.
    Connection extras supported (JSON):
      - ssl: bool
      - currentSchema: str
      - securityMechanism: str/int (e.g., 13)
      - odbc_dsn: explicit ODBC DSN name if using pyodbc
    """
    conn_name_attr = "db2_conn_id"
    default_conn_name = "db2_default"
    hook_name = "IBM Db2"

    def __init__(self, *args, db2_conn_id: str = default_conn_name, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db2_conn_id = db2_conn_id
        self._driver = None  # "ibm_db_dbi" or "pyodbc"

    def get_conn(self):
        conn = self.get_connection(self.db2_conn_id)
        extra = conn.extra_dejson or {}

        # Try ibm_db_dbi first
        try:
            import ibm_db_dbi  # type: ignore
            self._driver = "ibm_db_dbi"
            parts = [
                f"DATABASE={conn.schema};",
                f"HOSTNAME={conn.host};" if conn.host else "",
                f"PORT={conn.port};" if conn.port else "",
                "PROTOCOL=TCPIP;",
                f"UID={conn.login};" if conn.login else "",
                f"PWD={conn.password};" if conn.password else "",
            ]
            if extra.get("ssl"):
                parts.append("SECURITY=SSL;")
            if extra.get("currentSchema"):
                parts.append(f"CURRENTSCHEMA={extra['currentSchema']};")
            if extra.get("securityMechanism"):
                parts.append(f"SECURITYMECHANISM={extra['securityMechanism']};")
            dsn = "".join(parts)
            return ibm_db_dbi.connect(dsn, "", "")
        except Exception as e:  # noqa: BLE001
            log.info("ibm_db_dbi not available or failed: %s — falling back to pyodbc", e)

        # Fallback to pyodbc
        import pyodbc  # type: ignore
        self._driver = "pyodbc"

        dsn = extra.get("odbc_dsn")
        if dsn:
            conn_str = f"DSN={dsn};UID={conn.login};PWD={conn.password}"
        else:
            # Free-form connection string
            conn_str = (
                f"DRIVER={{IBM DB2 ODBC DRIVER}};"
                f"DATABASE={conn.schema};"
                f"HOSTNAME={conn.host};PORT={conn.port};PROTOCOL=TCPIP;"
                f"UID={conn.login};PWD={conn.password};"
            )
            if extra.get("ssl"):
                conn_str += "SECURITY=SSL;"

        return pyodbc.connect(conn_str, autocommit=False)

    def get_uri(self) -> str:
        # purely informational
        c = self.get_connection(self.db2_conn_id)
        return f"db2://{c.login}:***@{c.host}:{c.port}/{c.schema}"

    def bulk_load(self, table: str, file_path: str, method: str = "LOAD", commitcount: int = 5000) -> None:
        """
        Perform high-throughput bulk load using ADMIN_CMD.
        Requires privileges on SYSPROC.ADMIN_CMD.
        """
        file_path_escaped = file_path.replace("'", "''")
        cmd = (
            f"{method} FROM '{file_path_escaped}' OF DEL "
            f"MODIFIED BY COLDEL,; DUMPFILE DELPRIORITY 1 "
            f"COMMITCOUNT {commitcount} INSERT INTO {table}"
        )
        sql = f"CALL SYSPROC.ADMIN_CMD('{cmd}')"
        self.run(sql)

    def run(self, sql: Any, autocommit: bool = False, parameters: Optional[Iterable] = None) -> None:
        """
        Override to ensure commits on success when not autocommit.
        """
        conn = self.get_conn()
        try:
            cur = conn.cursor()
            if parameters:
                cur.execute(sql, parameters)
            else:
                cur.execute(sql)
            if autocommit or getattr(conn, "autocommit", False):
                pass
            else:
                conn.commit()
        finally:
            try:
                cur.close()
            except Exception:  # noqa: BLE001
                pass
            try:
                conn.close()
            except Exception:  # noqa: BLE001
                pass
