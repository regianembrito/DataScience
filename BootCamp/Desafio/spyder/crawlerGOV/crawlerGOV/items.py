# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapergovItem(scrapy.Item):
    #Para cada página de notícia:
    url_pagina = scrapy.Field()
    titulo_pagina = scrapy.Field()

    #Para cada notícia da página:
    assunto_noticia = scrapy.Field()
    titulo_noticia = scrapy.Field()
    url_noticia = scrapy.Field()
    
class CrawlergovItem(scrapy.Item):
    #Para cada página de notícia:
    titulo_pagina = scrapy.Field()
    url_pagina = scrapy.Field()
    
    assunto_noticia = scrapy.Field()
    titulo_noticia = scrapy.Field()
    subtitulo_noticia = scrapy.Field()
    
    data_publicacao = scrapy.Field()
    texto_noticia = scrapy.Field()
    autor_noticia = scrapy.Field()
    
    categoria_noticia = scrapy.Field()
    
    tags_noticia = scrapy.Field()
