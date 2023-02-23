FROM apache/airflow:2.5.0
USER airflow
COPY ./airflow.cfg /opt/airflow/airflow.cfg