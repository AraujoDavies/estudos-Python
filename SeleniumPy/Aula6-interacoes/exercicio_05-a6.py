# vencer o formulário preenchendo as colunas na ordem usando querySelector
url = 'https://selenium.dunossauro.live/exercicio_05.html'

from selenium import webdriver;
from selenium.webdriver.common.by import By;

#abrindo navegador
b = webdriver.Firefox()
b.get(url)

#função que preenche
def preenche(form):
    """dentro do parametro coloque o nome do formularia a ser preenchido e ele fará o resto"""
    # elementos:
    nome = f'.form-{form} input[name=nome]'
    senha = f'.form-{form} input[name=senha]'
    submit = f'.form-{form} input[name={form}]'
    #preenche nome
    nome = b.find_element(By.CSS_SELECTOR, nome)
    nome.send_keys('Aqui :D')
    #preenche senha
    senha = b.find_element(By.CSS_SELECTOR, senha)
    senha.send_keys('senhaqqr')
    #envia form
    submit = b.find_element(By.CSS_SELECTOR, submit)
    submit.click()

# quais formularios eu tenho e chamando a função
forms = ['l0c0', 'l0c1', 'l1c0', 'l1c1']
for form in forms:
    preenche(form)