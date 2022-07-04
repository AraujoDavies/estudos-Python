"""Checar as Mudanças do site, nas tags:
span (focus, blur) blur = desfoque
p (change)
"""


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_07_d.html')

input_text = browser.find_element(By.TAG_NAME, 'input')
span = browser.find_element(By.TAG_NAME, 'span')
p = browser.find_element(By.TAG_NAME, 'p')

"""
Quando clicar no input
o texto de p deve ser 'está com foco'
Quando clicar no p
o texto de p deve ser 'está sem foco'
"""
input_text.click()
assert "está com foco" == span.text, "'está com foco' não está em span"
p.click()
assert "está sem foco" == span.text, "'está sem foco' não está em span"


"""
Dado que o texto '0' deve ser o content de 'p'
Envie algo...
Então o texto '1' deve ser o content de 'p'
"""

assert p.text == "0" , 'p não é zero'
input_text.send_keys('algo')
span.click()
assert p.text == "1", 'p não é um'



browser.quit()