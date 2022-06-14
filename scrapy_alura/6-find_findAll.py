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
import pprint
# criando objeto Beautifulsoup:
soup = BeautifulSoup(html, "html.parser")
#################################################################################
#find & findall
soup.find('img') # primeira ocorrencia = soup.img
soup.find_all('img') == soup.findAll('img') == soup('img') # todas ocorrencias

# parametro limit
soup.find_all('img', limit=3) 

# pegando uma ocorrência específica
soup('img')[1]

# buscando por listas 
soup.findAll(['h1','h2','h3','h4','h5','h6'])

# buscando por conteudo dentro da tag
soup.find_all('p', text = 'Belo Horizonte - MG')

# buscando por atributo
soup.find_all('img', alt='Foto') 
soup.find_all('p', class_= 'txt-value') # class é uma palavra reservada do python

# buscando por argumentos do atributo
soup.findAll('p', {'class': 'txt-value'}) 

# obtendo todo texto de uma pagina
soup(text = True)