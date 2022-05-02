# conceitos de BACK e Forward - Browser history
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def find_by_text(browser, tag, text):
    """ Encontrar o elemento com o texto 'text'
    
    argumentos:
    - browser = instancia do browser (firefox, chrome, etc...)
    - text = Conteudo q deve estar na tag
    - tag = tag onde o texto será procurado
    """
    elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento

browser = webdriver.Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

caixas = ['um', 'dois', 'tres', 'quatro']

for n in caixas:
    sleep(0.3)
    find_by_text(browser, 'div', n).click()

for n in caixas:
    sleep(0.3)
    browser.back()

for n in caixas:
    sleep(0.3)
    browser.forward()

browser.quit()