# ObservaSampa: Automação de variáveis 
## Informações do processo
* **Processo:** Estimaivas da população em idade escolar do município de São Paulo
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre População.

## Fontes
A [Fundação SEADE](https://repositorio.seade.gov.br/) possui em seu repositório um conjunto de dados [População do Município de São Paulo por distrito e idade escolar](https://repositorio.seade.gov.br/dataset/populacao-do-municipio-de-sao-paulo-por-distrito-e-idade-escolar) o qual possui colunas com o código do distrito, nome do distrito, ano, sexo, faixa etária (colunas com diversos recortes), população total e Participação<17anos.

Anualmente a projeção populacional é realizada pela Fundação, com base no Censo e divulga dados quinquenais. Portanto, a cada censo (decenalmente) esta base deve ser atualizada no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0005, V0011, V0018, V0030, V0032, V0127) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo decenalmente (ou após cada Censo) com informações da expectativa de população para cada quinquênio.

## Descrição do processo

### Para a variável V0005 (População - 0 a 3 anos): 
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Excluir todas as colunas desde E à L (manter apenas de A a D);
3. Pivotar o valor da coluna D "De 00 a 03 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "Distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
8. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
9. Excluir a coluna "Distrito"; 
10. Incluir coluna "variavel" com o código da variável em todas as linhas. 

### Para a variável V0011 (População - 4 a 17 anos):
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Somar valores das colunas E, F, G e H (ou subtrair os valores da coluna J pela D) para obter os valores "de 4 a 17 anos";
3. Excluir todas as demais colunas (manter apenas de A a C e a coluna "de 4 a 17 anos" criada);
4. Pivotar o valor da coluna criada "de 4 a 17 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
5. Padronizar o nome do distrito (coluna B "Distrito"); 
6. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
7. Excluir a coluna A "cod_distrito" da SEADE; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "Distrito"; 
11. Incluir coluna "variavel" com o código da variável em todas as linhas. 

### Para a variável V0018 (População - 0 a 17 anos): 
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Excluir as colunas K e L e as colunas desde D à H (manter apenas de A a C e J);
3. Pivotar o valor da coluna J "Até 17 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "Distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
8. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
9. Excluir a coluna "Distrito"; 
10. Incluir coluna "variavel" com o código da variável em todas as linhas. 

### Para a variável V0030 (População - 6 a 14 anos):
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Somar valores das colunas F e G, para obter os valores "de 6 a 14 anos";
3. Excluir todas as demais colunas (manter apenas de A a C e a coluna "de 6 a 14 anos" criada);
4. Pivotar o valor da coluna criada "de 6 a 14 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
5. Padronizar o nome do distrito (coluna B "Distrito"); 
6. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
7. Excluir a coluna A "cod_distrito" da SEADE; 
8. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
9. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
10. Excluir a coluna "Distrito"; 
11. Incluir coluna "variavel" com o código da variável em todas as linhas. 

### Para a variável V0032 (População - 4 e 5 anos): 
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Excluir a coluna D e as colunas desde F à L (manter apenas de A a C e E);
3. Pivotar o valor da coluna E "De 04 a 05 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "Distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
8. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
9. Excluir a coluna "Distrito"; 
10. Incluir coluna "variavel" com o código da variável em todas as linhas. 

### Para a variável V0127 (População - 15 a 17 anos): 
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/7034fd9d-2bdd-4df9-8144-ececa0ef0707/resource/693c26ee-3da0-48d7-ac61-9c2bdc22264a/download/pop_idade_escolar_2000a2050_msp.csv); 
2. Excluir as colunas desde D à G e as colunas desde I à L (manter apenas de A a C e H);
3. Pivotar o valor da coluna H "De 15 a 17 anos", de cada "Ano" (coluna C), para cada "Distrito" (coluna B); 
4. Padronizar o nome do distrito (coluna B "Distrito"); 
5. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente; 
6. Excluir a coluna A "cod_distrito" da SEADE; 
7. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada [ano], bem como inserir o código do ObservaSamapa para o município na coluna "região"; 
8. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada [ano] e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
9. Excluir a coluna "Distrito"; 
10. Incluir coluna "variavel" com o código da variável em todas as linhas. 

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os códigos das variáveis | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| [Ano] | Preencher o cabeçalho com o valor do ano, de acordo com o ano indicado originalmente na coluna C. Preencher as linhas de valores de acordo com os valores de número da população em idade escolar (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
