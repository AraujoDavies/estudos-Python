"""
Exercício 3 do Curso de Selenium: Não ser pego pelo Diabão KKKK
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse

browser = webdriver.Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_03.html')

iniciar = browser.find_element(By.TAG_NAME, 'main')
sleep(0.1)
iniciar_li = iniciar.find_element(By.TAG_NAME, 'a').get_attribute('href')

browser.get(iniciar_li)

p1 = browser.find_element(By.TAG_NAME, 'main')
sleep(0.1)
p1_attr = p1.find_elements(By.TAG_NAME, 'a')

for el in p1_attr:
    if el.get_attribute('attr') == 'errado':
        link = el.get_attribute('href')
        
browser.get(link)

sleep(20)
p1 = browser.find_element(By.TAG_NAME, 'main')
sleep(0.1)
p1_attr = p1.find_elements(By.TAG_NAME, 'a')

for el in p1_attr:
    if el.text == browser.title:
        link = el.get_attribute('href')
browser.get(link)

p1 = browser.find_element(By.TAG_NAME, 'main')
sleep(1)
p1_attr = p1.find_elements(By.TAG_NAME, 'a')

url_parseada = urlparse(browser.current_url)

for el in p1_attr:
    if el.text in url_parseada.path:
        link = el.get_attribute('href')
browser.get(link)
sleep(1)
browser.refresh()