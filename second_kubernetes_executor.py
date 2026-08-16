from datetime import datetime
import time

from airflow import DAG
from airflow.operators.python import PythonOperator


def keep_worker_alive():
    print("Worker pod is alive!")
    print("Sleeping for 10 minutes...")

    time.sleep(600)

    print("10 minutes finished.")


with DAG(
    dag_id="test_kubernetes_worker",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test_worker = PythonOperator(
        task_id="keep_worker_alive",
        python_callable=keep_worker_alive,
    )
