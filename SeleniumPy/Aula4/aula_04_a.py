# Busca aninhada => buscar os elementos A e printar
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

list_n_ordenada = browser.find_elements(By.TAG_NAME, 'ul') # 1

lis = list_n_ordenada[0].find_elements(By.TAG_NAME, 'li') #2

a = lis[0].find_element(By.TAG_NAME, 'a') #3

print(a.text)

browser.quit()
""" 
1. buscamos os elementos 'UL'
2. buscamos os elementos 'LI'
3. dentro de 'LI' pegamos o elemento 'A'

    ul
        li
            a
                texto
"""