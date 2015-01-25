# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AgoraItem(scrapy.Item):
    """
        This class is a holder for a unit of scrapped data: i.e. an URI and URI'S position on site
    """
    url = scrapy.Field()
    link_number_on_site = scrapy.Field()
    link_id = scrapy.Field()
    source_url = scrapy.Field()
    link_position_within = scrapy.Field()
    

class OnetItem(AgoraItem):
    """
        This class is a holder for a unit of scrapped data: i.e. an URI and URI'S position on site
    """
    pass
