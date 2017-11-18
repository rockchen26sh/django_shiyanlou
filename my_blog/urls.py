"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views as art_views
from img_db import views as img_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', art_views.index),
    url(r'^test/$', art_views.test),
    url(r'^(?P<id>\d+)/$',art_views.detail, name='detail'),
    url(r'^archives/$',art_views.archives, name='archives'),
    url(r'^aboutme/$',art_views.about_me, name='about_me'),
	url(r'^tag(?P<tag>\w+)/$',art_views.search_tag, name='search_tag'),
	url(r'^search/$',art_views.blog_search, name='search'),
    url(r'^upload$',img_views.uploadImg,name = 'uploadImg'),
    url(r'^show$',img_views.showImg, name = 'showImg')
]
