# Combinadores
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_06.html'

b = webdriver.Firefox()
b.get(url)

"""
Irmãos adjacentes(A + B)
Geral de irmãos(A ~ B)
Filhos (A > B)
Descendentes (A  B)
"""