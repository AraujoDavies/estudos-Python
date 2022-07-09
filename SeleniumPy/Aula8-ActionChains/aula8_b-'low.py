from selenium import webdriver
from selenium.webdriver.common.by import By
#low-level
from selenium.webdriver.common.action_chains import ActionChains
#como digitar com shift...
"""
 importando a lib KEY do selenium OU pegando os codes das letras
"""
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
page = "https://selenium.dunossauro.live/aula_08_a.html"
palavra = 'Selenium'

browser.get(page)

txt = browser.find_element(By.TAG_NAME, 'textarea')

low = ActionChains(browser)
low.move_to_element(txt) # no low level é um passo de cada vez
low.click(txt) # clica 
low.key_down(Keys.SHIFT)
for letra in palavra:
    low.key_down(letra)
    low.key_up(letra)
low.key_up(Keys.SHIFT)
low.perform() # tem q performar!!! 