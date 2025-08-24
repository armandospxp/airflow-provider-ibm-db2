from __future__ import annotations

from datetime import datetime
from airflow import DAG
from airflow_provider_ibm_db2.operators.sql import Db2SqlOperator
from airflow_provider_ibm_db2.operators.stored_procedure import Db2StoredProcedureOperator
from airflow_provider_ibm_db2.operators.check import Db2CheckOperator

with DAG(
    dag_id="example_db2_mvp",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["example", "db2"],
) as dag:
    create_table = Db2SqlOperator(
        task_id="create_table",
        sql="CREATE TABLE IF NOT EXISTS STG.HEALTHCHECK(ID INT, MSG VARCHAR(100))",
    )

    insert_row = Db2SqlOperator(
        task_id="insert_row",
        sql="INSERT INTO STG.HEALTHCHECK(ID, MSG) VALUES (1, 'ok')",
    )

    check_count = Db2CheckOperator(
        task_id="check_count",
        sql="SELECT COUNT(*) FROM STG.HEALTHCHECK WHERE ID=1",
    )

    call_proc = Db2StoredProcedureOperator(
        task_id="call_proc",
        procedure="SYSPROC.ENV_GET_INST_INFO",
        parameters=[],
    )

    create_table >> insert_row >> check_count >> call_proc
