from __future__ import annotations

from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


class Db2SqlOperator(SQLExecuteQueryOperator):
    """
    Thin wrapper to use Db2 connection id by default.
    """
    template_fields = ("sql", "parameters")

    def __init__(self, *, conn_id: str = "db2_default", **kwargs):
        super().__init__(conn_id=conn_id, **kwargs)
