from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
page = "https://selenium.dunossauro.live/caixinha"

browser.get(page)

ac = ActionChains(browser)

caixa = browser.find_element(By.ID, 'caixa')
span = browser.find_element(By.TAG_NAME, 'span')

def colors(key1=None, key2=None):
    if key1:
        ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.pause(1) # semelhante ao sleep
    ac.click(caixa)
    ac.move_to_element(span)
    ac.move_to_element(caixa) # navega nos elementos
    ac.double_click(caixa) # auto-explicativo
    if key1==None and key2==None:
        ac.context_click(caixa) # click com o botão direito
    ac.perform() # vaiiiiiii!!
    ac.pause(3)
    if key1:
        ac.key_up(key1)
    if key2:
        ac.key_up(key2)

colors(Keys.CONTROL)
colors(Keys.SHIFT)
colors()
