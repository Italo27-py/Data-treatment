import pandas as pd
import seaborn as sns
import statistics as sts

#Data import
dataset=pd.read_csv("Dados_asimov_corrompido.xlsx - Campe Supply.csv")
#view
print(dataset.head())