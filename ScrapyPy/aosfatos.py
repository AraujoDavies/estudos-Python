import scrapy

class AosfatospageSpider(scrapy.Spider):
    name = 'aosfatospage'
    start_urls = ['http://www.aosfatos.org/']

    #essa função pega os links da aba "CHECAMOS"
    def parse(self, response):
        #Uma maneira interessante de debugar só uma parte do código -> import ipdb; ipdb.set_trace()
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]//@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.categorias
            )

    def categorias(self, response):
        # parei no minuto 43
        pass
        