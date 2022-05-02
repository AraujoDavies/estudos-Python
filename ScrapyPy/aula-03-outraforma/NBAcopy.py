# -*- encoding: utf-8 -*-

import requests #pip install requests
import pandas as pd #pip install pandas #pip install lxml (analisa o html/xml)
from bs4 import BeautifulSoup #pip install beautifilsoup4
from selenium import webdriver #pip install selenium
from selenium.webdriver.firefox.options import Options
import json
from selenium.webdriver.common.by import By
from time import sleep

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

top10ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
}

def buildrank(type):

        field = rankings[type]['field']
        label = rankings[type]['label']
        
        # click para pegar o rank em ordem certa
        driver.find_element(By.XPATH,
                f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()

        # pegando HTML da tabela 
        tabela_dados = driver.find_element(By.XPATH,
                "//div[@class='nba-stat-table']//table")
        html_content = tabela_dados.get_attribute('outerHTML') #=str

        #parseando HTML para transformá-lo em dado estruturado facilitando muito a vida :D
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table') #=class

        #(Estruturar conteúdo em um Data Frame) - Pandas
        # eliminando as tags HTML
        df_full = pd.read_html(str(table))[0].head(10) # pegar 10 primeiros itens da tabela
        df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]] # quais dados pegar
        df.columns = ['pos', 'player', 'team', 'total'] # cria colunas

        # criando meu dicionário com os dados

        return df.to_dict('records') # converte em dict e retorna

option = Options()
option.headless = True
driver = webdriver.Firefox()#(options=option) #faz a mágica sem abrir o browser

driver.get(url)
driver.implicitly_wait(15)  # in seconds

for i in rankings:
        top10ranking[i] = buildrank(i)
        sleep(2)

driver.quit()

with open('ranking.json', 'w', encoding='utf-8') as jp:
# criando arquivo JSON
# json só faz dump ou load 
# (o primeiro converte o obj em str, enquanto o load faz o oposto)
    jayzon = json.dumps(top10ranking, indent=4)
    jp.write(jayzon)