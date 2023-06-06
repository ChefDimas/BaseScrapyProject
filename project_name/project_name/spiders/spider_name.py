import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"
    allowed_domains = ["www.example.com"]
    start_urls = ["https://www.example.com"]

    def parse(self, response):
        pass
