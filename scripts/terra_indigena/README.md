# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Terra Indígena
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre Terra Indígena.

## Fontes
O [GeoSampa](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx#) possui em seu repositório o conjunto de dados [Legislação Urbana / Terras Indígenas](http://mapas.geosampa.prodam/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=13_Legisla%E7%E3o%20Urbana%5C%5CTerras%20Ind%EDgenas%5C%5CShapefile%5C%5CSIRGAS_SHP_terraindigena&arqTipo=Shapefile) o qual possui arquivos shapefile com os dados sobre as Terras Indígenas.

Não existe previsão de periodicidade de atualização deste dado. Por isso, deve entrar no ciclo de automação anualmente para verificar se houve alteração.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0415) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente ou sempre que houver alteração na área das Terras Indígenas.

## Descrição do processo

### Para a variável V0415 (Terras indígenas): 
1. Baixar o arquivo shapefile da base do Terras Indígenas do GeoSampa (http://mapas.geosampa.prodam/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=13_Legisla%E7%E3o%20Urbana%5C%5CTerras%20Ind%EDgenas%5C%5CShapefile%5C%5CSIRGAS_SHP_terraindigena&arqTipo=Shapefile) que possui o arquivo shapefile "SIRGAS_SHP_terraindigena" referente às Terras indígenas no município; 
2. Remover o zip de cada pasta "SIRGAS_SHP_terraindigena\SIRGAS_SHP_terraindigena" e ler o arquivo "SIRGAS_SHP_terraindigena.shp";
3. Remover duplicatas e somar valores da coluna "ti_area";
4. Divir o valor total por 1e+6 (um milhão) para trasnformar o valor em km²;
5. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total em km² calculado anteriormente.


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos da variável | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o [ano]. Preencher as linhas de valores com a área das Terras indígenas (ver descrição do processo acima) | Decimal | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
