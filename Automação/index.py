from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Passo 1: Pegar a cotação do dólar
# Abrir o navegador 

navegador = webdriver.Chrome()

# entrar no google
navegador.get("https://www.google.com.br/")
# pesquisar cotação
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoDolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacaoDolar)

#pegar cotação
# Passo 2: Pegar a cotação do euro
navegador.get("https://www.google.com.br/")
# pesquisar cotação
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoEuro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacaoEuro)


# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacaoOuro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacaoOuro = cotacaoOuro.replace(",",".")
navegador.quit()
print(cotacaoOuro)

# Passo 4: Atualizar a base de dados
# source => https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv
tabela = pd.read_excel("Produtos.xlsx")

tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacaoDolar)
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacaoEuro)
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacaoOuro)


# Passo 5: Recalcular os preços
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)


# Passo 6: Exportar a base de dados
tabela.to_excel("Produtos_novo.xlsx", index=False)