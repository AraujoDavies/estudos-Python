# URL PARSE

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from time import sleep

browser = webdriver.Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

url_parseada = urlparse(browser.current_url)
# parseResult(schme, netloc, path, params, query, fragment)

sleep(5)

browser.refresh()