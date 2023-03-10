# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Parques urbnos e lineares
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre parques urbanos e lineares.

## Fontes
O [GeoSampa](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx#) possui em seu repositório o conjunto de dados [Verde/Recursos Naturais/Parques Municipais ]https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=09_Verde%20e%20Recursos%20Naturais%5C%5CParques%20Municipais%5C%5CShapefile%5C%5CSIRGAS_SHP_parquemunicipal&arqTipo=Shapefile) o qual possui arquivo shapefile com os dados sobre os parques urbanos e lineares.

Não existe previsão de periodicidade de atualização deste dado. Por isso, deve entrar no ciclo de automação, a cada ano (anualmente), a inserção dos dados em referência ao ano anterior.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0726 e V0734) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações dos dados de parques.

## Descrição do processo

### Para a variável V0726 (Número de parques existentes no município): 
1. Baixar o arquivo shapefile da base de Parques Municipais do GeoSampa (https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=09_Verde%20e%20Recursos%20Naturais%5C%5CParques%20Municipais%5C%5CShapefile%5C%5CSIRGAS_SHP_parquemunicipal&arqTipo=Shapefile) o qual possui arquivo shapefile); 
2. Remover o zip da pasta "SIRGAS_SHP_parquemunicipal.shp" e ler o arquivo "SIRGAS_SHP_parquemunicipal/SIRGAS_SHP_parquemunicipal.shp";
3. Selecionar as colunas "pq_area", "pq_nome" e "pq_PrefReg"e remover duplicatas da coluan "pq_nome";
4. Contar observações e, em novo dataframe, dar a este valor o [ano] de interesse e incluir coluna "região" com o Código "M000", em refrência ao dado municipal de parques.
5. Repetir o passo acima para subprefeituras, isto é, para cada subprefeitura apresentada na coluna "pq_PrefReg", contar o número de parques e associar ao [ano] e ao código do Observasampa para subprefeituras no dataframe criado anteriormetne;
6. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida das coluans de regiao e [ano].

### Para a variavel V0734 (Área total de parques urbanos e lineares existentes): 
1. Baixar o arquivo shapefile da base de Parques Municipais do GeoSampa (https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=09_Verde%20e%20Recursos%20Naturais%5C%5CParques%20Municipais%5C%5CShapefile%5C%5CSIRGAS_SHP_parquemunicipal&arqTipo=Shapefile) o qual possui arquivo shapefile); 
2. Remover o zip da pasta "SIRGAS_SHP_parquemunicipal.shp" e ler o arquivo "SIRGAS_SHP_parquemunicipal/SIRGAS_SHP_parquemunicipal.shp";
3. Selecionar as colunas "pq_area", "pq_nome" e "pq_PrefReg"e remover duplicatas da coluan "pq_nome";
4. Transformar a coluna "pq_area" em numeric;
5. Somar coluna "pq_area" e, em novo dataframe, dar a este valor o [ano] de interesse e incluir coluna "região" com o Código "M000", em refrência ao dado de área em m² dos parques municipais;
6. Repetir o passo acima para cada subprefeitura (coluna "pq_PrefReg") e inserir os códigos de subprefeituras do ObservaSampa na "região";
7. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida das coluans de regiao e [ano].

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o ano. Preencher as linhas de valores sobre número e área dos parques (ver descrição do processo acima) | Inteiro e decimal | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
