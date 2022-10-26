from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

dag = DAG("example", start_date=days_ago(0, 0, 0, 0, 0))

operation = BashOperator(
    task_id="op1",
    bash_command="pwd",
    dag=dag,
)

operation2 = BashOperator(
    task_id="op2",
    bash_command="sleep 5",
    dag=dag,
)

operation3 = BashOperator(
    task_id="op3",
    bash_command="sleep 20",
    dag=dag,
)

operation4 = BashOperator(
    task_id="op4",
    bash_command="echo 'ok'",
    dag=dag,
)

operation2 >> [operation, operation3] >> operation4
