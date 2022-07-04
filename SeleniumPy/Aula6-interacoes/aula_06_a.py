# Encontrando elementos por CSS_Selector
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_06_a.html'

b = webdriver.Firefox()
b.get(url)

el = b.find_element(By.CSS_SELECTOR, 'input')
el.send_keys('Davies')

#igual na estilização 