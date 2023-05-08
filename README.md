# SGM-ExtracoesObservaSampa

Repositório desenvolvido pelo time da Coordenadoria de Avaliação e Gestão da Informação da Secretaria Executiva de Planejamento e Entregas Prioritárias

## Variáveis de ambiente

Copiar o arquivo sample.env para .env e edita-lo

## Criar buckets e criar access key no Minio

### Alterar as chaves Minio:
s3a.access.key e s3a.secret.key nos arquivos core-site.xml e metastore-site.xml do diretório conf
s3.aws-access-key e s3.aws-secret-key no arquivo minio.properties do diretório etc/catalog

Iniciar o docker-compose-catalogo-dados:

### Criar os schemas no
CREATE SCHEMA minio.bronze
WITH (location = 's3a://bronze/');

CREATE SCHEMA minio.silver
WITH (location = 's3a://silver/');

CREATE SCHEMA minio.gold
WITH (location = 's3a://gold/');


## Notas 

### Criar conexão twitter
Connection Id = twitter_default
Connection Type = HTTP
Host = https://api.twitter.com
Extra = {"Authorization":"Bearer xyzxyzxyzxyz"}

### Criar conexão spark
Connection Id = spark_default
Connection Type = Spark
Host = local

### Excluir nó e seus relacionamentos no Neo4j
MATCH (t:Table) where ID(t) = 31 detach delete t return *

### Atualizar os nós do Trino para o Neo4j
Executar no container python:
python3 src/trino_data_loader.py
