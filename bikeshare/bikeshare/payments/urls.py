from django.conf.urls import patterns, url

urlpatterns = patterns('bikeshare.payments.views',
    url(r'^get_token/$', 'get_token', name='get_token'),
)
