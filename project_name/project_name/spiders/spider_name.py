import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        alert = response.xpath('//*[@id="default"]/div/div/div/div/div[1]/h1').get()
        yield {'alert': alert}
