# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Cobertura Vegetal de 2020
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre a Cobertura Vegetal.

## Fontes
O [GeoSampa](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx#) possui em seu repositório o conjunto de dados [Verde e Recursos Naturais/ Mapeamento Vegetação 2020](http://mapas.geosampa.prodam/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=09_Verde%20e%20Recursos%20Naturais%5C%5CMapeamento_Vegetacao_2020%5C%5CShapefile) o qual possui arquivos shapefile com os dados sobre a Cobertura Vegetal.

Não existe previsão de periodicidade de atualização deste dado. Por isso, deve entrar no ciclo de automação sempre que houver um novo mapeamento.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0260) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo apenas uma vez para cada base nova sobre a Cobertura Vegetal.

## Descrição do processo

### Para a variável V0260 (Cobertura Vegetal (m²)): 
1. Baixar os arquivos shapefiles da base do Mapeamento da Vegetação 2020 do GeoSampa ("https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=09_Verde%20e%20Recursos%20Naturais%5C%5CMapeamento_Vegetacao_2020%5C%5CShapefile%5C%5CSIRGAS_SHP_vegetacao_pmd_[NOME DA SUBPREFEITURA]&arqTipo=Shapefile") os quaais possuem arquivos shapefile referente a cada subprefeura; 
2. Remover o zip de cada pasta "SIRGAS_SHP_vegetacao_pmd_[NOME DA SUBPREFEITURA].shp" e ler o arquivo "SIRGAS_SHP_vegetacao_pmd_[NOME DA SUBPREFEITURA].shp";
3. Transformar em numeric a coluna "qt_area" e somar os valores para cada SUBPREFEITURA;
4. Concatenar em dataframe o valora da área (e nomear a coluna como 2020) e incluir coluna "região" com o Código do ObservaSampa de cada SUBPREFEITURA; 
5. Somar os valores de "qt_area" e atribuir na coluna regiao o código "M000", em refrência ao dado de cobertura do município.
6. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida das coluans "regiao" e "2020".


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente às subprefeuras e ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o ano "2020". Preencher as linhas de valores com a área da Cobertura Vegetal (ver descrição do processo acima) | Decimal | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
