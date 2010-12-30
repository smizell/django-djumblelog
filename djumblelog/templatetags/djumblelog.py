from django import template
from django.conf import settings
from django.db import models

register = template.Library()

def show_djumblelog(context, num=10):
    """
    Templatetag for displaying entries from the djumblelog. This
    templatetag includes the `djumblelog/object_list.html` file, which
    is included in the djumblelog app or can be replaced by creating that
    file anywhere in your template directory path.
    
    Usage:
    {% load djumblelog %}
    {% show_djumblelog %}
    
    By default, it shows the last 10 entries, but that can be changed
    when the templatetag is called.
    
    Example:
    {% show_djumblelog 5 %}
    """
    entry_model = models.get_model("djumblelog", "entry")
    entries = entry_model.objects.all()[:num]
    return {
        'object_list': entries
    }
register.inclusion_tag("djumblelog/object_list.html", takes_context=True)(show_djumblelog)
