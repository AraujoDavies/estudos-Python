from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Texto de conteúdo A</p>
                <div id="container-a-1">
                    <h1>Título A.1</h1>
                    <h2 class="ref-a">Sub título A.1</h2>
                    <p>Texto de conteúdo A.1</p>
                </div>
            </div>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')

# Conhecendo 2 parametros do get_text 
soup.get_text(separator=' || ', strip=True).split(' || ')