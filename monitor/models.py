from django.db import models
import datetime
import json
import ipdb
import pytz


class LinkNotUnique(Exception):
    """
    Exception thrown when link that you are trying to save is not unique. You should filter those link prior to saving.
    """
    def __init__(self, value=""):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Link(models.Model):
    """
    The main data class: stores links found on sites.
    
    """
    uri = models.CharField(max_length=1000, blank=False, unique=True, db_index=True)
    link_position_within = models.IntegerField(null=True)
    link_id = models.CharField(max_length=1000, null=True)
    link_number_on_site = models.IntegerField(null=True)
    source_url = models.CharField(max_length=1000, null=True)
    ttl = models.DateTimeField(blank=True, default=None)
    added_time =models.DateTimeField(blank=True, default=None)
    
    stats = models.TextField(blank=True, default="{}")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    """ from og: tags """
    link_type = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    title = models.CharField(max_length=1000, blank=True, null=True, db_index=True)
    updated_time = models.DateTimeField(blank=True, null=True, db_index=True)
    
    def save(self, *args, **kwargs):
        if self.id is not None or len( Link.objects.filter(uri=self.uri)) == 0:
            super(Link, self).save(*args, **kwargs)
        else:
            raise LinkNotUnique
    
    def populate_og_stats(self):
        """
        This function is used mostly to update Link with information gained from OG tags found on site
        """
        if len(self.linkstats_set.all()) > 0 :
            stat = self.linkstats_set.latest("time")
            fb_21 = json.loads(stat.fb_21)
            if fb_21.has_key('og_object'):
                try:
                    self.link_type = fb_21['og_object']['type']
                except KeyError:
                    self.link_type = None
                
                try:
                    self.title = fb_21['og_object']['title']
                except KeyError:
                    self.title = None
                
                try:
                    self.updated_time = datetime.datetime.strptime(fb_21['og_object']['updated_time'], "%Y-%m-%dT%H:%M:%S+0000").replace(tzinfo=pytz.utc)
                except KeyError:
                    self.updated_time = None
                    
                self.save()
                



class LinkStats(models.Model):
    """
    This model stores information about link statistics found via Facebook or Twitter link API
    """
    link = models.ForeignKey(Link, db_index=True)
    link_uri = models.CharField(max_length=1000, db_index=True)
    time = models.DateTimeField(db_index=True)
    fb_21 = models.TextField()
    fb_rest = models.TextField()
    twitter = models.TextField()





