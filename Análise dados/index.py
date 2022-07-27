# PAsso 1: Importar a base dados
import pandas as pd
import plotly.express as px

# fonte dos dados https://www.kaggle.com/datasets
tabela = pd.read_csv("./telecom_users.csv")

# Passo 2: Visializar os dados
# Entender as informações que você tem disponível
# Descobrir as cagadas da base de dados

# excluir coluna inútil
tabela = tabela.drop("Unnamed: 0", axis=1)


#Passo 3: Tratamentos de dados (resolver as cagadas da base de dados)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Deletar coluna completamente  vazia
tabela = tabela.dropna(how="all", axis=1)

#Deletar linha com alguma informação  vazia
tabela = tabela.dropna(how="any", axis=0)
# print(tabela.info())


# Passo 4: Análise inicial dos dados
# Como estão os cancelamentos ? 26%?

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Descobrir os motivos do cancelamento

for coluna in tabela.columns: 

    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()