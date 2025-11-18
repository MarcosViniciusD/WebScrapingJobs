#importações 
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


#definir o que fazer
#entrar no site - ok
#acessar cidade desejada (americana, nova odessa, santa barbada do oeste)-
#pegar jobs da cidade desejada
#printar no arquivo csv
#ir para a proxima cidade - loop



#entrar no site
driver = webdriver.Chrome()
driver.get('https://ssi.aexecutiva.com.br/vagas')
sleep(6)

cidades_busca = [
    '//*[@id="cidade"]/option[2]' , #americana
    '//*[@id="cidade"]/option[8]', #nova odessa
    '//*[@id="cidade"]/option[10]', #sta brb doeste
]

for nome_da_cidade in cidades_busca:
    print(f'Cidades sendo buscada, calma um pouco :D')
    print(f"Buscando vagas para a cidade {nome_da_cidade}")


    try:
        selecionar_cidade =  driver.find_element(By.XPATH,'//*[@id="cidade"]')
        selecionar_cidade.click()
        sleep(5)
    except:
        print('Não foi possivel localizar a cidade')
