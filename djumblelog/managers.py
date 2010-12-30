from django.db import models
from django.contrib.contenttypes.models import ContentType

class EntryManager(models.Manager):
    """ Custom manager for Entry model """
        
    def get_for_model(self, app_label, model, order_by='-created_at'):
        try:
            content_type = ContentType.objects.get(app_label=app_label, model=model)
            return self.get_query_set().filter(content_type=content_type).order_by(order_by)
        except (ContentType.DoesNotExist, Entry.DoesNotExist):
            return None
            
    def get_for_object(self, instance):
        try:
            content_type = ContentType.objects.get_for_model(instance)
            entries = self.get_query_set().filter(content_type=content_type, object_id=instance.pk)
            return entries
        except ContentType.DoesNotExist:
            return None
            
    def delete_for_object(self, instance):
        entries = self.get_for_object(instance)
        if entries:
            entries.delete()
            return True
        return False
    
    def get_latest(self, app_label, model, order_by='-created_at', latest='created_at'):
        e = self.get_for_model(app_label, model, order_by='-created_at')
        if e:
            return e.latest(latest)
        return None
    
    def log(self, instance, created=False):
        ctype = ContentType.objects.get_for_model(instance)
        return Entry.objects.create(object_id=instance.pk, content_type=ctype)
