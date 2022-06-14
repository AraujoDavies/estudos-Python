# para obter o html de uma página será usado o URLLIB
from urllib.request import Request, urlopen
# tratar erros
# se for usar ambos é obrigatorio colocar a tratativa do HTTPError primeiro
from urllib.error import URLError, HTTPError 

url1 = 'https://alura-site-scraping.herokuapp.com/hello-world.php'
url2 = 'https://www.alura.com.br'

# response = urlopen(url1) 
# aqui obtemos o HTML da url1 sem problemas, porém a url2 vai dar o erro => 403: Forbidden

# Para resolver...
# pegar user-agent do navegador
resolve403 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

# tratativas de erros com o try
try:
    # Request informando User-Agent
    req = Request(url2, headers = resolve403)
    response = urlopen(req)
    print(response.read())

except HTTPError as e: # se erro de requisição ele printa
    print(e.status, e.reason)
except URLError as e: # se erro de URL ele printa getaddrinfo failed
    print(e.reason)