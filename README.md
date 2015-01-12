# MediaMonitor
Monitoring tool for Polish news sites articles popularity in social media.

Prerequisites:
* django
* scrapy
* celery


Roadmap:
MediaMonitor/ : django project folder with all core settings for django
linkspider/ : tools for scrapping links from sites
  linkspider/ : scrapy application for crawling Agora and Onet
    items.py : defines what information from each link is to be processed further
    pipelines.py : defines functions to process those items
    settings.py : scrapy settings: set log level, user agent and pipelines (see above)
    spiders/
      agora_spider.py : crawler defintion
      onet_spider.py : crawler defintion
    
monitor/ : django app: contains :
  views.py -  how to display the data
  models.py - Database models of links and stats: writing, reading, updating links and stats
  lib/share_getter.py - a core library for getting sharing statistics from FB and TW
  templates/ - templates for displaying the data
statspider/ : spider for scrapping popularity stats from social media sites
  spider.py: core script for getting the data (using monitor/lib/share_getter.py)
  
  

