# Preenchendo Forms e verificando resultado com assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads #transforma a lista em dict

firefox = webdriver.Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05.html')

def preencher_form(browser, nome, email, senha, telefone):
    firefox.find_element(By.NAME, 'nome').send_keys(nome)
    firefox.find_element(By.NAME, 'email').send_keys(email)
    firefox.find_element(By.NAME, 'senha').send_keys(senha)
    firefox.find_element(By.NAME, 'telefone').send_keys(telefone)
    firefox.find_element(By.NAME, 'btn').click()

sleep(0.2)

#criando dicionário
estrutura = {
    'nome': 'Devão', 
    'email': 'XUXUXU@xuxu.XU',
    'senha': '1234calabocaenaoencheosaco',
    'telefone': '(019)987654321'
}

preencher_form(firefox, **estrutura)

url_parseada = urlparse(firefox.current_url)

sleep(1)

resultado = firefox.find_element(By.ID, 'result').text
resultado_arrumado = resultado.replace("\'", "\"")

dic_arrumado = loads(resultado_arrumado)

assert dic_arrumado == estrutura # garanta que tal coisa aconteça

#firefox.quit()

assert 1 == 2 # retorna ERRO