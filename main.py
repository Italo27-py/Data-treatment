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
agrupado=dataset["DATA DA VENDA"].value_counts()
print(agrupado)

#setor

