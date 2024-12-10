from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ClodCrawlSpider(CrawlSpider):
    name = 'empreendedorismo_1.0'
    start_urls = ['https://sebrae.com.br/']

    rules = (
        Rule(LinkExtractor(allow='/pagina/\d+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        #Extração e salvamento
        titulo = response.css('strong::sbAccessibilityFontSize').get()
        subtitulos = response.css('h4::sbAccessibilityFontSize').getall()
        conteudo = response.css('p.sbAccessibilityFontSize').getall()

        yield {
            'url': response.url,
            'titulo': titulo,
            'subtitulos': subtitulos,
            'conteudo': ' '.jon(conteudo),
        }