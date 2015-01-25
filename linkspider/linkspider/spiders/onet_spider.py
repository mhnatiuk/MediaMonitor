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
        This function takes HTTPresponse object and extracts following info:
        1. url  - target address
        2. link_id - id given to this link. On GAZETA.pl site id is used in a strange way (as class should be used, i.e in the non-unique way)
        3. link_position_within - link position within it's link_id
        4. nr - number of the url as appeared in html source code
        5. source_url - url of the site with this link
        This function returns linkspider.items.AgoraItem instance.
        """
        articles = response.xpath("//article")
        urls_postition= defaultdict(list()) # link_positions_within_id
        
        for article in articles:
            section_name = article.xpath('@data-section').extract()
            urls_in_section = article.xpath(".//a").xpath("@href").re(r'^http.*')
            for nr, url in enumerate(urls_in_section):
                item = OnetItem()
                
                urls_position[section_name].append(url)
                
                item['url'] = url
                item['link_number_on_site'] = nr
                item['link_id'] = section_name
                item['source_url'] = response.url
                item['link_position_within'] = len( urls_position[ section_name ] ) # our item will always be last
                assert (item['link_position_within']-1) #but let's test that assumption
                yield item