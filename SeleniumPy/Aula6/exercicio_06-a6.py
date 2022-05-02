# Vencer o forms complexo 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
url = 'https://selenium.dunossauro.live/exercicio_06.html'
# abrindo navegador
b = webdriver.Firefox()
b.get(url)

#função que preenche
def preenche(form):
    """dentro do parametro coloque o nome do formularia a ser preenchido e ele fará o resto"""
    # elementos:
    nome = f'.form-{form} input[name=nome]'
    senha = f'.form-{form} input[name=senha]'
    submit = f'.form-{form} .form-btn'
    #preenche nome & senha
    nome = b.find_element(By.CSS_SELECTOR, nome)
    senha = b.find_element(By.CSS_SELECTOR, senha)
    senha.send_keys('senhaqqr')
    nome.send_keys('Aqui :D')
    #envia form
    sleep(1)
    submit = b.find_element(By.CSS_SELECTOR, submit)
    submit.click()

s = b.find_elements(By.CSS_SELECTOR, 'span')
sleep(0.2)
ja_preenchi = s[1].text

while 1<2:
    if ja_preenchi == '':
        break
    s = b.find_elements(By.CSS_SELECTOR, 'span')
    sleep(0.2)
    qual_preencher = s[0].text
    ja_preenchi = s[1].text
    preenche(qual_preencher)
    sleep(2)

print('Forms vencido - porém com erros KKKKKKKKKKK')