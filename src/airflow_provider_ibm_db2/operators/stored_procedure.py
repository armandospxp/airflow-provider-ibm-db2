from __future__ import annotations

from typing import Iterable, Optional
from airflow.models import BaseOperator
from airflow.utils.context import Context
from airflow_provider_ibm_db2.hooks.db2 import Db2Hook


class Db2StoredProcedureOperator(BaseOperator):
    template_fields = ("parameters",)

    def __init__(
        self,
        *,
        procedure: str,
        parameters: Optional[Iterable] = None,
        db2_conn_id: str = "db2_default",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.procedure = procedure
        self.parameters = parameters
        self.db2_conn_id = db2_conn_id

    def execute(self, context: Context) -> None:
        hook = Db2Hook(db2_conn_id=self.db2_conn_id)
        if self.parameters:
            placeholders = ",".join(["?"] * len(self.parameters))
        else:
            placeholders = ""
        sql = f"CALL {self.procedure}({placeholders})"
        hook.run(sql, parameters=self.parameters)
