import ipdb
import urllib2
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from BeautifulSoup import BeautifulSoup, SoupStrainer

class LinkGetter(scrapy.Spider):
    def __init__(self, domain):
        """ domain_list: a list of domains to extract links from (must start with http://)
        """
        self.domain = domain
        
        self.scrapy = scrapy.Spider(self.domain)
        self.scrapy.allowed_domains = self.scrapy.name
        self.scrapy.start_urls = [ self.scrapy.name ]
        
        self.settings = get_project_settings()
        self.crawler = Crawler(settings)
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.crawler.configure()
        self.scrapy.crawl(spider)
        self.scrapy.start()
        log.start()
        reactor.run()
        
        self.links = []
        
    def parse(self, response):
        self.links.extend(LinkExtractor.extract_links(response))
        
    """    
    def run(self):
        self.__crawlLinks()
    def __recursiveUrl(self, url,depth):
        if depth == self.depth and url not in self.links:
            return url
        elif url in self.links:
            return None
        else:
            try:
                assert type(url) == unicode
                page=urllib2.urlopen(url)
            except ValueError:
                return url
            except urllib2.URLError:
                return url
            soup = BeautifulSoup(page.read())
            new_a_tags= soup.findAll('a')
            newlinks = [a_tag.get('href') for a_tag in new_a_tags]
            newlinks = [link for link in newlinks if link not in self.links]
            if len(newlinks) == 0:
                return url
            else:
                for newlink in newlinks:
                    if newlink not in self.links:
                        return self.__recursiveUrl(newlink.get('href'),depth+1)
                    else:
                        return None
    
    def __crawlLinks(self):
        page=urllib2.urlopen(self.domain)
        soup = BeautifulSoup(page.read())
        a_tags = soup.findAll('a')
        self.links = [a_tag.get('href') for a_tag in a_tags]
        for link in self.links:
            self.links.append(self.__recursiveUrl(link,0))
    def get_links(self):
        links_clean = [link for link in self.links if link is not None]
        return set(links_clean) # guarantee that links are unique
    
    """
    
if __name__ == '__main__':
    getter = LinkGetter('http://www.gazeta.pl')
    