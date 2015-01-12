from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^linkstats/(?P<link_id>\d+)$', views.get_stats, name='get_stats'),
)