from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webooks.views.home', name='home'),
    # url(r'^webooks/', include('webooks.foo.urls')),

    url(r'^', include("webooks.urls.urls")),
    url(r'^api/v0/', include("webooks.apis.urls")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
