import scrapy


class SpiderbraeSpider(scrapy.Spider):
    name = "spiderbrae"
    allowed_domains = ["sebrae.com.br"]
    start_urls = ["https://sebrae.com.br/"]

    def parse(self, response):
        pass
