FROM apache/airflow:2.5.0
COPY ./airflow.cfg /opt/airflow/airflow.cfg
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY requirements-catalogo-dados.txt /
RUN pip install --no-cache-dir -r /requirements-catalogo-dados.txt

USER root
RUN apt update \
  && apt install -y procps \
  && apt-get update \
  && apt-get install -y default-jdk \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

