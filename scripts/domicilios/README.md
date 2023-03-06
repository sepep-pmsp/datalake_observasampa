# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Domicilios por distrito do município de São Paulo
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre Domicílios.

## Fontes
A [Fundação SEADE](https://repositorio.seade.gov.br/) possui em seu repositório um conjunto de dados [Domicílios por Distrito do Município de São Paulo](https://repositorio.seade.gov.br/dataset/domicilios-estado-de-sao-paulo/resource/e9f71c03-8dfd-4fea-bc8f-7723a6d9c0df) o qual possui colunas com o código do distrito, nome do distrito, ano e domicílios (número de domicílios).

Anualmente é inserida a projeção populacional realizada pela Fundação. Portanto, anualmente esta base deve ser atualizada no fluxo da automação.

## Destinos

Este processo tem como destino a criação da planilha com informações da variável (V0281) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de cada ano.

## Descrição do processo

### Para a variável V0281 (Domicílios particulares permanentes):
1. Baixar o arquivo do Repositório SEADE (https://repositorio.seade.gov.br/dataset/domicilios-estado-de-sao-paulo/resource/e9f71c03-8dfd-4fea-bc8f-7723a6d9c0df);
2. Pivotar o valor da coluna D "domicílio", de cada "ano" (coluna C), para cada nome de distrito (coluna B "nome_distrito");
3. Padronizar o nome do distrito (coluna B "nome_distrito");
4. Inserir a coluna "região", com os códigos aceitos pelo sistema do ObservaSampaa para cada distrito correspondente;
5. Excluir a coluna A "cod_distrito" da SEADE;
6. Incluir uma nova linha para o Município, em que se deve somar os valores de todos os distritos para cada ano, bem como inserir o código do ObservaSamapa para o município na coluan "região";
7. Incluir novas linhas para as subprefeituras. Na coluna "região", incluir o código do ObservaSamapa para cada subprefeituras correspondente e somar, para cada ano e subprefeitura, os valores dos distritos que correspondam a cada subprefeitura; 
8. Excluir a coluna "nome_distrito";
9. Incluir coluna "variável" com o código da variável em todas as linhas. 


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, preenhcer todas as linhas com V0281 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o ano indicado originalmente na coluna C. Preencher as linhas de valores de acordo com os valores de número de domicílios, originalmente na coluna D (ver descrição do processo acima) | Inteiro | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
