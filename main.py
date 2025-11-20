from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd

driver = Chrome()
driver.get("https://ssi.aexecutiva.com.br/vagas")
sleep(3)

dados = {
    'Ref': [],
    'Cargo': [],
    'Local': [],
    'Salário': [],
    'Descrição': []
}
linhas = driver.find_elements('css selector', '#tbl-vagas > tbody > tr')

for linha in linhas:
    colunas = linha.find_elements('tag name', 'td')
    
    if len(colunas) >= 5:
        dados['Ref'].append(colunas[1].text.strip())
        dados['Cargo'].append(colunas[2].text.strip())
        dados['Local'].append(colunas[3].text.strip())
        dados['Salário'].append(colunas[4].text.strip())
        dados['Descrição'].append(colunas[5].text.strip())

driver.quit()

