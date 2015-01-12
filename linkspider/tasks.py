from celery import Celery
from subprocess import call


import sys, os
sys.path.append("/home/m/MediaMonitor")
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
    spider.get_facebook_and_twitter_stats()

def populate_stats():
    all_links = models.Link.objects.filter(link_type=None)
    for link in all_links:
        link.populate_og_stats()
