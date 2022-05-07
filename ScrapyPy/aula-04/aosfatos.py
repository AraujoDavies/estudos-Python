import scrapy

class AosfatospageSpider(scrapy.Spider):
    name = 'aosfatospage'
    start_urls = ['http://www.aosfatos.org/']

    #essa função pega os links da aba "CHECAMOS" e chama a função categorias
    def parse(self, response):
        #Uma maneira interessante de debugar só uma parte do código -> import ipdb; ipdb.set_trace()
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]//@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link), # o link do site não é uma URL 'ex/example/aosfatos'
                callback=self.categorias # callback oq vem dps ?
            )

    # semelhante ao parse inicial, dessa vez pega cada card de noticia
    def categorias(self, response):
        news = response.css('a.entry-content::attr(href)').getall()
        for new in news:
            yield scrapy.Request(
                response.urljoin(new),
                callback=self.parse_new
            )
    
    # dentro do card de noticias pega as informações para criação do banco de dados
    def parse_new(self, response):
        title = response.css('article h1::text').get()
        # date vem: '5 de      \n   maio de      \n' porém com o split cria um array 
        # e o join faz a mágica ' 5 de maio de ...'
        date = ' '.join(response.css('.publish-date::text').get().split()) 
        quotes = # parei aqui 52m
        yield {
            'title': title,
            'date': date,
            'url': response.url
            }