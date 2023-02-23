FROM apache/airflow:2.5.0
COPY ./airflow.cfg /opt/airflow/airflow.cfg
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt