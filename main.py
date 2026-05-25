import pandas as pd
import seaborn as sns
import statistics as sts

#Data import
dataset=pd.read_csv("Dados_asimov_corrompido.xlsx - Campe Supply.csv")

#Apagar colunas inúteis (UNNAMED; COLUNA INÚTIL 0 E 1)
dataset = dataset.drop(columns=["UNNAMED: 0", "coluna_inutil_0", "coluna_inutil_1"])


#Mudança do nome das colunas
dataset.columns= ["DATA DA VENDA", "SETOR", "PRODUTO", "VENDEDOR", "REGIÃO", "ESTADO", "CLIENTE", "FATURAMENTO", "MARGEM DE LUCRO", "LUCRO"]

#view
print(dataset.head().to_string())

#print(dataset.columns)

#tamanho
tamanho=dataset.shape
print(tamanho)

#Primeiro passo:
#Analise exploratória

#data da venda
agrupado_0=dataset["DATA DA VENDA"].value_counts()
print(agrupado_0)

#setor
agrupado_1=dataset["SETOR"].value_counts()
print(agrupado_1)

#produto
agrupado_2=dataset["PRODUTO"].value_counts()
print(agrupado_2)

#vendedor
agrupado_3=dataset["VENDEDOR"].value_counts()
print(agrupado_3)

#região
agrupado_4=dataset["REGIÃO"].value_counts()
print(agrupado_4)

#estado
agrupado_5=dataset["ESTADO"].value_counts()
print(agrupado_5)

#cliente
agrupado_6=dataset["CLIENTE"].value_counts()
print(agrupado_6)

#faturamento
#agrupado_7=dataset["FATURAMENTO"].describe() #variavel numerica
#print(agrupado_7)

#margem de lucro
#agrupado_8=dataset["MARGEM DE LUCRO"].describe() #variavel numerica
#print(agrupado_8)

#lucro
#agrupado_9=dataset["LUCRO"].describe() #variavel numerica
#print(agrupado_9)

#checkando dados faltantes
vazio=dataset.isnull().sum()
print(vazio)

#iniciando tratamento

dataset["DATA DA VENDA"] = dataset["DATA DA VENDA"].fillna("2035-01-31 00:00:00")
dataset["SETOR"] = dataset["SETOR"].fillna("Congelados")
dataset["PRODUTO"] = dataset["PRODUTO"].fillna("Queijo")
dataset["VENDEDOR"]= dataset["VENDEDOR"].fillna("Vanessa")
dataset["CLIENTE"]= dataset["CLIENTE"].fillna("Atacarejo")

#Tratando da parte região e estado
 #Se ESTADO existe e REGIÃO está vazia → preencher REGIÃO com base no ESTADO.
 #Se REGIÃO existe e ESTADO está vazio → preencher ESTADO com base na REGIÃO.
 #Se os dois estão vazios → colocar Sudeste e Rio de Janeiro

#Tratando tabelas numéricas

c_n = ["FATURAMENTO", "MARGEM DE LUCRO", "LUCRO"]

for coluna in c_n:
    dataset[coluna]= dataset[coluna].astype(str).str.replace(",",".", regex=False)
    dataset[coluna] = pd.to_numeric(dataset[coluna], errors="coerce")

#faturamento
agrupado_7=dataset["FATURAMENTO"].describe() #variavel numerica
print(agrupado_7)

#margem de lucro
agrupado_8=dataset["MARGEM DE LUCRO"].describe() #variavel numerica
print(agrupado_8)

#lucro
agrupado_9=dataset["LUCRO"].describe() #variavel numerica
print(agrupado_9)

dataset["FATURAMENTO"] = dataset["FATURAMENTO"].fillna(896.626673)
dataset["MARGEM DE LUCRO"] = dataset["MARGEM DE LUCRO"].fillna(0.119311)
dataset["LUCRO"] = dataset["LUCRO"].fillna(3.474494e+03)

print(dataset.head(50).to_string())

#Arrumar a formatação dos valores
# 2 casas decimais
dataset["FATURAMENTO"]=dataset["FATURAMENTO"].round(2)
dataset["LUCRO"]=dataset["LUCRO"].round(2)

print(dataset.head(50).to_string())


