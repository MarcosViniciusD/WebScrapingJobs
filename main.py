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
