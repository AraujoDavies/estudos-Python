# como fazer uma Busca aninhada pelo HREF
from selenium import webdriver
from selenium.webdriver.common.by import By

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

def find_by_href(browser, link):
    """ Encontrar o elemento a com o link 'link'
    
    argumentos:
    - browser = instancia do browser (firefox, chrome, etc...)
    - link = link que será procurado em todas as tags 'a'
    """
    elementos = browser.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = webdriver.Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

# chamando as funções:
# elementos_x = find_by_text(browser, 'li', 'DuckDuckGo')
elementos_x = find_by_href(browser, 'ddg')

print(elementos_x.text)
print(elementos_x.get_attribute('href'))

browser.quit()