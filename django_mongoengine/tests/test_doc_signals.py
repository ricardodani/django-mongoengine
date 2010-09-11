from mongoengine import connect, fields
from unittest import TestCase
from mongoengine.queryset import DoesNotExist
from django.db.models import signals

from django_mongoengine.documents import Document

connect("django_mongoengine_testing")

class SimpleDocument(Document):
    name = fields.StringField()

class SignalTestCase(TestCase):
    fired_signals = {}
    
    def setUp(self):
        SimpleDocument(name="Jane Doe").save()
    
    def tearDown(self):
        SimpleDocument.drop_collection()
        
    def test_pre_save(self):
        def pre_save_simple_document(*args, **kwargs):
            self.fired_signals["pre_save"] = kwargs["instance"].id
        
        signals.pre_save.connect(pre_save_simple_document, sender=SimpleDocument)
        
        SimpleDocument(name="John Doe").save()
        
        self.assert_("pre_save" in self.fired_signals)
        self.assert_(self.fired_signals["pre_save"] is None)
    
    def test_post_save(self):
        def post_save_simple_document(*args, **kwargs):
            self.fired_signals["post_save"] = kwargs["instance"].id

        signals.post_save.connect(post_save_simple_document, sender=SimpleDocument)
        
        SimpleDocument(name="John Doe").save()
        
        self.assert_("post_save" in self.fired_signals)
        self.assert_(self.fired_signals["post_save"] is not None)
    
    def test_pre_delete(self):
        def pre_delete_simple_document(*args, **kwargs):
            self.fired_signals["pre_delete"] = SimpleDocument.objects.get(name="Jane Doe")
            
        signals.pre_delete.connect(pre_delete_simple_document, sender=SimpleDocument)

        SimpleDocument.objects.get(name="Jane Doe").delete()

        self.assert_("pre_delete" in self.fired_signals)
        self.assert_(self.fired_signals["pre_delete"] is not None)
        
    def test_post_delete(self):
        def post_delete_simple_document(*args, **kwargs):
            try:
                SimpleDocument.objects.get(name="Jane Doe")
            except DoesNotExist:
                self.fired_signals["post_delete"] = None
            else:
                self.fired_signals["post_delete"] = True

        signals.post_delete.connect(post_delete_simple_document, sender=SimpleDocument)

        SimpleDocument.objects.get(name="Jane Doe").delete()

        self.assert_("post_delete" in self.fired_signals)
        self.assert_(self.fired_signals["post_delete"] is None)