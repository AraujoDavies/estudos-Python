# Importa as opções do Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request

def trata_html(input):
    return " ".join(input.split()).replace('> <','><')

# url da página inicial da academia das apostas
academia = "https://www.academiadasapostasbrasil.com/"

# abrindo o firefox em background
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(academia)
# sleep (10)
# driver.quit()

#sleep(4)
for i in range(0,2):
    driver.find_element(By.XPATH, '//td[contains(@class, "footer")]')
    driver.find_element(By.XPATH, '//td[contains(@class, "footer")]').click()
    #sleep(4) # colocar uma espera aqui


html_table = driver.find_element(By.XPATH, '//table[contains(@class, "dskt")]').get_attribute('outerHTML')
html_table = trata_html(html_table)
soup = BeautifulSoup(html_table, 'html.parser')