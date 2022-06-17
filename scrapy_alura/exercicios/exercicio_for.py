from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="container-a">
                <h1>Curso de Web Scraping</h1>
                <h3>Treinamento Alura</h3>
                <p class="main descr">Curso para ensinar técnicas de coleta de dados na web.</p>
            </div>
            <div id="tools">
                <p class="main lib-a">BeautifulSoup</p>
                <p class="libs">findAll()</p>
                <p class="libs">getText()</p>
                <p class="main lib-b">urllib.request</p>
                <p class="libs">urlopen()</p>
                <p class="main lib-c">pandas</p>
                <p class="libs">DataFrame()</p>
            </div>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')


# obter a saída:
# BeautifulSoup
# urllib.request
# pandas





# GABARITO ABAIXO...





























for item in soup.find('div', id = 'tools').findAll('p', class_='main'):
    print(item.getText())
