# Encontrando elementos por [Atributos]
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_06_a.html'

b = webdriver.Firefox()
b.get(url)

el = b.find_element(By.CSS_SELECTOR, 'input')
el.send_keys('Davies')

"""
pode buscar por [atributo] ou [atributo operador valor]

[atributo=valor] exatamente igual
[atributo*=valor] deve ocorrer (útil)
[atributo|=valor] exatamente igual ou iniciar
[atributo^=valor] iniciado em 
[atributo$=valor] terminado em
[atributo~=valor] um deve ser exatamente igual
"""

# usando o atributo type [attr=valor]
#nome = b.find_element(By.CSS_SELECTOR, '[type="text"]')
#senha = b.find_element(By.CSS_SELECTOR, '[type="password"]')
#btn = b.find_element(By.CSS_SELECTOR, '[type="submit"]')

# usando o atributo name [attr=valor]
#nome = b.find_element(By.CSS_SELECTOR, '[name="nome"]')
#senha = b.find_element(By.CSS_SELECTOR, '[name="senha"]')
#btn = b.find_element(By.CSS_SELECTOR, '[name="l0c0"]')

# usando o atributo * [att*=valor]
#nome = b.find_element(By.CSS_SELECTOR, '[name*="ome"]')
#senha = b.find_element(By.CSS_SELECTOR, '[name*="nha"]')
#btn = b.find_element(By.CSS_SELECTOR, '[name*="l0"]')

nome.send_keys('Davies')
senha.send_keys('noob123')
btn.click()

#vc pode fazer isso de 3 mil maneiras diferentes