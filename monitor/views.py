from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import models
import json_helpers
import ipdb

def index(request):
    #link_list = models.Link.objects.all()
    
    page = request.GET.get('page')
    articles =  models.Link.objects.filter(link_type = 'article').order_by('-created_at');
    
    paginator = Paginator(articles, 50)
    try:
        index_entries_paged = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        index_entries_paged = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        index_entries_paged = paginator.page(paginator.num_pages)
    
    
    return render(request, "links/index.html", {'index' : index_entries_paged})

def get_stats(request, link_id):
    link = get_object_or_404(models.Link, pk=link_id)
    if request.META.has_key('HTTP_REFERER'):
        referer = request.META['HTTP_REFERER']
    else:
        referer = "#"
    stats = json_helpers.get_stats(link)
    return render(request, "stats/show.html", {'uri' : link.uri,
                                               'HTTP_REFERER': referer ,
                                               'updated_time' : link.updated_time ,
                                               'created_at' : link.created_at,
                                               'col_names' : stats[0].keys(),
                                               'stats' : stats})

# Create your views here.
