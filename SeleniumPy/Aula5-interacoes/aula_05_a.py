# Encontrando elementos por ID
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_a.html')

py = firefox.find_element(By.ID, 'python')

print(py.text)

firefox.quit()