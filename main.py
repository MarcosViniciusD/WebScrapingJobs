import os
from dotenv import load_dotenv

load_dotenv()

URL= os.getenv("URL_Site")


print (f"URL DO SITE {URL}")

#entrar no site