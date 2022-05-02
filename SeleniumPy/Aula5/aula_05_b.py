# Encontrando elementos por Classe
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_b.html')

linguagens = firefox.find_elements(By.CLASS_NAME, 'linguagens')

for linguagem in linguagens:
    print(
        linguagem.find_element(By.TAG_NAME, 'h2').text, '-',
        linguagem.find_element(By.TAG_NAME, 'p').text
    )

firefox.quit()