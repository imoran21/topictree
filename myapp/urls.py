from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.home', name='home'),
	url(r'^slug/(?P<slug>[-\w]+)/$', 'myapp.views.slug', name='slugview'),


)
