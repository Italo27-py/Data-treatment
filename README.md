# Tratamento de Dados - Campe Supply

Este repositório foi criado para documentar o processo de tratamento de dados realizado em Python, utilizando principalmente as bibliotecas Pandas e NumPy. O objetivo principal do projeto foi limpar, corrigir, padronizar e reorganizar uma base de dados corrompida, tornando-a mais adequada para análises futuras.

## Objetivo do projeto

O projeto teve como foco o tratamento de uma planilha com inconsistências em dados categóricos, numéricos e valores ausentes. Durante o processo, foram aplicadas técnicas de limpeza, correção de erros de digitação, preenchimento de lacunas vazias, criação de novas colunas e reorganização da estrutura final da tabela.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- PyCharm
- Git
- GitHub

## Principais etapas realizadas

### 1. Importação dos dados

A base foi importada a partir de um arquivo CSV utilizando a biblioteca Pandas.

```python
import pandas as pd

dataset = pd.read_csv("Dados_asimov_corrompido.xlsx - Campe Supply.csv")
````

### 2. Análise inicial da base

Foram utilizados comandos para visualizar as primeiras linhas da tabela, verificar os nomes das colunas, identificar valores vazios e analisar os tipos de dados.

```python
print(dataset.head())
print(dataset.columns)
print(dataset.isna().sum())
print(dataset.dtypes)
```

### 3. Tratamento de valores vazios

Foram tratados valores ausentes em diferentes colunas da base. Em alguns casos, os valores vazios foram preenchidos com base em regras específicas do projeto.

Exemplo:

```python
dataset["SETOR"] = dataset["SETOR"].fillna("Congelados")
```

No caso das colunas `região` e `ESTADO`, foi adotada uma estratégia mais cuidadosa, pois os dados possuem relação entre si. Como a coluna `ESTADO` apresentava muitas inconsistências, ela foi recriada a partir da coluna `região`, respeitando os estados possíveis para cada região.

### 4. Correção de erros de escrita

Algumas colunas categóricas apresentavam diversos erros de digitação. Para corrigir isso, foram criados dicionários de substituição.

As principais colunas tratadas foram:

* `região`
* `SETOR`
* `VENDEDOR`
* `CLIENTE`

Exemplo:

```python
dataset["SETOR"] = dataset["SETOR"].replace(correcao_setor)
```

Essa abordagem permitiu padronizar os valores e reduzir inconsistências na base.

### 5. Recriação de colunas com base em regras

Algumas colunas estavam muito corrompidas ou não faziam sentido em relação a outras informações. Por isso, foram recriadas com base em regras lógicas.

Por exemplo, a coluna `PRODUTO` foi recriada a partir da coluna `SETOR`.

```python
import numpy as np

produtos_por_setor = {
    "Carnes": ["Bovina", "Suína", "Frango"],
    "Laticínio": ["Queijo", "Sorvete", "Leite", "Coalhada"],
    "Congelados": ["Pizza", "Lasanha"],
    "Bebidas": ["Sucos", "Refrigerantes", "Cervejas"]
}

dataset["PRODUTO"] = dataset["SETOR"].apply(
    lambda setor: np.random.choice(produtos_por_setor[setor])
)
```

A mesma lógica foi aplicada para recriar a coluna `ESTADO` com base na coluna `região`.

```python
estados_por_regiao = {
    "Sudeste": ["Rio de Janeiro", "Minas Gerais", "São Paulo"],
    "Sul": ["Paraná", "Santa Catarina", "Rio Grande do Sul"],
    "Nordeste": ["Bahia", "Sergipe", "Rio Grande do Norte"]
}

dataset["ESTADO"] = dataset["região"].apply(
    lambda regiao: np.random.choice(estados_por_regiao[regiao])
)
```

### 6. Tratamento de valores numéricos

As colunas numéricas apresentavam valores em formato de texto, principalmente por causa do uso de vírgula como separador decimal.

Por isso, foi feita a conversão para formato numérico.

```python
colunas_numericas = ["FATURAMENTO", "MARGEM DE LUCRO", "LUCRO"]

for coluna in colunas_numericas:
    dataset[coluna] = dataset[coluna].astype(str).str.replace(",", ".", regex=False)
    dataset[coluna] = pd.to_numeric(dataset[coluna], errors="coerce")
```

Após a conversão, foi possível analisar média, mediana, quartis e outros indicadores estatísticos.

```python
print(dataset[colunas_numericas].describe())
```

### 7. Criação da coluna de lucro calculado

Durante a análise, foi identificado que alguns valores da coluna `LUCRO` não correspondiam ao cálculo esperado a partir de `FATURAMENTO` e `MARGEM DE LUCRO`.

Por isso, foi criada uma nova coluna chamada `LUCRO_CALCULADO`.

```python
dataset["LUCRO_CALCULADO"] = dataset["FATURAMENTO"] * dataset["MARGEM DE LUCRO"]
dataset["LUCRO_CALCULADO"] = dataset["LUCRO_CALCULADO"].round(2)
```

Essa nova coluna garante maior coerência nos dados financeiros.

### 8. Reorganização da tabela

Ao final do tratamento, as colunas foram reorganizadas em uma ordem mais lógica para análise.

```python
colunas_ordenadas = [
    "data da venda",
    "SETOR",
    "PRODUTO",
    "VENDEDOR",
    "região",
    "ESTADO",
    "CLIENTE",
    "FATURAMENTO",
    "MARGEM DE LUCRO",
    "LUCRO_CALCULADO"
]

dataset = dataset[colunas_ordenadas]
```

### 9. Exportação do arquivo tratado

Após todos os tratamentos, foi criado um novo arquivo CSV com os dados limpos.

```python
dataset.to_csv("dados_tratados.csv", index=False)
```

Também é possível salvar com separador `;`, facilitando a abertura no Excel em português.

```python
dataset.to_csv("dados_tratados.csv", index=False, sep=";")
```

## Aprendizados

Durante o projeto, foi possível praticar conceitos importantes de tratamento de dados, como:

* identificação de valores ausentes;
* padronização de categorias;
* correção de erros de digitação;
* conversão de variáveis para tipos corretos;
* criação de novas colunas;
* uso de regras lógicas para reconstrução de dados;
* análise estatística inicial com Pandas;
* exportação de uma nova base tratada.

Um dos principais desafios foi lidar com colunas categóricas muito corrompidas, como `região`, `ESTADO`, `SETOR`, `VENDEDOR` e `CLIENTE`. Esse processo mostrou a importância de analisar os valores únicos antes de aplicar qualquer correção automática.

## Conclusão

O projeto foi importante para aplicar na prática conceitos de limpeza e preparação de dados. Além de utilizar comandos básicos do Pandas, foi necessário pensar em estratégias coerentes para tratar inconsistências sem comprometer a lógica da base.

A etapa de tratamento mostrou que dados reais podem apresentar muitos problemas, como valores vazios, erros de escrita, formatos incorretos e informações inconsistentes. Por isso, antes de qualquer análise, é essencial preparar bem a base de dados.

Ao final, foi gerado um novo arquivo tratado, pronto para ser utilizado em análises exploratórias e visualizações futuras.

```
```
