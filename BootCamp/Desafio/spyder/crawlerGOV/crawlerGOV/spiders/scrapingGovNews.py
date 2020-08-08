import scrapy

from crawlerGOV.items import ScrapergovItem

class ScrapinggovnewsSpider(scrapy.Spider):
    name = 'scrapingGovNews'
    
    #allowed_domains = ['https://www.gov.br/pt-br/noticias']
    #start_urls = ['http://https://www.gov.br/pt-br/noticias/']
    
    def __init__(self):
        self.start_urls = ['https://www.gov.br/pt-br/noticias/']  

    def parse(self, response):
        self.log('Acessando a URL: %s' % response.url)
        
        item = ScrapergovItem()
        
        item['titulo_pagina']  = response.css("title ::text").extract_first()
        item['url_pagina'] = response.url

        
        noticias = response.xpath("//div[@class='nitf-basic-tile tile-content']")
        count_noticias = 0
        
        for noticia in noticias:

            count_noticias += 1
            self.log('Notícias %s' % str(count_noticias))
                  
            assunto = noticia.xpath(".//p")
        
            item['assunto_noticia'] = ''.join(assunto.xpath('text()').get())
            
            tituloNoticia = noticia.xpath(".//h2//a")
            item['titulo_noticia'] = ''.join(tituloNoticia.xpath('text()').get())
            item['url_noticia'] = ''.join(tituloNoticia.xpath('@href').get())            

            yield item