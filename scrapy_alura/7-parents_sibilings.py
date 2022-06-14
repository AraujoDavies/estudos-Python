from bs4 import BeautifulSoup
from pprint import pprint

# criando uma função com esse tratamento de html que facilitará para o BS4:
def tratar_html(input):
    return " ".join(input.split()).replace('> <', '><')

html = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Texto de conteúdo A</p>
            </div>
            <div id="container-b">
                <h1>Título B</h1>
                <h2 class="ref-b">Sub título B</h2> 
                <p>Texto de conteúdo B</p>
            </div>
        </body>
    </html>
"""

html = tratar_html(html)
soup = BeautifulSoup(html, 'html.parser')

#parents
soup.find('h2').find_parent() # retorna o primeiro pai
soup.find('h2').find_parent('body') # retorna o pai q eu especifiquei
soup.find('h2').find_parents() # mostra uma list c/ todos os pais :D

# parent de todos itens da lista
soup.find_all('h2')
for item in soup.find_all('h2'):
    pprint(item.find_parent())

# siblings - irmão, tags na mesma hierarquia
soup.find('h2').findNextSibling() # encontrara o proximo irmão
soup.find('h2').findPreviousSibling() # encontrará o irmão acima

soup.find('h1').findNextSiblings() # vai retornar os irmaos q estão abaixo dentro da mesma tag
soup.find('p').findPreviousSiblings() # vai retornar os irmão acima dentro da msm tag

# Next & Previous
soup.find('p').findNext() # encontrará a próxima tag
soup.find('h1').findPrevious() # encontrará a tag anterior
soup.find('h2').findAllNext() # retorna todas as tag abaixo do primeiro h2
soup.find('h2').findAllPrevious() # Sem sentido mas vale o teste :D