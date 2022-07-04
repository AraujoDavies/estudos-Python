#Desafio
"""     DESAFIOS:
    1. Pegar todos as tags das aulas e printar
    {nome da aula: 'link da aula'}
    2. Navegar até o exercício 3
    pegar a URL e ir até lá
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
browser = webdriver.Firefox()

browser.get('https://selenium.dunossauro.live')

"""
Parte 1
"""
sleep(0.1)
# caminho dos itens que quero no aside
aside = browser.find_element(By.TAG_NAME, 'aside')
uls_aside = aside.find_elements(By.TAG_NAME, 'ul')
a_aside = uls_aside[0].find_elements(By.TAG_NAME, 'a')

result1 = {}

for el in a_aside:
    result1[el.text] = el.get_attribute('href')

pprint(result1)

"""
Parte 2
"""
# caminho dos itens que quero no Main
main = browser.find_element(By.ID, 'main')
uls_main = main.find_elements(By.TAG_NAME, 'ul')
li_main = uls_main[2].find_elements(By.TAG_NAME, 'li')
a_main = li_main[2].find_element(By.TAG_NAME, 'a').get_attribute('href')

browser.get(a_main)


#browser.quit()