from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.conf import settings

from djumblelog.models import Entry

class LatestEntries(Feed):
    title = "Tumblelog"
    link = 'http://%s' % Site.objects.get(pk=settings.SITE_ID).domain
    description = "Latest Tumblelog entries"
    description_template = 'djumblelog/feed_latest_description.html'

    def items(self):
        return Entry.objects.all()[:10]

class LatestEntriesByType(Feed):
    description_template = 'djumblelog/feed_type_description.html'
    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist
        try:
            ctype = ContentType.objects.get(name=bits[0])
        except ContentType.DoesNotExist:
            raise FeedDoesNotExist
        return Entry.objects.filter(content_type=ctype)

    def title(self, obj):
        return "Tumblelog: Entires for %s" % obj.get().content_type.model_class().__name__

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return 'http://%s' % Site.objects.get(pk=settings.SITE_ID).domain
    
    def description(self, obj):
        return "Tumblelog: Entires for %s" % obj.get().content_type
    
    def items(self, obj):
        return obj[:10]
