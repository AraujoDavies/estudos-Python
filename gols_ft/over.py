# Importa as opções do Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from time import sleep
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxProfile

options=Options()
firefox_profile = FirefoxProfile()
options.profile = firefox_profile

# url da página inicial da academia das apostas
academia = "https://www.academiadasapostasbrasil.com/"

# abrindo o Navegador e Request
f = options.profile

f = Firefox(options.profile) 

f.get(academia)