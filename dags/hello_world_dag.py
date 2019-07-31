from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from tableau.client.TableauServerConnection import TableauServerConnection


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1)
}


def initialize_tableau_conn():
    conn = TableauServerConnection()
    print(conn)


with DAG(
    'hello_world',
    default_args=default_args,
    catchup=False,
    schedule_interval='0 7 * * *',
    max_active_runs=1
) as dag:

    # wait_first_job = ExternalTaskSensor(
    #     task_id='wait_first_job',
    #     external_dag_id='tutorial',
    #     external_task_id='print_date',
    #     trigger_rule='all_done'
    # )

    start_hello_world = BashOperator(
        task_id='start_hello_world',
        bash_command="echo 'STARTING HELLO WORLD SAMPLE'"
    )

    initialize_tableau_conn = PythonOperator(
        task_id='initialize_tableau_conn',
        python_callable=initialize_tableau_conn()
    )

    print_hello_world = BashOperator(
        task_id='print_hello_world',
        bash_command="echo 'Hello there, you little world, you'"
    )

    end_hello_world = BashOperator(
        task_id='end_hello_world',
        bash_command="echo 'ENDING HELLO WORLD SAMPLE'"
    )

    # trigger_next = TriggerDagRunOperator(
    #     task_id='start_scorecard_subscriptions',
    #     trigger_dag_id='tableau_subscription_exam