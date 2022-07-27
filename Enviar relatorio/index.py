from matplotlib.pyplot import table
import pyautogui
import webbrowser
import pyperclip
import time
import pandas


# #Passo 1: Entrar no sistema(no nosso caso vai ser entrar no link)
webbrowser.open('chrome')
pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t")
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#site carregando

time.sleep(5)
#Passo 2: Navegar no sistema e encontrar a base de dados(entrar na pasta Exportar)
pyautogui.click(x=400, y=302, clicks=2)

time.sleep(2)

#Passo 3:  Download da base de dados
pyautogui.click(x=364, y=373) # clicou no arquivo
pyautogui.click(x=1719, y=193) # clicou nos 3 pontos
pyautogui.click(x=1498, y=597) # clicou em fazer download

time.sleep(7)

pyautogui.click(x=438, y=233) # selecionar a pasta de download
pyautogui.press('enter')


# Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
tabela = pandas.read_excel("/home/luan/Downloads/Vendas - Dez.xlsx")

quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()

#Passo 5: Entrar no email

pyautogui.hotkey("ctrl", "t")
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(7)

# Passo 6: Mandar um email para a diretoria com os indicadores
# Clicar no botão mais
pyautogui.click(x=92, y=201)

# escrever o destinatário
pyautogui.write("nespudelte@vusra.com")
pyautogui.press("tab")

# escrever o assunto
pyautogui.press("tab")
pyperclip.copy("Relatório do de vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

# corpo do email
texto = f"""
Prezados bom dia
O faturamento de ontem foi de R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade}

Abs: Luan dev
"""
pyautogui.write(texto)

# enviar o email
pyautogui.hotkey("ctrl", "enter")










