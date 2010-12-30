from django.views.generic import list_detail
from django.contrib.contenttypes.models import ContentType

from djumblelog.models import Entry

def index(request, queryset=Entry.objects.all(), model_name=None,
            paginate_by=15, template_name="djumblelog/object_list.html"):
    """
    Wrapper around generic view object_list
    Generic list of objects.

    Templates: ``djumblelog/object_list.html``
    Context:
        object_list
            list of objects
        is_paginated
            are the results paginated?
        results_per_page
            number of objects per page (if paginated)
        has_next
            is there a next page?
        has_previous
            is there a prev page?
        page
            the current page
        next
            the next page
        previous
            the previous page
        pages
            number of pages, total
        hits
            number of objects, total
        last_on_page
            the result number of the last of object in the
            object_list (1-indexed)
        first_on_page
            the result number of the first object in the
            object_list (1-indexed)
        page_range:
            A list of the page numbers (1-indexed).
    """
    if model_name:
        ctype = ContentType.objects.get_for_model(model_name)
        queryset = Entry.objects.filter(content_type=ctype)
    params = {
        'queryset': queryset,
        'paginate_by': paginate_by,
        'template_name': template_name,
    }
    return list_detail.object_list(request, **params)