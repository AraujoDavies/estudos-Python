# ajudando Beautifulsoup a ler os dados da requisição
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

# retorna tipo bytes e o HTML vem mal formatado e cheio de caracteres esquisitos que podem confundir o BS
print(type(html)) 

# arrumando caracteres e transformar em tipo str
html = html.decode('utf-8') 

# split divide, como nao tem parametro ele vai criar uma list separando os espaços vazios
html.split()

# join vai juntar todos itens da lista separando pelo caracter q eu colocar nas aspas
" ".join(html.split())

# replace para tirar os espaços
" ".join(html.split()).replace('> <', '><') 
# ESTÁ PERFEITO!!!

# criando uma função com esse tratamento de html que facilitará para o BS4:
def tratar_html(input):
    return " ".join(input.split()).replace('> <', '><')

html = tratar_html(html)
print(html)