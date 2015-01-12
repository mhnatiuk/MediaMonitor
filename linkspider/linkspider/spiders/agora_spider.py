import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from linkspider.items import AgoraItem


class AgoraSpider(CrawlSpider):
    """
    This class inhertis methods from scrapy.contrib.spider.CrawlSpider and is a scrapy spider
    allowed_domains: a list of domains on wich crawling is allowed
    start_urls: a list of urls where to start scrapping
    """
    
    name = "agora"
    allowed_domains = ["gazeta.pl", "wyborcza.pl", "wyborcza.biz", "plotek.pl", "sport.pl", "moto.pl", "lula.pl", "edziecko.pl", "deser.pl",  "gazetapraca.pl", "gazetadom.pl", "domiporta.pl", "alert24.pl", "gazeta.tv", "agora.pl", "searchlab.pl", "adtaily.pl", "adplayer.pl", "payper.pl", "cityinfotv.pl", "tokfm.pl", "tuba.pl"]
    start_urls = ["http://www.gazeta.pl/","http://www.wyborcza.pl", "http://www.wyborcza.biz"]

#    xpaths = '''//a/@href'''
    rules = ( Rule(LinkExtractor(allow_domains = allowed_domains ) , callback="parse", follow=True), )
    def parse(self, response):
        """
        This function extracts url and its position on site
        """
        for nr, url in enumerate(response.xpath('//a/@href').extract()):
            item = AgoraItem()
            item['url'] = url
            item['position'] = nr
            yield item
	    #yield scrapy.Request(url, callback=self.parse)

