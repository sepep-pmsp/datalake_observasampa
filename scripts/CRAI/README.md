# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** CRAI 
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre o Centro de Referência para o Atendimento do Imigrante (CRAI).

## Fontes
O [Dados ABertos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/) possui em seu repositório o conjunto de dados [Base de Dados e Dicionário - CRAI](http://dados.prefeitura.sp.gov.br/dataset/base-de-dados-do-centro-de-referencia-e-atendimento-para-imigrantes-crai) o qual possui arquivo com base de dados dos atendimentos no CRAI.

Anualmente os dados, publicados pela SMDHC, estão desatualizados no Portal. No entanto, o objetivo é que a cada ano (anualmente) adicion-se os dados do ano anterior, inserindo as atualizações no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0276 e V0584) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações dos dados do CRAI.

## Descrição do processo

### Para a variável V0276 (Pessoas atendidas pelo Centro de Referência e Atendimento ao Imigrante): 
1. Baixar a base de registros do CRAI do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/f31cf2a4-684a-453b-aca2-8e00455a8a48/resource/7eb866c0-02a3-4215-893d-d0b62a196c0c/download/bancocrai2014a2019---sistematizacao-geoinfo-atualizada.csv); 
2. Filtrar coluna "data_cadastro" para o [ano] de interesse;
3. Contar o núemro de observações e criar dataframe com o valor para o [ano] e a região "M00", indicando ser este o resultado para Municipio;
4. Inserir coluna variável com o código da variável.

### Para a variável V0584 (Número de atendimentos no Centro de Referência para atendimento ao imigrante para regularização migratória): 
1. Baixar a base de registros do CRAI do Portal Dados Abertos (http://dados.prefeitura.sp.gov.br/dataset/f31cf2a4-684a-453b-aca2-8e00455a8a48/resource/7eb866c0-02a3-4215-893d-d0b62a196c0c/download/bancocrai2014a2019---sistematizacao-geoinfo-atualizada.csv); 
2. Filtrar a coluna "demanda_1" para o valor "Regularização migratória" e a coluna "data_cadastro" para o [ano] de interesse;
3. Contar o núemro de observações e criar dataframe com o valor para o [ano] e a região "M00", indicando ser este o resultado para Municipio;
4. Inserir coluna variável com o código da variável.



## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o ano. Preencher as linhas de valores de acordo com o número de atendimentos no CRAI (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
