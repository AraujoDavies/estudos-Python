from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver # faz a ligação entre o webdriver e a class
)


class Escuta(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para página anterior')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME,'span').text)
        print(f'antes do click no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME,'span').text)
        print(f'depois do click no {elemento.tag_name}')


browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Escuta()) #faz a ligação entre a classe e o selenium

rapi_browser.get('https://selenium.dunossauro.live/aula_07_d')

input_de_texto = rapi_browser.find_element(By.TAG_NAME,'input')
span = rapi_browser.find_element(By.TAG_NAME,'span')
p = rapi_browser.find_element(By.TAG_NAME,'p')

input_de_texto.click()
span.click()
rapi_browser.get('https://selenium.dunossauro.live/aula_07_c')

rapi_browser.back()

browser.quit()