from selenium import webdriver
from selenium.webdriver.common.by import By

page = "https://selenium.dunossauro.live/keyboard.html"
browser = webdriver.Firefox()

browser.get(page)

html = browser.find_element(By.TAG_NAME, 'html')
html.send_keys('sou foda')

"""
Eventos de teclado
# keyup
# keydown
# accesskey
"""
