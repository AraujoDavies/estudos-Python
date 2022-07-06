# pega o antes e dps de cada campo do formulário da seguinte página "https://selenium.dunossauro.live/exercicio_07.html"

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver # faz a ligação entre o webdriver e a class
)
from time import sleep

class Vigia(AbstractEventListener):
    """    def campo1(self, url, webdriver):
            print(f'indo para {url}')
        
        def campo2(self, webdriver):
            print('voltando')
    """
    def before_click(self, elemento, webdriver):
        print(f'{elemento.text}')

    def after_click(self, elemento, webdriver):
        print(f'{elemento.text}')

browser = Firefox()

f = EventFiringWebDriver(browser, Vigia()) # trabalhem juntos :D

f.get("https://selenium.dunossauro.live/exercicio_07.html")
sleep(5)
lnome = f.find_element(By.ID,'lnome')
lemail = f.find_element(By.ID,'lemail')
lsenha = f.find_element(By.ID,'lsenha')

lnome.click()
f.find_element(By.ID,'nome').send_keys('teste')
lemail.click()
f.find_element(By.ID,'email').send_keys('teste@email.com')
lsenha.click()
f.find_element(By.ID,'senha').send_keys('teste')

f.find_element(By.TAG_NAME,'legend').click() 
# ele vai retornar dois valores iguais pois o valor inicial da tag nao foi alterado

browser.find_element(By.ID,'btn').click()
#f.get("https://selenium.dunossauro.live/exercicio_03.html")
#f.back()