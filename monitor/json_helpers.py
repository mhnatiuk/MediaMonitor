import json
import ipdb
def get_index_object(link_obj):
    index = {}
    index['id'] = link_obj.id
    index['uri'] = link_obj.uri
    try:
        fb_21 = json.loads(link_obj.linkstats_set.all()[0].fb_21)
    except IndexError: # not stats
        index['error'] = "No stats yet for this link"
        return index
    
    #ipdb.set_trace()
    try:
        index['title'] = fb_21['og_object']['title'].encode('utf8')
    except KeyError:
        index['title'] = "<i>No OG obj.</i>"
    try:
        index['og_type'] = fb_21['og_object']['type']
    except KeyError:
        index['og_type'] =  "<i>No OG obj.</i>"
    try:
        index['updated_time'] = fb_21['og_object']['updated_time']
    except KeyError:
        index['updated_time'] = "<i>No OG obj.</i>"
    
    return index

def get_stats(link_obj):
    link_stats_by_time = link_obj.linkstats_set.order_by("time")
    obj_list = []
    for stat in link_stats_by_time:
        fb21 = json.loads(stat.fb_21)
        #fb_rest = json.loads(stat.fb_rest)
        twitter = json.loads(stat.twitter)
        obj = {}
        obj['uri'] = stat.link_uri
        obj['time'] = stat.time
        obj['share_count'] = fb21['share']['share_count']
        obj['comment_count'] = fb21['share']['comment_count']
	if twitter.has_key('count'):
	    obj['twitter']  = twitter['count']
	else:
	    obj['twitter'] = '{}'	
        #ipdb.set_trace()
        #obj['fb_rest_comment_count'] = fb_rest['{http://api.facebook.com/1.0/}comment_count']
        #obj['fb_rest_share_count'] = fb_rest['{http://api.facebook.com/1.0/}share_count']
        #obj['fb_rest_like_count'] = fb_rest['{http://api.facebook.com/1.0/}like_count']
        #obj['fb_rest_total_count'] = fb_rest['{http://api.facebook.com/1.0/}total_count']
        obj_list.append(obj)
    return obj_list
        
