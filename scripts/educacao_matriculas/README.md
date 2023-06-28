# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Microdados Educação - Matrículas
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre quantidade, sexo, raça, modalidade, aprovação, reprovação, distorção idade-série e abandono dos alunos da Rede Municipal.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Microdados da Rede Municipal de Educação - Matrículas](http://dados.prefeitura.sp.gov.br/dataset/microdados-matriculas) o qual lista a base de dados com informações sobre o perfil e a situação escolar de cada um dos estudantes da Rede Municipal.

Os arquivos inseridos na base se referem a conjuntos de anos e são de formato .zip e, quando extraídos, resultam em arquivos .csv para cada um dos anos daquele conjunto. A temporalidade dos conjuntos é variada (por exemplo, há arquivo de 2000 a 2005, mas também de 2006 a 2008, ou de 2015 a 2018, ou seja, três amplitudes temporais diferentes).

Sem que haja uma padronização clara sobre a frequência de atualização, são inseridas bases como de [2019-2021](http://dados.prefeitura.sp.gov.br/dataset/8b89fbee-63f2-4084-bfac-58687ea351d0/resource/1cd547cf-0c4c-4bcf-a14f-7292041e6e27/download/micmatv2019-2021.rar), que contém os arquivos referentes a 2019, 2020 e 2021, e deve ser empregada para a automação.

Até o momento de produção deste documento, o arquivo referente a 2021 estava disponibilizado como .txt.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0008, V0009, V0010, V0033, V0034, V0035, V0036, V0042, V0050, V0054, V0081, V0085, V0087, V0088, V0090, V0091, V0095, V0097, V0604 e V0607) formatada no template de importação do Intranet do ObservaSampa, sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de cada ano.

## Descrição do processo

### Para a variável V0008 (Alunos da rede municipal - sexo feminino):
1. Para cada ano, baixar o arquivo do Portal de Dados Abertos da PMSP que contenha aquele ano, no formato "Microdados de Matrículas - {Ano}/{Ano}". Por exemplo, para 2020, o arquivo [2019-2021](http://dados.prefeitura.sp.gov.br/dataset/8b89fbee-63f2-4084-bfac-58687ea351d0/resource/1cd547cf-0c4c-4bcf-a14f-7292041e6e27/download/micmatv2019-2021.rar);
2. Extrair o arquivo baixado;
3. Na pasta da extração, utilizar o arquivo referente ao ano que se deseja, no formato "Microdados_EOL_Matriculas_Ano_{Ano}". Por exemplo, para 2020, "Microdados_EOL_Matriculas_Ano_2020";
4. Filtrar as alunas de sexo feminino (código "F") na coluna "CD_SEXO";
5. Para o total do Município, contar o número de linhas;
6. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
7. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
8. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0009 (Alunos da rede municipal de ensino):
1. No mesmo arquivo referente ao ano, para o total do Município, contar o número de linhas;
2. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
3. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
4. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0010 (Alunos da rede municipal - sexo masculino):
1. No mesmo arquivo referente ao ano, filtrar os alunos de sexo masculino (código "M") na coluna "CD_SEXO";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0033 (Alunos da rede municipal de ensino - raça/cor amarela):
1. No mesmo arquivo referente ao ano, filtrar os alunos de raça/cor amarela (código "4") na coluna "CD_RACA_COR";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0034 (Alunos da rede municipal de ensino - raça/cor branca):
1. No mesmo arquivo referente ao ano, filtrar os alunos de raça/cor branca (código "1") na coluna "CD_RACA_COR";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0035 (Alunos da rede municipal de ensino - raça/cor indígena):
1. No mesmo arquivo referente ao ano, filtrar os alunos de raça/cor indígena (código "5") na coluna "CD_RACA_COR";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0036 (Alunos da rede municipal de ensino - raça/cor parda):
1. No mesmo arquivo referente ao ano, filtrar os alunos de raça/cor parda (código "3") na coluna "CD_RACA_COR";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0042 (Alunos da rede municipal de ensino - raça/cor preta):
1. No mesmo arquivo referente ao ano, filtrar os alunos de raça/cor preta (código "2") na coluna "CD_RACA_COR";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0050 (Matrículas nas creches da rede municipal de ensino):
1. No mesmo arquivo referente ao ano, filtrar os alunos matriculados em creches (código "CRECHE") na coluna "MODALIDADE";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0054 (Matrículas na Pré-Escola da rede municipal de ensino):
1. No mesmo arquivo referente ao ano, filtrar os alunos matriculados em pré-escolas (código "PRE") na coluna "MODALIDADE";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0081 (Alunos do Ensino Fundamental da rede municipal de ensino matriculados com idade acima da recomendada para a série (idade recomendada +2)):
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para o 1º Ano do Ensino Fundamental, filtrar o códigos "110" na coluna "CD_SERIE";
3. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 8 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 6 anos para a série é igual ou superior a 2 anos);
4. Contar o número de linhas resultantes, que será igual ao número total de alunos do 1º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
5. Para o 2º Ano do Ensino Fundamental, filtrar o códigos "111" na coluna "CD_SERIE";
6. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 9 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 7 anos para a série é igual ou superior a 2 anos);
7. Contar o número de linhas resultantes, que será igual ao número total de alunos do 2º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
8. Para o 3º Ano do Ensino Fundamental, filtrar o códigos "112" na coluna "CD_SERIE";
9. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 10 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 8 anos para a série é igual ou superior a 2 anos);
10. Contar o número de linhas resultantes, que será igual ao número total de alunos do 3º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
11. Para o 4º Ano do Ensino Fundamental, filtrar o códigos "116" na coluna "CD_SERIE";
12. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 11 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 9 anos para a série é igual ou superior a 2 anos);
13. Contar o número de linhas resultantes, que será igual ao número total de alunos do 4º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
14. Para o 5º Ano do Ensino Fundamental, filtrar o códigos "117" na coluna "CD_SERIE";
15. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 12 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 10 anos para a série é igual ou superior a 2 anos);
16. Contar o número de linhas resultantes, que será igual ao número total de alunos do 5º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
17. Para o 6º Ano do Ensino Fundamental, filtrar o códigos "115" na coluna "CD_SERIE";
18. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 13 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 11 anos para a série é igual ou superior a 2 anos);
19. Contar o número de linhas resultantes, que será igual ao número total de alunos do 6º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
20. Para o 7º Ano do Ensino Fundamental, filtrar o códigos "118" na coluna "CD_SERIE";
21. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 14 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 12 anos para a série é igual ou superior a 2 anos);
22. Contar o número de linhas resultantes, que será igual ao número total de alunos do 7º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
23. Para o 8º Ano do Ensino Fundamental, filtrar o códigos "119" na coluna "CD_SERIE";
24. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 15 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 13 anos para a série é igual ou superior a 2 anos);
25. Contar o número de linhas resultantes, que será igual ao número total de alunos do 8º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
26. Para o 9º Ano do Ensino Fundamental, filtrar o códigos "120" na coluna "CD_SERIE";
27. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 16 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 14 anos para a série é igual ou superior a 2 anos);
28. Contar o número de linhas resultantes, que será igual ao número total de alunos do 9º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
29. Para o total do Município, somar os valores das contagens de alunos em situação de Distorção Idade-Série do 1º ao 9º ano do Ensino Fundamental;
30. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
31. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
32. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0085 (Alunos do Ensino Médio da rede municipal de ensino matriculados com idade acima da recomendada (idade recomendada+2) para a série): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Médio (de código "MEDIO") na coluna "MODALIDADE";
2. Para o 1º Ano do Ensino Médio, filtrar os códigos "351" e "385" (referentes ao 1º ano do Ensino Médio, nos turnos manhã e noite, respectivamente) na coluna "CD_SERIE";
3. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 17 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 15 anos para a série é igual ou superior a 2 anos);
4. Contar o número de linhas resultantes, que será igual ao número total de alunos do 1º Ano do Ensino Médio em situação de Distorção Idade-Série;
5. Para o 2º Ano do Ensino Médio, filtrar os códigos "352" e "386" (referentes ao 2º ano do Ensino Médio, nos turnos manhã e noite, respectivamente) na coluna "CD_SERIE";
6. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 18 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 16 anos para a série é igual ou superior a 2 anos);
7. Contar o número de linhas resultantes, que será igual ao número total de alunos do 2º Ano do Ensino Médio em situação de Distorção Idade-Série;
8. Para o 3º Ano do Ensino Médio, filtrar os códigos "353" e "387" (referentes ao 3º ano do Ensino Médio, nos turnos manhã e noite, respectivamente) na coluna "CD_SERIE";
9. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 19 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 17 anos para a série é igual ou superior a 2 anos);
10. Contar o número de linhas resultantes, que será igual ao número total de alunos do 3º Ano do Ensino Médio em situação de Distorção Idade-Série;
11. Para o total do Município, somar os valores das contagens de alunos em situação de Distorção Idade-Série no 1º ano, no 2º ano e no 3º ano do Ensino Médio;
12. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
13. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
14. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0087 (Soma de alunos aprovados, reprovados e que abandonaram a escola no Ensino Fundamental na rede municipal): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para os alunos aprovados, filtrar "1" na coluna "SIT_AL_APROV" e contar o número de linhas;
3. Para os alunos reprovados, filtrar "1" na coluna "SIT_AL_REPROV" e contar o número de linhas;
4. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_ABAND" e contar o número de linhas;
5. Para o total do Município, somar os valores das contagens de alunos aprovados, alunos reprovados e alunos que abandonaram a escola;
6. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
7. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
8. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0088 (Total de alunos do Ensino Fundamental da rede municipal que abandonaram a escola): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_ABAND" e contar o número de linhas;
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0090 (Alunos do Ensino Médio da rede municipal que abandonaram a escola): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Médio (de código "MEDIO") na coluna "MODALIDADE";
2. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_ABAND" e contar o número de linhas;
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0091 (Soma de alunos aprovados, reprovados e que abandonaram a escola no Ensino Médio na rede municipal): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Médio (de código "MEDIO") na coluna "MODALIDADE";
2. Para os alunos aprovados, filtrar "1" na coluna "SIT_AL_APROV" e contar o número de linhas;
3. Para os alunos reprovados, filtrar "1" na coluna "SIT_AL_REPROV" e contar o número de linhas;
4. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_ABAND" e contar o número de linhas;
5. Para o total do Município, somar os valores das contagens de alunos aprovados, alunos reprovados e alunos que abandonaram a escola;
6. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
7. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
8. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0095 (Alunos do Ensino Fundamental da rede municipal reprovados): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_REPROV" e contar o número de linhas;
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0097 (Alunos do Ensino Médio da rede municipal de ensino reprovados): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Médio (de código "MEDIO") na coluna "MODALIDADE";
2. Para os alunos que abandonaram a escola, filtrar "1" na coluna "SIT_AL_REPROV" e contar o número de linhas;
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0604 (Alunos do Ensino Fundamental da rede municipal de ensino matriculados nas séries iniciais com idade acima da recomendada para a série (idade recomendada +2)): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para o 1º Ano do Ensino Fundamental, filtrar o códigos "110" na coluna "CD_SERIE";
3. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 8 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 6 anos para a série é igual ou superior a 2 anos);
4. Contar o número de linhas resultantes, que será igual ao número total de alunos do 1º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
5. Para o 2º Ano do Ensino Fundamental, filtrar o códigos "111" na coluna "CD_SERIE";
6. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 9 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 7 anos para a série é igual ou superior a 2 anos);
7. Contar o número de linhas resultantes, que será igual ao número total de alunos do 2º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
8. Para o 3º Ano do Ensino Fundamental, filtrar o códigos "112" na coluna "CD_SERIE";
9. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 10 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 8 anos para a série é igual ou superior a 2 anos);
10. Contar o número de linhas resultantes, que será igual ao número total de alunos do 3º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
11. Para o 4º Ano do Ensino Fundamental, filtrar o códigos "116" na coluna "CD_SERIE";
12. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 11 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 9 anos para a série é igual ou superior a 2 anos);
13. Contar o número de linhas resultantes, que será igual ao número total de alunos do 4º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
14. Para o 5º Ano do Ensino Fundamental, filtrar o códigos "117" na coluna "CD_SERIE";
15. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 12 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 10 anos para a série é igual ou superior a 2 anos);
16. Contar o número de linhas resultantes, que será igual ao número total de alunos do 5º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
17. Para o total do Município, somar os valores das contagens de alunos em situação de Distorção Idade-Série do 1º ao 5º ano do Ensino Fundamental;
18. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
19. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
20. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0607 (Alunos do Ensino Fundamental da rede municipal de ensino matriculados nas séries finais com idade acima da recomendada para a série (idade recomendada +2)): 
1. No mesmo arquivo referente ao ano, filtrar os alunos do Ensino Fundamental (de código "FUND") na coluna "MODALIDADE";
2. Para o 6º Ano do Ensino Fundamental, filtrar o códigos "115" na coluna "CD_SERIE";
3. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 13 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 11 anos para a série é igual ou superior a 2 anos);
4. Contar o número de linhas resultantes, que será igual ao número total de alunos do 6º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
5. Para o 7º Ano do Ensino Fundamental, filtrar o códigos "118" na coluna "CD_SERIE";
6. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 14 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 12 anos para a série é igual ou superior a 2 anos);
7. Contar o número de linhas resultantes, que será igual ao número total de alunos do 7º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
8. Para o 8º Ano do Ensino Fundamental, filtrar o códigos "119" na coluna "CD_SERIE";
9. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 15 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 13 anos para a série é igual ou superior a 2 anos);
10. Contar o número de linhas resultantes, que será igual ao número total de alunos do 8º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
11. Para o 9º Ano do Ensino Fundamental, filtrar o códigos "120" na coluna "CD_SERIE";
12. Na coluna "IDADE_ALUNO_MAR", filtrar as linhas que tenham valor igual ou superior a 16 anos (ou seja, os valores em que a diferença da idade do aluno para a idade ideal de 14 anos para a série é igual ou superior a 2 anos);
13. Contar o número de linhas resultantes, que será igual ao número total de alunos do 9º Ano do Ensino Fundamental em situação de Distorção Idade-Série;
14. Para o total do Município, somar os valores das contagens de alunos em situação de Distorção Idade-Série do 6º ao 9º ano do Ensino Fundamental;
15. Para os resultados em nível de Distrito, realizar as etapas de contagem com o filtro pelo nome de cada um dos distritos na coluna "NOME_DISTRITO" e, depois, somar os resultados;
16. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
17. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas para V0008, um para V0009, um para V0010, um para V0033, um para V0034, um para V0035, um para V0036, um para V0042, um para V0050, um para V0054, um para V0081, um para V0085, um para V0087, um para V0088, um para V0090, um para V0091, um para V0095, um para V0097, um para V0604 e outro para V0607 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022 para o arquivo de origem dezembro/2022. Preencher as linhas de valores de acordo com o resultado obtido na coleta dos valores das linhas indicadas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
