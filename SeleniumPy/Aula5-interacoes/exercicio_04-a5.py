#Exercício 4 - Aula 5

# Enviar Form
# pegar o resultado e fazer um assert com o Query da URL

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = webdriver.Firefox()
browser.get(url)

def preencher_form(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()

estrutura = {
    'nome': 'Davies',
    'email': 'Lindo@bonito.modesto',
    'senha': 'naoTimInteressa',
    'telefone': '99125003' # olha eu recaindo outra vez... LEMBREIIIIIIII que tô bloqueado
}

sleep(1)
preencher_form(browser, **estrutura)

url_parseada = urlparse(browser.current_url)
json = url_parseada.query.split('&')
json.pop() # remover ultimo elemento
query = str(json)
query = query.replace("%40", "@")
query = query.replace("=", ": ")
query = query.replace('\'', '')
#query = query.replace(']"', '}')
#query = loads(query)

sleep(3)
site_result = browser.find_element(By.ID, 'main').find_element(By.TAG_NAME, 'textarea').text
site_result = site_result.replace("\"", "")
site_result = site_result.replace("{", "[")
site_result = site_result.replace("}", "]")
site_result = site_result.replace("\'", "")

assert site_result == query
