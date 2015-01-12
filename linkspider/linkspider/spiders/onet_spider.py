import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from linkspider.items import OnetItem


class OnetSpider(CrawlSpider):
    """
    This class inhertis methods from scrapy.contrib.spider.CrawlSpider and is a scrapy spider
    allowed_domains: a list of domains on wich crawling is allowed
    start_urls: a list of urls where to start scrapping
    """

    name = "onet"
    allowed_domains = ["onet.pl"]
    start_urls = ["http://www.onet.pl"]

#    xpaths = '''//a/@href'''
    rules = ( Rule(LinkExtractor(allow_domains = allowed_domains ) , callback="parse", follow=True), )
    def parse(self, response):
        """
        This function extracts url and its position on site
        """

        for nr, url in enumerate(response.xpath('//a/@href').extract()):
            item = OnetItem()
            item['url'] = url
            item['position'] = nr
            yield item
	    #yield scrapy.Request(url, callback=self.parse)

