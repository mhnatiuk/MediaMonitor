from celery import Celery
from subprocess import call


import sys, os
sys.path.append("/home/mh/MediaMonitor")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MediaMonitor.settings")
from monitor import models

from statsspider import spider

app = Celery('tasks', broker='amqp://guest@localhost//')
app.config_from_object("celeryconfig")

"""
This are just wrappers for Celery to use as tasks
"""


@app.task
def crawl():
    call_agora_crawler()
    call_onet_crawler()


@app.task
def get_and_update_stats():
    get_stats()
    populate_stats() 

def call_agora_crawler():
    call(["scrapy", "crawl", "agora"])

def call_onet_crawler():
    call(["scrapy", "crawl", "onet"])


def get_stats():
    """
    spider.get_facebook_and_twitter_stats is a function that calls APIs of Facebook
    and Twitter and scraps link popularity data from those sites.
    """
    spider.get_facebook_and_twitter_stats()

def populate_stats():
    """
    Scrapped data from Agora and Onet sites contain OpenGraph tags. OpenGraph allows
    to filter gathered data by content type (currently we are interesed only in "article" type),
    see when the article was updated and other useful data. 
    """
    all_links = models.Link.objects.filter(link_type=None)
    for link in all_links:
        link.populate_og_stats()
