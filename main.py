from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import pandas as pd

driver = Chrome()
driver.get("https://ssi.aexecutiva.com.br/vagas")
sleep(3)

dados = {
    'Cidade': [],
    'Ref': [],
    'Cargo': [],
    'Local': [],
    'Salário': [],
    'Descrição': []
}

select = Select(driver.find_element('xpath','//*[@id="cidade"]'))

localidades = ["AMERICANA", "NOVA ODESSA", "SANTA BARBARA D OESTE","SANTA BARBARA D' OESTE","SANTA BARBARA D'OESTE"]

for cidade in localidades:
    print(f"Buscando vagas em {cidade}...")
    select.select_by_visible_text(cidade)
    sleep(2)

    linhas = driver.find_elements('css selector', '#tbl-vagas > tbody > tr')

    for linha in linhas:
        colunas = linha.find_elements('tag name', 'td')
        
        if len(colunas) >= 5:
            dados['Cidade'].append(cidade)
            dados['Ref'].append(colunas[1].text.strip())
            dados['Cargo'].append(colunas[2].text.strip())
            dados['Local'].append(colunas[3].text.strip())
            dados['Salário'].append(colunas[4].text.strip())
            dados['Descrição'].append(colunas[5].text.strip())

driver.quit()

df = pd.DataFrame(dados)
df.to_excel('vagas.xlsx', index=False)

print("Planilha gerada com sucesso!")
