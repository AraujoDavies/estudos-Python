# clique até vencer o jogo https://curso-python-selenium.netlify.app/exercicio_02.html#
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html#')

sleep(1)

# elementos que manipularei
a = browser.find_element(By.TAG_NAME, "a")
nEsperado = browser.find_element(By.XPATH, "/html/body/p[2]").text
#myN é o numero esperado que eu tenho q encontrar
varinutil, myN = nEsperado.split(':') 

for click in range(30):
    a.click()
    ps = browser.find_elements(By.TAG_NAME, "p")
    lastP = ps[-1].text.split(":")

    if lastP[-1] == myN:
        break
    else: 
        print(lastP[-1])