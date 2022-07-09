# implicity Waits

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_09_a.html'
b.get(url)

# vai esperar por 20 segundo até o elemento procurado aparecer
b.implicitly_wait(20) 
# não é igual ao sleep, q para por um tempo a execução do código

# uso o wait pra esperar o carregamento das variaveis a seguir...
btn = b.find_element(By.TAG_NAME, 'button') #2
btn.click()
el = b.find_element(By.ID, 'finished') #3

assert el.text == "Carregamento concluído", "CC não encontrado l19"

# ponto negativo: se ele não encontrar ele vai esperar 20 segundos q nem um besta :D