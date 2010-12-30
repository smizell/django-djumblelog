from django.conf.urls.defaults import *

from djumblelog.feeds import LatestEntries, LatestEntriesByType

feeds = {
    'latest': LatestEntries,
    'type': LatestEntriesByType,
}

urlpatterns = patterns('',
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    url(r'^$', 'djumblelog.views.index', name="djumblelog_index"),
)
