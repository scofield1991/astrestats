from django.conf.urls import patterns, url
from stats import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^graph_data/$', views.graph_data, name='graph_data')
)
