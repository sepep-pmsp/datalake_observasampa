# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Extensão de ciclovias
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre Ciclovias.

## Fontes
O [Mapa Digital da Cidade de São Paulo - Geosampa] e Os [Dados ABertos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/) possuem em seus repositórios o conjunto de dados [Ciclovias](http://dados.prefeitura.sp.gov.br/dataset/ciclovias) o qual possui arquivo com base de dados e shapefile das estruturas cicloviárias implantadas pela Prefeitura de São Paulo.

Anualmente o mapeamento é feito pela Companhia de Engenharia de Tráfego - CET. A cada ano (anualmente) deve-se verificar se houve atualização no dado e, havendo, esta base deve ser atualizada no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0635 e V0577) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de estoque da rede cicloviária implantada na cidade.

## Descrição do processo

### Para a variável V0635 (Extensão em quilômetros de ciclovias, ciclofaixas e ciclorrotas): 
1. Baixar o arquivo do Geosampa (http://mapas.geosampa.prodam/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=04_Transporte%5C%5CRede%20Cicloviaria%5C%5CShapefile%5C%5CSIRGAS_SHP_redecicloviaria&arqTipo=Shapefile) ou dos Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/706fcad5-9dd6-4174-81d2-c2c2294b8d2a/resource/40513683-d5ae-4626-a060-4f22ce2b29b0/download/ciclovias.zip); 
2. Realizar unzip;
3. Abrir arquivo e separar a coluna "Descriptio" de modo a obter os valores de extensão;
4. Somar os valroes de extensão por ano (<= [ano]) e inserir em nova tabela nas colunas "[ano]", "variavel" (com o código da variável) e coluna "região" (com o código do ObservaSamapa para o município);
[*verificar possibilidade de o indicador apresentar dados regionalizados por distrito e subprefeitura]

### Para a variável V0577 (Média anual de extensão de infraestrutura cicloviária): 
1. Baixar o arquivo do Geosampa (http://mapas.geosampa.prodam/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=04_Transporte%5C%5CRede%20Cicloviaria%5C%5CShapefile%5C%5CSIRGAS_SHP_redecicloviaria&arqTipo=Shapefile) ou dos Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/706fcad5-9dd6-4174-81d2-c2c2294b8d2a/resource/40513683-d5ae-4626-a060-4f22ce2b29b0/download/ciclovias.zip); 
2. Realizar unzip;
3. Abrir arquivo e separar a coluna "Descriptio" de modo a obter os valores de extensão;
4. Somar os valroes de extensão por ano (<= [ano]); 
5. Duplicar o dataframe ou Baixar variáveis do DadosAbertos do ObservaSampa (https://dados-abertos-observasampa.prefeitura.sp.gov.br/_temp/DadosAbertos/ObservaSampaDadosAbertosVariaveisCSV.csv)
6. Filtrar a variável "V0635-Extensão em quilômetros de ciclovias, ciclofaixas e ciclorrotas)" e colher o valor do ano imediatamente anterior ao ano de interesse;
7. Subtrair o valor do processo 4 com o valor do processo 6 (ex.: para calcular o valor de 2021 subtrair a extensão de 2021 por 2020); 
8. Inserir o resultado em nova tabela na colunas "[ano]" (referente ao ano anterior ao da raspagem do dado, ex: 2022 (2023-1)), "variavel" (com o código da variável) e coluna "região" (com o código do ObservaSamapa para o município); 
[*verificar possibilidade de o indicador apresentar dados regionalizados por distrito e subprefeitura]


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o valor do ano. Preencher as linhas de valores de acordo com os valores para ciclovias (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
