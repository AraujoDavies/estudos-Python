from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>Fotos</h1>
            <div>
                <img alt="Foto" src="https://caelum-online-public.s3.amazonaws.com/1381-scraping/01/img-cars/mercedes-benz-slr/mercedes-benz-slr-2925433__340.jpg">
                <img alt="Foto" src="https://caelum-online-public.s3.amazonaws.com/1381-scraping/01/img-cars/vwbeetle/vwbeetle-836065__340.jpg">
                <img alt="Foto" src="https://caelum-online-public.s3.amazonaws.com/1381-scraping/01/img-cars/porsche-911-gt2rs/porsche-911-gt2rs-3076518__340.jpg">
            </div>
        </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')

#pegando links 

imgs = soup.findAll('img')

for img in imgs:
    print(img.get('src'))