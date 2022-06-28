from operator import contains
import scrapy

class MlSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ['https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page=1']

    def parse(self, response):
        for produto in response.xpath('//ol[@class="items_container"]//li'):
            yield {
                'titulo': produto.xpath('.//p[@class="promotion-item__title"]/text()').get(),
                'preco': produto.xpath('.//span[@class="promotion-item__price"]//text()').getall(),
                'link': produto.xpath('.//a/@href').get()
            }
            
            next_page = response.xpath('//a[contains(@title, "Próxima")]/@href').get()
            if '&page' in next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
    
    #classe ok = andes-pagination__button--next
    #classe fim = andes-pagination__button--next andes-pagination__button--disabled