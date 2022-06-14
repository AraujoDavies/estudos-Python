from urllib.request import Request, urlopen

# função extra q auxilia BS4
def tratar_html(i):
    return " ".join(i.split()).replace('> <', '><')
# request e response do html
url = 'https://alura-site-scraping.herokuapp.com/index.php'
response = urlopen(url)
input = response.read()
# transforma em string 
input = input.decode('utf-8')
# html da pagina
html = tratar_html(input)

from bs4 import BeautifulSoup
# criando objeto Beautifulsoup:
soup = BeautifulSoup(html, "html.parser")
# ACESSANDO ATRIBUTOS DE UMA TAG
soup.img.attrs
soup.img.attrs.keys()
soup.img.attrs.values()
soup.img['src'] = soup.img.get('src')