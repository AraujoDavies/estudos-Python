# Functools partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from functools import partial

"""
Na aula anterior fizemos duas funções q fazia a mesma coisa pois o until() 
não nos deixar enviar a função com varios parametros, exemplo: "until(wait_btn(parm1, parm2))"
o correto é apenas: "until(wait_btn)"

usando o Functools partial resolve o problema
"""

def wait_element(element, b): 
    btn = b.find_element(By.ID, element)
    # pode forçar um erro aqui para o return ser False
    print(f'tentando achar: {element}')
    return bool(btn)

################# usando functools #####################
wait_btn = partial(wait_element, "request")
wait_msg = partial(wait_element, 'finished')
# atenção a estrutura da def wait_element
################# usando functools #####################

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

wait.until(wait_msg, "Msg de sucesso não retornada")