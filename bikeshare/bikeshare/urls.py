from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bikeshare.views.home', name='home'),
    url(r'^payments/', include('bikeshare.payments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
