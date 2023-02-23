FROM apache/airflow:2.5.0
USER airflow
RUN pip install $_PIP_ADDITIONAL_REQUIREMENTS
COPY ./airflow.cfg /opt/airflow/airflow.cfg