from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^topictree/', include('myapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
