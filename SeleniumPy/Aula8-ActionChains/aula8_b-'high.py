# Abra a url da var page e preste atenção nas SAIDAS DE TECLADO
from selenium import webdriver
from selenium.webdriver.common.by import By

page = "https://selenium.dunossauro.live/aula_08_a.html"

browser = webdriver.Firefox()

browser.get(page)

#hi-level
txt = browser.find_element(By.TAG_NAME, 'textarea')
txt.send_keys('sOu FoDa') # no site escreva do msm jeito q o send_keys abaixo p ver a a diferença

#low-level - demonstração
from selenium.webdriver.common.action_chains import ActionChains

palavra = 'Selenium'
low = ActionChains(browser)
#low.move_to_element(txt)
low.key_down(palavra[0])
low.key_up(palavra[0])
low.perform() # tem q performar!!! 