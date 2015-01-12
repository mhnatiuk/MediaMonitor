import sys
import ipdb
import os

sys.path.append("/home/m/MediaMonitor")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MediaMonitor.settings")

from monitor.lib import share_getter
from monitor.models import Link, LinkStats
from django.utils import timezone
import json
import django
django.setup()
import datetime


def get_all_valid_links():
    all_links = Link.objects.all()
    valid_links = [ link for link in all_links if link.ttl > timezone.now() ]
    return valid_links

def get_facebook_and_twitter_stats():
    ipdb.set_trace()
    django.setup()
    json_en = json.JSONEncoder()
    links = get_all_valid_links()
    stats_getter = share_getter.StatsGetter([link.uri for link in links], lag=1)
    stats  = stats_getter.get_stats()
    for i, link in enumerate(links):
        ls = LinkStats()
        ls.link_id = link.id
        ls.link_uri = link.uri
	
        ls.time = stats[i]['time']
        ls.fb_21 = json_en.encode(stats[i]['fb_21'])
	ls.fb_rest = '{}' #json_en.encode(stats[i]['fb_rest'])
	ls.twitter = json_en.encode(stats[i]['twitter'])
	ls.save()


if __name__ == "__main__":
    get_facebook_and_twitter_stats()        
