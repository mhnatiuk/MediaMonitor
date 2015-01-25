import scrapy

from collections import defaultdict
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from linkspider.items import AgoraItem

import ipdb


class AgoraSpider(CrawlSpider):
    """
    This class inhertis methods from scrapy.contrib.spider.CrawlSpider and is a scrapy spider
    allowed_domains: a list of domains on wich crawling is allowed
    start_urls: a list of urls where to start scrapping
    """
    name = "agora"
    allowed_domains = ["gazeta.pl", "wyborcza.pl", "wyborcza.biz", "plotek.pl", "sport.pl", "moto.pl", "lula.pl", "edziecko.pl", "deser.pl",  "gazetapraca.pl", "gazetadom.pl", "domiporta.pl", "alert24.pl", "gazeta.tv", "agora.pl", "searchlab.pl", "tokfm.pl", "tuba.pl"]
    start_urls = ["http://www.gazeta.pl/","http://www.wyborcza.pl", "http://www.wyborcza.biz"]

#    xpaths = '''//a/@href'''
    rules = ( Rule(LinkExtractor(allow_domains = allowed_domains ) , callback="parse", follow=True), )

    def parse(self, response):
        """
        This function takes HTTPresponse object and extracts following info:
	1. url  - target address
	2. link_id - id given to this link. On GAZETA.pl site id is used in a strange way (as class should be used, i.e in the non-unique way)
	3. link_position_within - link position within it's link_id
	4. nr - number of the url as appeared in html source code
	5. source_url - url of the site with this link
	This function returns linkspider.items.AgoraItem instance.
        """
        all_urls = response.xpath('//a')

	urls_postition= defaultdict(list()) # link_positions_within_id 

        for nr, link in enumerate(all_urls):
	    
	    item = AgoraItem()
	    
	    # extraction by using scrapy lxml selectors
	    
            url = link.xpath('@href').extract() # select url 
            link_id = link.xpath('@id').extract() # select id 
	    urls_postition[link_id].append(url) # append url to know the order in which it appeared within the class (link_id)
	    
            
            ipdb.set_trace() # DO NOT DEPLOY
	    
            item['url'] = url # 
            item['link_number_on_site'] = nr
	    item['link_id'] = link_id
            item['source_url'] = response.url
	    item['link_position_within'] = len( urls_position[ link_id ] ) # our item will always be last
	    assert (item['link_position_within']-1) #but let's test that assumption
            yield item
	    #yield scrapy.Request(url, callback=self.parse)

    
    
    
    
    

