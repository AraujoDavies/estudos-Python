# Pegar dados da seguinte pagina web: https://curso-python-selenium.netlify.app/exercicio_01.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#browser
browser = webdriver.Firefox()
browser.get('https://curso-python-selenium.netlify.app/exercicio_01.html')

sleep(1)

#localizando todas as informações
h1 = browser.find_element(By.TAG_NAME, "h1")
t1 = browser.find_element(By.XPATH, "/html/body/p[1]")
t2 = browser.find_element(By.XPATH, "/html/body/p[2]")
t3 = browser.find_element(By.XPATH, "/html/body/p[3]")

#retornando as informações :D
print(h1.text)
print(t1.text)
print(t2.text)
print(t3.text)

browser.quit()