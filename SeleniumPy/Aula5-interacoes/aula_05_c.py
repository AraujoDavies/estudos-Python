# Preenchendo Formulário e submetendo
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_c.html')

def melhor_filme(browser, filme, email, telefone):
    firefox.find_element(By.NAME, 'filme').send_keys(filme)
    firefox.find_element(By.NAME, 'email').send_keys(email)
    firefox.find_element(By.NAME, 'telefone').send_keys(telefone)
    firefox.find_element(By.NAME, 'enviar').click()

melhor_filme(firefox, 'VENOM', 'XUXUXU@xuxu.XU', '(019)987654321')

firefox.quit()

#parei no FORM (1:04)