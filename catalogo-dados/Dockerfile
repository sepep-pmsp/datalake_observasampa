FROM python:3

COPY requirements-catalogo-dados.txt /
RUN pip install --no-cache-dir -r /requirements-catalogo-dados.txt

COPY setup.py /
COPY requirements-dev.txt /
RUN python3 setup.py install
