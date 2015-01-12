import json
import ipdb
from lxml import etree
import urllib
from time import time, sleep
import datetime
import facebook
from django.utils import timezone
import pytz
from mysettings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET

class StatsGetter(object):
    def __init__(self, linklist, lag=1):
        """ linklist_file : file/buffer/list with list of links to check separated by newline
        """
        assert type(linklist) in (file, buffer, list), "Excepted file, buffer or list"
        self.__configure_time()
        self.__setup_fb()
        self.TWITTER_API = 'http://urls.api.twitter.com/1/urls/count.json?url='
        self.link_count = 0
        self.lag = lag
        
        if type(linklist) == (file or buffer):
            self.linklist = [link.strip() for link in open(linklist_file, "r").readlines()]
        else: #list
            self.linklist = linklist
        self.stats = self.get_stats_for_links()
        
    
        
    def __configure_time(self):
        self.tzname = "Europe/Warsaw"
        timezone.activate(pytz.timezone(self.tzname))
        self.tz  = pytz.timezone("Europe/Warsaw")
    def __setup_fb(self):
        self.fb_app_token = facebook.get_app_access_token(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
        self.graph = facebook.GraphAPI(self.fb_app_token, version="2.1")
        self.rest_url = "http://api.facebook.com/restserver.php?method=links.getStats&urls="
        
    def get_rest_url(self):
        return self.rest_url
    
    def get_fb_api21_stats(self,link):
        #response = urllib.urlopen(self.FB_API + link)
        #ipdb.set_trace()
        if self.link_count % 50 == 0:
            sleep(self.lag)
        try:
            return self.graph.get_object(link)
        except facebook.GraphAPIError:
            return {}
        except UnicodeError:
            return {}
    
    def get_fb_rest_stats(self, link):
        if self.link_count % 50 == 0:
            sleep(self.lag)
        try:
            response = urllib.urlopen( self.get_rest_url() + link )
        except UnicodeError:
            return {}
        tree = etree.parse(response)
        root = tree.getroot()
        link_stat = root.getchildren()[0]
        stats_dict = dict()
        for child in link_stat.getchildren():
            stats_dict[ child.tag ] = child.text    
        return stats_dict
    """
    def get_sharedcount(self, links):
        sharedcount_api_key = "0d871aa187fd3a843fa894796702b59215b1ed8a"
        ipdb.set_trace()
        
        data = urllib.urlencode("\n".join(links))
        req =urllib2.Request("https://free.sharedcount.com/bulk?apikey=:" + sharedcount_api_key, data)
        response = urllib2.urlopen(req)
        ack = json.loads(response.read())
        bulk_id = ack['bulk_id']
        sleep(1)
        response = urllib2.urlopen( ("https://free.sharedcount.com/bulk?apikey=:%s&bulk_id=:%s") % (sharedcount_api_key, bulk_id))
        stats = json.dumps(response.read())
        return stats
    """    
    def get_twitter_stats(self, link):
        if self.link_count % 50 == 0:
            sleep(self.lag)
        try:
            response = urllib.urlopen(self.TWITTER_API + link)
        except UnicodeError:
            return {}
        try:
            json_obj = json.loads(response.read())
        except ValueError:
            return {}
        return json_obj
    
    def get_link(self, link):
        self.link_count +=1
        fb_21_response = self.get_fb_api21_stats(link)
        fb_REST_response = {} #self.get_fb_rest_stats(link)
        tw_response = self.get_twitter_stats(link)
        return {'fb_21' : fb_21_response, 'fb_rest': fb_REST_response, 'twitter' : tw_response, 'time' : datetime.datetime.now().replace(tzinfo=self.tz) }    
    def get_stats_for_links(self):
        return [self.get_link(link) for link in self.linklist ]
        #return self.get_sharedcount(self.linklist)
        
    def get_stats(self):
        return self.stats
    
    
    
    
        
