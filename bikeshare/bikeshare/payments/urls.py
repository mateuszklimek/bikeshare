from django.conf.urls import patterns, url

urlpatterns = patterns('bikeshare.payments.views',
    url(r'^get_token/$', 'get_token', name='get_token'),
    url(r'^new_bike/$', 'new_bike', name='new_bike'),

    url(r'^test/', 'test', name='test'),

)
