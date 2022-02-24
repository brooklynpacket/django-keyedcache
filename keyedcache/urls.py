"""
URLConf for Caching app
"""
from __future__ import unicode_literals
from django.urls import path

from . import views

urlpatterns = [
    path('', views.stats_page, {}, 'keyedcache_stats'),
    path('view/', views.view_page, {}, 'keyedcache_view'),
    path('delete/', views.delete_page, {}, 'keyedcache_delete'),
]
