import os
from dotenv import load_dotenv

load_dotenv()

URL= os.getenv("URL_Site")


print (f"URL DO SITE {URL}")

#entrar no site
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://ssi.aexecutiva.com.br/vagas')
input('')