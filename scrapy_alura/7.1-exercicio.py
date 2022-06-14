from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Curso de</p>
                <p>Web</p>
                <p>Scraping</p>
                <p>com Python</p>
            </div>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')

# obtenha o resultado a seguir: [<p>Web</p>, <p>Scraping</p>]


















# Gabarito...























# VOCÊ JÁ TENTOU RESOLVER ?




























# BELEZA, O PRÓXIMO É O GABARITO

























soup.find('p').findAllNext(limit=2)