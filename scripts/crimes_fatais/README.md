# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Crimes Fatais
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre crimes fatais (entendido por homicídios dolosos e lesão corporal seguida de morte) e correlatos.

## Fontes
O [SSP Transparência](http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx) possui em seu repositório os conjuntos de dados [HOMICÍDIO DOLOSO e LESÃO CORPORAL SEGUIDA DE MORTE) o qual possui a apresentação dos dados, podenso ser exportados para planilhas em xls.

Não existe previsão de periodicidade de atualização deste dado. Por isso, deve entrar no ciclo de automação anualmente para verificar se houve alteração.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0585, V0586, V0588, V0587 e V0252) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente, no primerio semestre, para oter os dados do ano anterior.

## Descrição do processo

### Para a variável V0585 (Crimes fatais): 
1. Acessar os dados de HOMICÍDIOS DOLOSOS em ("javascript:__doPostBack('ctl00$cphBody$btnHomicicio','')") que possui a apresentação tabular dos dados mensais de homicídios e o botão "Exportar" para baixar a tabela com estes dados em formato xls; 
2. Selecionar a aba com o [ano];
3. Filtrar coluna "Cidade" para "São Paulo"; 
4. Repetir o processo para cada [ano] e contar registros; 
5. Acessar os dados de LESÃO CORPORAL SEGUIDA DE MORTE ("javascript:__doPostBack('ctl00$cphBody$btnLesaoMorte','')") que baixa automaticamente uma planilha em xls; 
6. Para cada aba com o [ano], filtrar a coluna "MUNICIPIO_CIRCUNSCRICAO"=="São Paulo" e contar a quantidade de casos; 
7. Somar os dados de HOMICÍDIOS DOLOSOS com os de LESÃO CORPORAL SEGUIDA DE MORTE, para cada [ano];
8. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total de crimes fatais calculado anteriormente por ano.

### Para a variável V0586 (Crimes fatais - População Negra): 
1. Acessar os dados de HOMICÍDIOS DOLOSOS em ("javascript:__doPostBack('ctl00$cphBody$btnHomicicio','')") que possui a apresentação tabular dos dados mensais de homicídios e o botão "Exportar" para baixar a tabela com estes dados em formato xls; 
2. Filtrar coluna "Cidade" para "São Paulo";
3. Selecionar o [ano], filtrar coluna "COR_PELE" para "Preto" e "Pardo"; 
4. Contar registros e exportar os dados de cada [ano]; 
5. Acessar os dados de LESÃO CORPORAL SEGUIDA DE MORTE ("javascript:__doPostBack('ctl00$cphBody$btnLesaoMorte','')") que baixa automaticamente uma planilha em xls; 
6. Para cada aba com o [ano], filtrar a coluna "MUNICIPIO_CIRCUNSCRICAO"=="São Paulo", filtrar coluna "COR_PELE" para "Preto" e "Pardo" e contar a quantidade de casos; 
7. Somar os dados de HOMICÍDIOS DOLOSOS com os de LESÃO CORPORAL SEGUIDA DE MORTE para cada [ano];
8. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total de crimes fatais calculado anteriormente por ano.

### Para a variável V0587 (Crimes fatais - Mulheres): 
1. Acessar os dados de HOMICÍDIOS DOLOSOS em ("javascript:__doPostBack('ctl00$cphBody$btnHomicicio','')") que possui a apresentação tabular dos dados mensais de homicídios e o botão "Exportar" para baixar a tabela com estes dados em formato xls; 
2. Filtrar coluna "Cidade" para "São Paulo"; 
3. Selecionar o [ano], filtrar coluna "SEXO_PESSOA" para "Feminino"; 
4. Contar registros e exportar os dados de cada [ano]; 
5. Acessar os dados de LESÃO CORPORAL SEGUIDA DE MORTE ("javascript:__doPostBack('ctl00$cphBody$btnLesaoMorte','')") que baixa automaticamente uma planilha em xls; 
6. Para cada aba com o [ano], filtrar a coluna "MUNICIPIO_CIRCUNSCRICAO"=="São Paulo", filtrar coluna "SEXO_PESSOA" para "Feminino" e contar a quantidade de casos; 
7. Somar os dados de HOMICÍDIOS DOLOSOS com os de LESÃO CORPORAL SEGUIDA DE MORTE para cada [ano]; 
8. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total de crimes fatais calculado anteriormente por ano. 

### Para a variável V0588 (Número de homicídios de homens jovens): 
1. Acessar os dados de HOMICÍDIOS DOLOSOS em ("javascript:__doPostBack('ctl00$cphBody$btnHomicicio','')") que possui a apresentação tabular dos dados mensais de homicídios e o botão "Exportar" para baixar a tabela com estes dados em formato xls; 
2. Filtrar coluna "Cidade" para "São Paulo"; 
3. Selecionar o [ano], filtrar coluna "IDADE_PESSOA" para >=15 e <=29; 
4. Contar registros e exportar os dados de cada [ano]; 
5. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total calculado anteriormente por ano. 

### Para a variável V0252 (Registros de homicídios dolosos): 
1. Acessar os dados de HOMICÍDIOS DOLOSOS em ("javascript:__doPostBack('ctl00$cphBody$btnHomicicio','')") que possui a apresentação tabular dos dados mensais de homicídios e o botão "Exportar" para baixar a tabela com estes dados em formato xls; 
2. Filtrar coluna "Cidade" para "São Paulo"; 
3. Contar registros e exportar os dados de cada [ano]; 
4. Incluir, em primeira posição, coluna "variavel" com o código da variável, seguida da coluna "regiao", com o código do municpipio ("M00"), e da coluna [ano], com o valor total calculado anteriormente por ano. 



## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos da variável | String | N/A | N/A | N/A |
| Região | Preencher com o código da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o [ano]. Preencher as linhas de valores com os valores das variáveis (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
