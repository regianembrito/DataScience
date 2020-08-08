import scrapy

from crawlerGOV.items import CrawlergovItem

class CrawlinggovnewsSpider(scrapy.Spider):
    
    name = 'crawlingGovNews'
    #allowed_domains = ['https://www.gov.br/pt-br/noticias']
    
    start_urls = ['https://www.gov.br/pt-br/noticias/']

    def parse(self, response):
        self.log('Acessando a URL: %s' % response.url)
        
        noticias = response.xpath("//div[@class='nitf-basic-tile tile-content']")
        
        item = CrawlergovItem()
        for noticia in noticias:
            
            tituloNoticia = noticia.xpath(".//h2//a")
            url = tituloNoticia.xpath('@href').extract_first()
            self.log('Notícia %s' % tituloNoticia.xpath('text()').extract_first())            
    
            yield response.follow(url, self.parse_noticia)
            
        item['titulo_pagina']  = response.css("title ::text").extract_first()
        item['url_pagina'] = response.url
        #item['categoria'] = 'HOME'
        
        yield item
        
       
    def parse_noticia(self, response):
        self.log('Acessando a URL: %s' % response.url)
        
        item = CrawlergovItem()
        
        item['titulo_pagina']  = response.css("title ::text").extract_first()
        item['url_pagina'] = response.url
        
        article = response.xpath("//article")
        
        item['assunto_noticia'] = article.xpath(".//p[@class='nitfSubtitle']/text()").extract_first()
        item['titulo_noticia'] = article.xpath(".//h1[@class='documentFirstHeading']/text()").extract_first()
        item['subtitulo_noticia'] = article.xpath(".//div[@class='documentDescription']/text()").extract_first()
        #item['data_publicacao'] = article.xpath(".//div[@class='documentDescription']/text()").extract_first()
        
        item['texto_noticia'] = ''.join(article.xpath(".//div[@id='parent-fieldname-text']/div").extract())
        
        item['autor_noticia'] = article.xpath(".//span[@class='discreet']/text()").extract_first()
        item['categoria_noticia'] = article.xpath(".//span[@id='form-widgets-categoria']/div/a/text()").extract_first()
        item['tags_noticia'] = ''.join(response.xpath("//div[@id='category']/a/text()").extract())
        
        yield item 