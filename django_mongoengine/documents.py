from mongoengine import Document as MEDocument
from django.db.models import signals

class Document(MEDocument):
    def save(self, safe=True, force_insert=False):
        signals.pre_save.send(sender=self.__class__, instance=self)
        before = '_id' in self and self['_id'] or None
        super(Document, self).save(safe=safe, force_insert=force_insert)
        after = '_id' in self and self['_id'] or None
        signals.post_save.send(sender=self.__class__, instance=self,
                               created=bool(not before and after))

    def delete(self, safe=False):
        signals.pre_delete.send(sender=self.__class__, instance=self)
        super(Document, self).delete(safe=safe)
        signals.post_delete.send(sender=self.__class__, instance=self)