# Explicit Waits
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
# import do WAIT
from selenium.webdriver.support.ui import WebDriverWait 

def wait_btn(b):
    btn = b.find_elements(By.TAG_NAME, "button") 
    # pode forçar um erro aqui para o return ser False
    print('tentando achar o Btn')
    return bool(btn)

def wait_sucess(b):
    el = b.find_element(By.ID, 'finished')
    print('tentando achar msg de sucesso')
    return bool(el)

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_09_a.html'
wait = WebDriverWait(b, 15, poll_frequency=1) # driver, timeout, tentativas por segundo
b.get(url) 

#until_not espera valor falso para validar
"""
wait.until_not(wait_btn) # callable, msg de erro 
"""

# until espera valor verdadeiro para validar
wait.until(wait_btn, "Elemento Botão não encontrado") # callable, msg de erro
b.find_element(By.TAG_NAME, "button").click()

wait.until(wait_sucess, "Msg de sucesso não retornada")