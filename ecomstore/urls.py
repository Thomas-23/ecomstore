from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

from ecomstore import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#url(r'^catalog/$', 'ecomstore.views.catalog'),
	url(r'^', include('catalog.urls')),
	url(r'^catalog/$', 'preview.views.home'),
    url(r'^cart/', include('cart.urls')),
	
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	#urlpatterns += patterns('',
	#	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
	#	'document_root': settings.STATIC_ROOT,
	#	}),
	#)

handler404 = 'ecomstore.views.file_not_found_404'
	
