import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# fonte dos dados => https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V
tabela = pd.read_csv("advertising.csv")

#mostra correlação
tabela.corr()


# cria o gráfico
# sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)


#  exbir gráfico
# plt.show()

# y -> quem quero prever (Vendas)
# x -> é o resto todo (quem vou usar para fazer a previsão)

x = tabela[["TV", "Radio", "Jornal"]]
y = tabela["Vendas"]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

#Cria a inteligência artificial
modelo_regressaoLinear = LinearRegression()
modelo_arvoreDecisao = RandomForestRegressor()

# treina a inteligência artificial
modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_arvoreDecisao.fit(x_treino, y_treino)

#testar os modelos

previsao_regressaoLinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoreDecisao = modelo_arvoreDecisao.predict(x_teste)

print(r2_score(y_teste, previsao_regressaoLinear))
print(r2_score(y_teste, previsao_arvoreDecisao))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["arvore_decisao"] = previsao_arvoreDecisao
tabela_auxiliar["regrassao_linear"] = previsao_regressaoLinear


plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
# plt.show()

# usando os modelos gerado

novos = pd.read_csv("novos.csv") 
previsao = modelo_arvoreDecisao.predict(novos)
print(previsao)