from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>Busca por veículos</h1>
            <div>
                <p id="info-search">Encontramos 1325 anúncios</p>
                <span class="info-pages">20 anúncios por página</span>
            </div>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')


# quantas paginas terá ?

import math

math.ceil(int(soup.p.getText().split()[1]) / int(soup.span.getText().split()[0]))
