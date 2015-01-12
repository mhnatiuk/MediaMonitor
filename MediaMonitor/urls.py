from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'monitor.views.index', name='index'),
     #url(r'^/index[/]?$', 'monitor.views.index', name='index'),
    url(r'^monitor/', include('monitor.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
