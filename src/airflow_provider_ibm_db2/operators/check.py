from __future__ import annotations

from airflow.providers.common.sql.operators.sql import SQLCheckOperator, SQLValueCheckOperator


class Db2CheckOperator(SQLCheckOperator):
    def __init__(self, *, conn_id: str = "db2_default", **kwargs):
        super().__init__(conn_id=conn_id, **kwargs)


class Db2ValueCheckOperator(SQLValueCheckOperator):
    def __init__(self, *, conn_id: str = "db2_default", **kwargs):
        super().__init__(conn_id=conn_id, **kwargs)
