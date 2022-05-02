# esperas implícitas
 
from selenium import webdriver
from selenium.webdriver.common.by import By

f = webdriver.Firefox()
f.get('https://curso-python-selenium.netlify.app/aula_09_a.html')

f.implicitly_wait(30)

btn = f.find_element(By.TAG_NAME, 'button')
btn.click()

sucesso = f.find_element(By.CSS_SELECTOR, '#finished')
assert sucesso.text == 'Carregamento concluído'

# vai demorar 30 segundos pra retornar q elemento nao existe
f.find_element(By.CSS_SELECTOR, 'Fausto')