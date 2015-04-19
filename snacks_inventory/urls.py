from django.conf.urls import patterns, url

from snacks_inventory import views

urlpatterns = patterns('snacks_inventory.views',
    url(r'^$', 'index', name='index'),
    url(r'^consumed/$', 'consumed_an_item', name='consumed_an_item'),
    url(r'^get_all_snacks/$', 'get_all_snacks', name='get_all_snacks'),
    url(r'^get_all_consumed_snacks/$', 'get_all_consumed_snacks', name='get_all_consumed_snacks'),

)