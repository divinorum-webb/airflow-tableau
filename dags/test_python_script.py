from datetime import datetime
import os

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# from tableau.scripts.test_get_users import main
# from tableau.scripts.test_get_users import query_user
from tableau.scripts.sample_save_users import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1)
}


def print_cwd():
    cwd = os.getcwd()
    return cwd


with DAG(
    'test_script',
    default_args=default_args,
    catchup=False,
    schedule_interval='0 7 * * *',
    max_active_runs=1
) as dag:

    start_script_example = BashOperator(
        task_id='start_script_example',
        bash_command="echo 'STARTING PYTHON SCRIPT EXAMPLE'"
    )

    print_cwd = PythonOperator(
        task_id='print_cwd',
        python_callable=print_cwd
    )

    # run_python_script = PythonOperator(
    #     task_id='run_python_script',
    #     python_callable=query_user,
    #     op_kwargs={'user_id': '1a853d3e-8d87-4cfc-8999-455a903595f2'}
    # )

    run_python_script = PythonOperator(
        task_id='run_python_script',
        python_callable=main
    )

    end_script_example = BashOperator(
        task_id='end_script_example',
        bash_command="echo 'ENDING PYTHON SCRIPT EXAMPLE'"
    )

    start_script_example >> print_cwd >> run_python_script >> end_script_example
