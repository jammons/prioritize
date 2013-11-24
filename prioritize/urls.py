""" Default urlconf for prioritize """

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'prioritize.views.home', name='home'),
    url(r'^set/(?P<set_id>[-\w]+)/$', 'prioritize.views.set_home', name='set_home'),
    url(r'^set/(?P<set_id>[-\w]+)/compare$', 'prioritize.views.compare', name='compare'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
