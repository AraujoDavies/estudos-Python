# Primeira Automação - Clicando no adiciona Ancora 10 vezes

# #bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#variaveis
url = 'https://curso-python-selenium.netlify.app/aula_03.html#'
browser = webdriver.Firefox()

#abrindo navegador
browser.get(url)
sleep(1)

#encontrando elemento
a = browser.find_element(By.TAG_NAME, "a")
ps = browser.find_elements(By.TAG_NAME, "p")

#loop for
for click in range(10):
    ps = browser.find_elements(By.TAG_NAME, "p")
    a.click()
    print(f' P value = {ps[-1].text} Click({click}) |  Boolean: {ps[-1].text != str(click)}' )

# fechando navegador
browser.quit()