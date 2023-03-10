# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Estimaivas da população do município de São Paulo
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre População.

## Fontes
A [Fundação SEADE](https://repositorio.seade.gov.br/) possui em seu repositório um conjunto de dados [População do Município de São Paulo por distritos, sexo e idade](https://repositorio.seade.gov.br/dataset/populacao-do-municipio-de-sao-paulo-por-sexo-e-idade) o qual possui colunas com o código do distrito, nome do distrito, ano, sexo, faixa etária e população (projeção da população residente).

Anualmente é inserida a projeção populacional realizada pela Fundação. Portanto, anualmente esta base deve ser atualizada no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0001, V0019, V0046, V0073, V0079, V0084, V0249, V0340, V0341, V0723) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de cada ano.

## Descrição do processo

### Para a variável V0001 (População total): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
3. Padronizar o nome do distrito (coluna B "distrito"); 
4. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
5. Excluir a coluna A "cod_distrito" da SEADE; 
6. Para todo [ano] e nome de distrito igual, somar os valores de "população" e excluir as colunas "sexo" e "faixa etária"; 
7. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
8. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
9. Excluir a coluna "distrito"; 
10. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0019 (Metade (50%) da população feminina - 50 a 69 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "sexo"=="Mulheres" e a coluna "faixa_etaria"=="50 a 54" & "55 a 59" & "60 a 64" & "65 a 69" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Dividir o novo valor da coluna "populacao" por 2;
4. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
5. Padronizar o nome do distrito (coluna B "distrito"); 
6. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
7. Excluir a coluna A "cod_distrito" da SEADE; 
8. Excluir as colunas "sexo" e "faixa etária"; 
9. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
10. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
11. Excluir a coluna "distrito"; 
12. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0046 (População de 30 a 69 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "faixa_etaria"=="30 a 34" & "35 a 39" & "40 a 44" & "45 a 49" & "50 a 54" & "55 a 59" & "60 a 64" & "65 a 69" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0073 (População com mais de 15 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "faixa_etaria"=!"00 a 04" & "05 a 09" & "10 a 14" (ou seja, exclui-se as categorias expressas na fórmula, mantendo todo o restante, obtendo o efeito de >=15) e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0079 (População com idade igual ou superior a 60 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "faixa_etaria"=="60 a 64" & "65 a 69" & "70 a 74" & "75 e +" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0084 (Um terço (1/3) da população feminina com idade entre 25 a 64 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "sexo"=="Mulheres" e a coluna "faixa_etaria"== "25 a 29" & "30 a 34" & "35 a 39" & "40 a 44" & "45 a 49" & "50 a 54" & "55 a 59" & "60 a 64" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Dividir o novo valor da coluna "populacao" por 3; 
4. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
5. Padronizar o nome do distrito (coluna B "distrito"); 
6. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
7. Excluir a coluna A "cod_distrito" da SEADE; 
8. Excluir as colunas "sexo" e "faixa etária"; 
9. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
10. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
11. Excluir a coluna "distrito"; 
12. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0249 (População total - feminina): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "sexo"=="Mulheres" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0340 (População total - masculina): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "sexo"=="Homens" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 

### Para a variável V0341 (População menor até 14 anos): 
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "faixa_etaria"=="00 a 04" & "05 a 09" & "10 a 14" e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; 
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 


### Para a variável V0723 (População em idade ativa): **[COMPROMETIDO, SEADE NÃO TEM BASE ATIVA PARA ISSO, deveria ser >=14]**
1. Baixar o arquivo REFERENTE AO ANO DE INTERSSE (para cada ano existe uma base, exceto quando termina em 0 ou 5, quando se compartilha a mesma base de projeção) do Repositório SEADE (exemplo: https://repositorio.seade.gov.br/dataset/09975945-64f1-48cc-9f4d-72f11ddd5e6f/resource/f3e6f400-668a-43bb-92ac-fe5ad51fd44a/download/populacaomsp_2022_sexo_idade.csv); 
2. Filtrar a coluna "faixa_etaria"=!"00 a 04" & "05 a 09" & "10 a 14" (ou seja, exclui-se as categorias expressas na fórmula, mantendo todo o restante, obtendo o efeito de >=15) e somar valores da coluna "populacao" para cada valor em "ano" e "distrito"; **[resultado será idêntico à V0073]**
3. Pivotar o valor da coluna F "população", de cada "ano" (coluna C) - nos casos em que o ano terminar em 0 ou 5 -, para cada "distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Excluir as colunas "sexo" e "faixa etária"; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município (M00) na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "distrito"; 
11. Incluir coluna "variável" com o código da variável em todas as linhas. 


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o valor do ano, de acordo com o ano indicado originalmente na coluna C. Preencher as linhas de valores de acordo com os valores de número da população, originalmente na coluna F (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
