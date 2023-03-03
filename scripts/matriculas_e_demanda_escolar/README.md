# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Matrículas e Demanda da Rede Municipal de Ensino
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores de matrículas e demanda da rede municipal de ensino.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Demanda Registrada e Matrículas - Educação Infantil, Fundamental e EJA](http://dados.prefeitura.sp.gov.br/dataset/demanda-e-matriculas) o qual lista a base de dados com informações sobre cadastro de demanda por vagas, matrículas e matrículas em processo em educação infantil, ensino fundamental e educação de jovens e adultos na Rede Municipal, por distritos e para o município.

Os valores trazidos pela base se referem à quantidade de alunos matriculados, em processo de matrícula ou aguardando vaga na rede municipal, ou seja, a base traz o estoque de cada um desses elementos no momento de  mensuração.

Em conformidade com o Decreto Municipal nº 47.155, de 30 de março de 2006, são contabilizados os alunos matriculados nas redes direta, indireta e conveniada.

Trimestralmente são inseridas bases como de [dezembro de 2022](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/45612acc-edd3-4134-ac7f-9a0026f60c97/resource/66dbab4e-9393-4726-bead-b40c8132c3bf/download/demanda-e-matricula-trimestraldezembro2022.xls), que deve ser empregada para a automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0015, V0021, V0023, V0025, V0048, V0055, V0605, V0608, V0702 e V0824) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações do mês de Dezembro de cada ano.

## Descrição do processo

### Para a variável V0015 (Matrículas - ensino fundamental rede municipal):
1. Para cada ano, baixar o arquivo de dezembro do conjunto de dados do Portal de Dados Abertos da PMSP, no formato "Demanda e Matrículas - Dez/{ANO}". Por exemplo, [(dezembro-2022)](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/45612acc-edd3-4134-ac7f-9a0026f60c97/resource/66dbab4e-9393-4726-bead-b40c8132c3bf/download/demanda-e-matricula-trimestraldezembro2022.xls);
2. Somar os valores das subcolunas "Ens. Fund.I" e "Ens. Fund.II", na coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0021 (Matrículas - creches rede municipal e conveniada): 
1. No mesmo arquivo de dezembro do último ano, selecionar os valores da subcoluna "Creche", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0023 (Matrículas - pré-escolas rede municipal e conveniada): 
1. No mesmo arquivo de dezembro do último ano, selecionar os valores da subcoluna "Pré Escola", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0025 (Matrículas - ensino médio rede municipal): 
1. No mesmo arquivo de dezembro do último ano, selecionar os valores da subcoluna "Ens. Médio", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0048 (Total da Demanda (atendida e não atendida) de Creche da rede municipal de ensino): 
1. No mesmo arquivo de dezembro do último ano, somar os valores da subcoluna "Creche", da coluna "Matrículas", com os valores da subcoluna "Creche Total", da coluna "Demanda";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0055 (Total da Demanda (atendida e não atendida) da Pré-escola da rede municipal de ensino): 
1. No mesmo arquivo de dezembro do último ano, somar os valores da subcoluna "Pré Escola", da coluna "Matrículas", com os valores da subcoluna "Pré Escola Total", da coluna "Demanda";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0605 (Matrículas na Rede Municipal do 1º ao 5º Ano): 
1. No mesmo arquivo de dezembro do último ano, selecionar os valores da subcoluna "Ens. Fund.I", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0608 (Matrículas na Rede Municipal do 6º ao 9º Ano): 
1. No mesmo arquivo de dezembro do último ano, selecionar os valores da subcoluna "Ens. Fund.II", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0702 (Número de Matrículas na Educação de Jovens e Adultos (EJA) - rede municipal): 
1. No mesmo arquivo de dezembro do último ano, somar os valores das subcolunas "EJA I" e "EJA II", da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0824 (Matrículas na Rede Municipal de Ensino): 
1. No mesmo arquivo de dezembro do último ano, somar os valores de todas as subcolunas ("Creche", "Pré Escola", "Ens. Fund.I", "Ens. Fund.II", "EJA I", "EJA II", "Ens. Médio" e "Ed. Prof."), da coluna "Matrículas";
3. Para o total do Município, selecionar os valores referentes à linha "TOTAL" (linha 99);
4. Para os resultados regionalizados, selecionar os valores das linhas correspondentes aos 96 distritos (linhas 3 a 98);
5. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas para V0015, um para V0021, um para V0023, um para V0025, um para V0048, um para V0055, um para V0605, um para V0608, um para V0702 e outro para V0824 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022 para o arquivo de origem dezembro/2022. Preencher as linhas de valores de acordo com o resultado obtido na coleta dos valores das linhas indicadas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
