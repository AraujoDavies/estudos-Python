# Importa as opções do Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from time import sleep
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import FirefoxProfile
import json

# url da página inicial da academia das apostas
academia = "https://www.academiadasapostasbrasil.com/"
# abrindo o Navegador e Request
f = Firefox()
f.get(academia)
wdw = WebDriverWait(f, 30, poll_frequency=1)


qt_analises_page = 1 # quantas vezes a lista de jogos foram att
def prox_urls(): 
    """
    Faz o click para listar os próximos jogos && tem um contador
    """
 
    global qt_analises_page
    next_btn = f.find_element(By.XPATH, '//div[@class= "widget-double-container-left mb-content"]//span[contains(@class, "date-increment")]')
    
    qt_analises_page += 1
    next_btn.click()            
    
    
times_anteriores = []
def valida_html():
    """
    Vai verificar se o time da lista atual é igual ao da lista 
    anterior e retornar BOOL para validar a expansão
    """
    # variável diferencial => verifica se a lista de time foi carregada :D
    time1_from_list = f.find_element(By.XPATH, '//div[@id="fh_main_tab"]//tbody//tr//p').text 
    # verifica se o time da pagina a seguir é igual ao time da página anterior e se pode ser adicionado ou não 
    if bool(times_anteriores) == False:
        # code para fazer o procedimento pela 1°vez
        times_anteriores.append(time1_from_list)
        return True
    elif bool(times_anteriores) and time1_from_list != times_anteriores[-1]:
        # code para fazer o procedimento da 2°vez em diante
        times_anteriores.append(time1_from_list)
        return True
    return False

def wait_expansao():
    """
    vai retornar TRUE até expandir tudo, ou seja enquanto houver jogos ocultos continua TRUE
    """
    try:
        btn_exp = f.find_element(By.XPATH, '//td[contains(@class, "footer")]')
    except:
        sleep(1)
        print('WARN: btn de expandir não existe mais')
        btn_exp = False
    
    return (True if bool(btn_exp) else False)
    
def click_expansao(): 
    """
     função q responsável pela expansão de todos os jogos
    """
    try:
        sleep(1)
        #while wait_expansao():
        if wait_expansao():
            btn_exp = f.find_element(By.XPATH, '//td[contains(@class, "footer")]')
            btn_exp.click()
            wdw.until_not(wait_expansao, "erro na def soup")     
    except:
        sleep(1)
        print('WARN: verificando se ainda tem btn_expandir para refazer o click')
        if wait_expansao():
            click_expansao()
    #valida_html() # é bom validar o html de novo    

urls = [] # vai guardar as urls
def soup():
    """
        cria objeto BS4;
        cria JSONs para cada dia, Ex: [ {hoje:[url, url]}, {17/07/20: [url, url]} ]
    """
    try:
        # tabela de jogos
        table_games = f.find_element(
            By.XPATH, 
            '//div[@class="widget-double livescores large"]').get_attribute(
                'outerHTML'
                )
        soup = BeautifulSoup(table_games, 'html.parser') # criando soup
        date = soup.find('label').attrs['data-displaydate'] # data
        href = soup.find_all('td', class_='score') # todas partidas
        print(f'DIA: {date} - Jogos adicionados: {len(href)}')
        all_urls = {date: [] }
        # preciso pegar a referencia da data p
        for link in href:
            all_urls[date].append(link.find('a').attrs['href'])
        urls.append(all_urls)
    except:
        print('soup error')

def gerar_json():
    with open('urls.json', 'w', encoding='utf-8') as jp:
        # criando arquivo JSON
        # json só faz dump ou load 
        # (o primeiro converte o obj em str, enquanto o load faz o oposto)
        jayzon = json.dumps(urls, indent=4)
        jp.write(jayzon)
    print('JSON gerado!')

# processoo de execução...
try:
    for i in range(x):
        print(f'iniciando {i+1}')
        if i > 0:
            prox_urls()
        #valida_html()
        wait_expansao()
        click_expansao()
        soup()
    print(f'Qt de dias analisados: {qt_analises_page}')
    gerar_json()
except:
    print('FATAL ERROR!!!!')

""" TESTES:
qt_analises_page = 1 # quantas vezes a lista de jogos foram att
times_anteriores = []

valida_html()
wait_expansao()
click_expansao()
soup()
"""