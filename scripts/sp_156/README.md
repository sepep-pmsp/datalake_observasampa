# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** SP156
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre os dados do SP156.

## Fontes
O [Dados ABertos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/) possui em seu repositório o conjunto de dados [Dado do SP156](http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156) o qual possui arquivo com base de dados das solicitações recebidas no SP156.

Anualmente a SMIT atualiza dados trimestrais. A cada ano (anualmente) deve-se concatenar os arquivos com dadso do ano anterior, inserindo as atualizações no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V2001, V0202, V0485 e V0486) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente (todo mês de fevereiro) com informações dos dados do SP156.

## Descrição do processo

### Para a variável V0201 (Total de solicitações do serviço 156): 
1. Baixar os arquivos trimestrais (ou mensais, quando for o caso) do ano de referência do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156); 
2. Concatenar as bases trimestrais ou mensais do ano de referência (exemplo, para 2021, concatenar as bases dos 4 trimestres: http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/dee8a960-805d-4c0b-aa69-62e8c4692eee/download/arquivofinal4tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/e63c9267-daf4-4395-be6c-d96dbad72b2a/download/arquivofinal3tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/ece6dc7c-6f1b-478d-afe9-71deb8117116/download/arquivofinal2tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d9c502f0-dcc1-4d2d-948a-0fc0520852cc/download/arquivofinal1tri2021.xlsx.csv );
3. Contar o núemro de observações e criar dataframe com o valor para o ano e a região "M00", indicando ser este o resultado para Municipio;
4. Criar tabela com número de observações para subprefeituras (coluna I);
5. Inserir valores com os códigos do ObservaSampa para subprefeituras no dataframe criado;
6. Inserir coluna variável com o código da variável.

### Para a variável V0202 (Total de solicitações do serviço 156 - acessibilidade): 
1. Baixar os arquivos trimestrais (ou mensais, quando for o caso) do ano de referência do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156); 
2. Concatenar as bases trimestrais ou mensais do ano de referência (exemplo, para 2021, concatenar as bases dos 4 trimestres: http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/dee8a960-805d-4c0b-aa69-62e8c4692eee/download/arquivofinal4tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/e63c9267-daf4-4395-be6c-d96dbad72b2a/download/arquivofinal3tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/ece6dc7c-6f1b-478d-afe9-71deb8117116/download/arquivofinal2tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d9c502f0-dcc1-4d2d-948a-0fc0520852cc/download/arquivofinal1tri2021.xlsx.csv );
3. Filtrar a coluna "Tema" (coluna C) para "Acessibilidade";
4. Contar o núemro de observações e criar dataframe com o valor para o ano e a região "M00", indicando ser este o resultado para Municipio;
5. Criar tabela com número de observações para subprefeituras (coluna I);
6. Inserir valores com os códigos do ObservaSampa para subprefeituras no dataframe criado;
5. Inserir coluna variável com o código da variável.


### Para a variável V0485 (Solicitações recebidas pelos serviços Alagamento e Inundação pela Central SP156): 
1. Baixar os arquivos trimestrais (ou mensais, quando for o caso) do ano de referência do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156); 
2. Concatenar as bases trimestrais ou mensais do ano de referência (exemplo, para 2021, concatenar as bases dos 4 trimestres: http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/dee8a960-805d-4c0b-aa69-62e8c4692eee/download/arquivofinal4tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/e63c9267-daf4-4395-be6c-d96dbad72b2a/download/arquivofinal3tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/ece6dc7c-6f1b-478d-afe9-71deb8117116/download/arquivofinal2tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d9c502f0-dcc1-4d2d-948a-0fc0520852cc/download/arquivofinal1tri2021.xlsx.csv );
3. Filtrar a coluna Serviço (coluna E) para os termos "Alagamento" e (&) "Inundação";
4. Contar o núemro de observações e criar dataframe com o valor para o ano e a região "M00", indicando ser este o resultado para Municipio;
5. Criar tabela com número de observações para subprefeituras (coluna I);
6. Inserir valores com os códigos do ObservaSampa para subprefeituras no dataframe criado;
5. Inserir coluna variável com o código da variável.

### Para a variável V0486 (Solicitações recebidas pelo serviço Limpeza da via pública após enchentes ou eventos pela central 156): 
1. Baixar os arquivos trimestrais (ou mensais, quando for o caso) do ano de referência do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156); 
2. Concatenar as bases trimestrais ou mensais do ano de referência (exemplo, para 2021, concatenar as bases dos 4 trimestres: http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/dee8a960-805d-4c0b-aa69-62e8c4692eee/download/arquivofinal4tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/e63c9267-daf4-4395-be6c-d96dbad72b2a/download/arquivofinal3tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/ece6dc7c-6f1b-478d-afe9-71deb8117116/download/arquivofinal2tri2021.xlsx.csv ; http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d9c502f0-dcc1-4d2d-948a-0fc0520852cc/download/arquivofinal1tri2021.xlsx.csv );
3. Filtrar a coluna Serviço (coluna E) para "Solicitar limpeza da via pública após enchentes ou eventos";
4. Contar o núemro de observações e criar dataframe com o valor para o ano e a região "M00", indicando ser este o resultado para Municipio;
5. Criar tabela com número de observações para subprefeituras (coluna I);
6. Inserir valores com os códigos do ObservaSampa para subprefeituras no dataframe criado;
5. Inserir coluna variável com o código da variável.


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o valor do ano. Preencher as linhas de valores de acordo com o número de solicitações recebidas no SP156 (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
