from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^$', 'main'),
    url(r'^login/.$', 'test'),
    url(r'^signup/.$', 'test'),
    url(r'^question/\d+/.$', 'question', name='question'),
    url(r'^ask/.$', 'test'),
    url(r'^popular/.$', 'popular'),
    url(r'^new/.$', 'test')
)