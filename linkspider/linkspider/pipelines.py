# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys, os

sys.path.append("/home/mh/MediaMonitor")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MediaMonitor.settings")

from scrapy.exceptions import DropItem
from monitor import models
from datetime import datetime
from datetime import timedelta
from django.utils.timezone import *
import pytz
import ipdb
import django




class AgoraspiderPipeline(object):
    """
    In scrapy, a pipeline is a class that acts as middleware for all scrapped items.
    Here, this class checks whether this item has been seen before by the spider,
    and if not, saves this item to DB adding a time-to-live for this link.
    """
    def __init__(self):
        self.urls_seen = set()
    	django.setup()
    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(item['url'])
	    link = models.Link()
	    
	    link.url = item['url']
	    link.link_position_within = item['link_position_within']
	    link.link_number_on_site = item['link_number_on_site']
	    link.link_id = item['link_id']
	    link.source_url = item['source_url']
	    link.added_time = now().replace(tzinfo=get_current_timezone()) 
	    link.ttl = now().replace(tzinfo=get_current_timezone())  + timedelta(days=30)
	    link.source_url = item['source_url']
	    
	    try:
		    link.save()
	    except models.LinkNotUnique:
    		pass
        return item

"""
    url = scrapy.Field()
    link_number_on_site = scrapy.Field()
    link_id = scrapy.Field()
    source_url = scrapy.Field()
    link_position_within = scrapy.Field()
"""

class OnetspiderPipeline(AgoraspiderPipeline):
    pass

