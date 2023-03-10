# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Área do Município
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores baseados na área do Município.

## Fontes
O [GeoSampa](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx#) possui em seu repositório o conjunto de dados [Limites Administrativos/distritos](https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=01_Limites%20Administrativos%5C%5CDistrito%5C%5CShapefile%5C%5CSIRGAS_SHP_distrito&arqTipo=Shapefile) o qual possui arquivo shapefile com os dados da área de cada distritos.

Estes daods não necessitam atualização períodica, uma vez que a área do município não tende a mudar com frequência. Todavia, recomenda-se que a cada ano (anualmente) insira os dados do ano anterior para ganrantir as operaç~eos anuais de cada indicador.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0261 e V0416) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de área do município e regiões administrativas.

## Descrição do processo

### Para a variável V0416 (Área do município (Km²)): 
1. Baixar o arquivo shapefile da base Limite Adminsitrativo dos Distritos do GeoSampa (https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/downloadIfr.aspx?orig=DownloadCamadas&arq=01_Limites%20Administrativos%5C%5CDistrito%5C%5CShapefile%5C%5CSIRGAS_SHP_distrito&arqTipo=Shapefile); 
2. Remover o zip da pasta "SIRGAS_SHP_distrito" e ler o arquivo "SIRGAS_SHP_distrito\\SIRGAS_SHP_distrito.shp";
3. Criar coluna "regiao" e inserir o código do observa para cada distrito correspondente ao nome descrito na coluna "ds_nome";
4. Para cada Subprefeitura desccirta na coluna "ds_subpref" somar os valores de "ds_areakm"; 
5. Incluir código da regiao do observa para cada Subprefeitura;
6. Somar valoresda coluna "ds_areakm" para distritos ou Subprefeitura de modo a obter o valor da área para o Município. Inserir código da região "M00";
7. Concatenar os resultados em dataframe com a coluna região e uma coluna [ano] de interesse a partir dos valores da coluna "ds_areakm";
8. Inserir na primeira posição o código da variável "V0416".

### Para a variável V0261 (Área do município (m²)): 
A partir do processo utilizado para a variável acima, incluir uma última trasnformação: 

9. Dividir a coluna [ano] por 1000000 (um milhão), a fim de trasnformar o dado em m²; 
10. Alterar o código da variável.


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região do ObservaSampa, referente ao município, às Subprefeituras e aos Distritos de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o ano. Preencher as linhas de valores de área (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
