# ObservaSampa: Automação de variáveis 
## **Processo:** SP156

library(tidyverse)

##O indicador será regionalizado por subprefeitura, para isso será preciso
#Puxar o código de sub da API do Observa
library(rjson)
cdsub<- "https://api.observasampa.prefeitura.sp.gov.br/v1/basic/regioes/?cd_nivel_regiao=2" 
cdsub<- fromJSON(paste(readLines(cdsub), collapse=""))
json_file <- lapply(cdsub, function(x) {
  x[sapply(x, is.null)] <- NA
  unlist(x)
})
df<-as.data.frame(t(do.call("cbind", json_file)))
codigosub<- df %>% rename(subprefeituras = nm_regiao_padrao,
                          regiao = cd_regiao)
codigosub<- codigosub %>% mutate(regiao= paste0( 00 , regiao),
                                 regiao = str_sub(regiao, start = -2),
                                 regiao= paste0("S", regiao))
                            

#Baixar base do SP156
sp156_t4<- read_delim("http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/dee8a960-805d-4c0b-aa69-62e8c4692eee/download/arquivofinal4tri2021.xlsx.csv",
                      delim = ",", locale = locale(encoding = "UTF-8"))
sp156_t3<- read_delim("http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/e63c9267-daf4-4395-be6c-d96dbad72b2a/download/arquivofinal3tri2021.xlsx.csv",
                      delim = ",", locale = locale(encoding = "UTF-8"))
sp156_t2<- read_delim("http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/ece6dc7c-6f1b-478d-afe9-71deb8117116/download/arquivofinal2tri2021.xlsx.csv",
                      delim = ",", locale = locale(encoding = "UTF-8"))
sp156_t1<- read_delim("http://dados.prefeitura.sp.gov.br/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d9c502f0-dcc1-4d2d-948a-0fc0520852cc/download/arquivofinal1tri2021.xlsx.csv",
                      delim = ",", locale = locale(encoding = "UTF-8"))
sp156<- rbind(sp156_t1, sp156_t2, sp156_t3, sp156_t4)

#Para V0201
V0201<- data.frame(summarise(sp156, n()))
V0201<- V0201 %>% rename("2021" = "n..") %>%  mutate(regiao = "M00")
tabela<- data.frame(table(sp156$Subprefeitura))
tabela<- tabela %>% rename(subprefeituras = Var1, "2021" = Freq)

tabela<- inner_join(tabela, codigosub, by = "subprefeituras")
tabela<- tabela %>%  select(regiao, "2021")
V0201<- rbind(V0201, tabela)
V0201<- V0201 %>% mutate(variavel = "V0201")
V0201<- V0201 %>% select(variavel, regiao, "2021")

#Para V0202
filtV0202<- filter(sp156, Tema == "Acessibilidade")
V0202<- data.frame(summarise(filtV0202, n()))
V0202<- V0202 %>% rename("2021" = "n..") %>%  mutate(regiao = "M00")
tabela2<- data.frame(table(filtV0202$Subprefeitura))
tabela2<- tabela2 %>% rename(subprefeituras = Var1, "2021" = Freq)
#Inserir coluna com códigos do observa
tabela2<- inner_join(tabela2, codigosub, by = "subprefeituras")
tabela2<- tabela2 %>%  select(regiao, "2021")
V0202<- rbind(V0202, tabela2)
V0202<- V0202 %>% mutate(variavel = "V0202")
V0202<- V0202 %>% select(variavel, regiao, "2021")

#Para V0485
filtV0485<- filter(sp156, Serviço == "Alagamento" | Serviço == "Inundação")
V0485<- data.frame(summarise(filtV0485, n()))
V0485<- V0485 %>% rename("2021" = "n..") %>%  mutate(regiao = "M00")
tabela3<- data.frame(table(filtV0485$Subprefeitura))
tabela3<- tabela3 %>% rename(subprefeituras = Var1, "2021" = Freq)
#Inserir coluna com códigos do observa
tabela3<- inner_join(tabela3, codigosub, by = "subprefeituras")
tabela3<- tabela3 %>%  select(regiao, "2021")
V0485<- rbind(V0485, tabela3)
V0485<- V0485 %>% mutate(variavel = "V0485")
V0485<- V0485 %>% select(variavel, regiao, "2021")

#Para V0486
filtV0486<- filter(sp156, Serviço == "Solicitar limpeza da via pública após enchentes ou eventos")
V0486<- data.frame(summarise(filtV0486, n()))
V0486<- V0486 %>% rename("2021" = "n..") %>%  mutate(regiao = "M00")
tabela4<- data.frame(table(filtV0486$Subprefeitura))
tabela4<- tabela4 %>% rename(subprefeituras = Var1, "2021" = Freq)
#Inserir coluna com códigos do observa
tabela4<- inner_join(tabela4, codigosub, by = "subprefeituras")
tabela4<- tabela4 %>%  select(regiao, "2021")
V0486<- rbind(V0486, tabela4)
V0486<- V0486 %>% mutate(variavel = "V0486")
V0486<- V0486 %>% select(variavel, regiao, "2021")

#salvando planilhas no PC para subir no ObservaSampa
write_csv2(V0201, file = "C:\\Users\\nome_login\\Documents\\V0201.csv")
write_csv2(V0202, file = "C:\\Users\\nome_login\\Documents\\V0202.csv")
write_csv2(V0485, file = "C:\\Users\\nome_login\\Documents\\V0485.csv")
write_csv2(V0486, file = "C:\\Users\\nome_login\\Documents\\V0486.csv")
