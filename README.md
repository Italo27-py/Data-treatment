Claro kkk. Deixei com uma linguagem mais natural, menos “formal demais” e com mais cara de texto feito por aluno explicando o próprio projeto:

````markdown
# Tratamento de Dados - Campe Supply

Este repositório foi criado para organizar o desenvolvimento do meu projeto de tratamento de dados em Python. A ideia foi trabalhar em cima de uma base corrompida, corrigindo problemas como valores vazios, erros de digitação, dados em formatos incorretos e colunas inconsistentes.

Também utilizei o GitHub para registrar as mudanças feitas no código por meio dos commits, deixando o processo mais organizado e fácil de acompanhar.

## Objetivo

O objetivo principal do projeto foi tratar uma base de dados para deixá-la mais limpa e pronta para futuras análises. Durante o processo, precisei analisar as colunas, entender os problemas existentes e aplicar soluções usando Python, principalmente com a biblioteca Pandas.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- PyCharm
- Git
- GitHub

## Etapas do projeto

### Importação da base

A base foi importada a partir de um arquivo CSV usando o Pandas.

```python
import pandas as pd

dataset = pd.read_csv("Dados_asimov_corrompido.xlsx - Campe Supply.csv")
````

### Análise inicial

No começo, usei alguns comandos para entender melhor a estrutura da tabela, visualizar as primeiras linhas, verificar os nomes das colunas, os tipos de dados e a quantidade de valores vazios.

```python
print(dataset.head())
print(dataset.columns)
print(dataset.isna().sum())
print(dataset.dtypes)
```

Essa etapa foi importante para saber quais colunas precisavam de tratamento.

### Tratamento de valores vazios

Durante o tratamento, encontrei várias colunas com valores ausentes. Em alguns casos, foi possível preencher esses espaços com valores padrão.

Um exemplo foi a coluna `SETOR`, onde os valores vazios foram preenchidos como `Congelados`.

```python
dataset["SETOR"] = dataset["SETOR"].fillna("Congelados")
```

Em outras colunas, como `região` e `ESTADO`, o tratamento exigiu mais atenção, pois não fazia sentido preencher tudo com o valor mais repetido sem considerar a relação entre região e estado.

### Correção de erros de escrita

Algumas colunas tinham muitos erros de digitação, principalmente nas categorias. Por isso, utilizei dicionários de correção para padronizar os nomes.

As principais colunas corrigidas foram:

* `região`
* `SETOR`
* `VENDEDOR`
* `CLIENTE`

Exemplo:

```python
dataset["SETOR"] = dataset["SETOR"].replace(correcao_setor)
```

Essa parte foi uma das mais trabalhosas, porque foi necessário verificar os valores únicos das colunas e corrigir os erros encontrados.

### Recriação de algumas colunas

Em alguns casos, percebi que era mais viável recriar determinadas colunas a partir de outras informações da tabela.

A coluna `PRODUTO`, por exemplo, foi recriada a partir da coluna `SETOR`.

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

Também utilizei uma lógica parecida para recriar a coluna `ESTADO` a partir da coluna `região`, respeitando os estados possíveis para cada região.

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

### Tratamento dos valores numéricos

As colunas numéricas estavam em formato de texto, principalmente por causa do uso de vírgula como separador decimal. Para conseguir fazer cálculos e análises, foi necessário converter esses dados para números.

```python
colunas_numericas = ["FATURAMENTO", "MARGEM DE LUCRO", "LUCRO"]

for coluna in colunas_numericas:
    dataset[coluna] = dataset[coluna].astype(str).str.replace(",", ".", regex=False)
    dataset[coluna] = pd.to_numeric(dataset[coluna], errors="coerce")
```

Depois disso, foi possível analisar melhor os dados numéricos com comandos como:

```python
print(dataset[colunas_numericas].describe())
```

### Criação da coluna de lucro calculado

Durante a análise, percebi que alguns valores da coluna `LUCRO` não batiam com o cálculo feito a partir do `FATURAMENTO` e da `MARGEM DE LUCRO`.

Por isso, criei uma nova coluna chamada `LUCRO_CALCULADO`.

```python
dataset["LUCRO_CALCULADO"] = dataset["FATURAMENTO"] * dataset["MARGEM DE LUCRO"]
dataset["LUCRO_CALCULADO"] = dataset["LUCRO_CALCULADO"].round(2)
```

Essa coluna foi criada para deixar o valor do lucro mais coerente com os outros dados da tabela.

### Organização final da tabela

Depois dos tratamentos, reorganizei as colunas em uma ordem mais lógica para facilitar a leitura e a análise.

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

### Exportação da base tratada

No final do processo, criei um novo arquivo CSV com a base já tratada.

```python
dataset.to_csv("dados_tratados.csv", index=False)
```

Também é possível salvar usando `;` como separador, o que facilita a abertura do arquivo no Excel.

```python
dataset.to_csv("dados_tratados.csv", index=False, sep=";")
```

## Aprendizados

Durante o projeto, consegui praticar vários pontos importantes do tratamento de dados, como:

* identificação de valores vazios;
* correção de erros de digitação;
* padronização de categorias;
* conversão de dados para o tipo correto;
* criação de novas colunas;
* uso de regras lógicas para reconstruir informações;
* organização da tabela final;
* exportação de uma nova base tratada.

Uma das maiores dificuldades foi lidar com colunas categóricas muito corrompidas. Em alguns momentos, não dava para simplesmente preencher os dados com o valor mais repetido, porque isso poderia gerar informações incoerentes. Por isso, foi necessário pensar em soluções que fizessem sentido dentro do contexto da tabela.

## Conclusão

Esse projeto foi importante para colocar em prática o tratamento de dados usando Python. Apesar de algumas etapas parecerem simples no início, a base apresentou vários problemas que exigiram análise e tomada de decisão.

Com isso, consegui entender melhor a importância de preparar bem os dados antes de qualquer análise. No final, foi gerado um novo arquivo tratado, mais organizado e pronto para ser usado em futuras análises exploratórias.

```
```
