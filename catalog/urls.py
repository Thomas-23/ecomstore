from django.conf.urls import patterns, include, url
from catalog.views import IndexView, show_product, show_category
urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='catalog_home'),
	url(r'^category/(?P<slug>[-\w]+)/$', show_category, name='catalog_category'),
	url(r'^product/(?P<slug>[-\w]+)/$',show_product, name='catalog_product'),
)