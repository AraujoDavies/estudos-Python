from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li>Abertura</li>
                <li>10%</li>
                <li>11%</li>
                <li>10.5%</li>
                <li>9%</li>
                <li>Fechamento</li>
            </ul>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')

# exercise pop, how to delete "li" without number ? 
# como eliminar as Li sem conteudo numérico ?


















# gabarito abaixo
# awnser above























# ...















lis = soup.findAll('li')
lis.pop()
lis.pop(0)
lis