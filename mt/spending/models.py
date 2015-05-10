from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(blank=True, default=u'', max_length=255)
    sub_category = models.ForeignKey('self', blank=True, null=True)

class Note(models.Model):
    """
    Note about something, like a place you ate at
    """
    timestamp = models.DateTimeField('date taken')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = now()

class Spending(models.Model):
    timestamp = models.DateTimeField('date published')
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    description = models.TextField(blank=True, default=u'')
    receipt = models.ImageField(blank=True, null=True) #upload_to=None
    receipt_text = models.TextField(blank=True, default=u'') #Populated via OCR

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = now()

class Place(models.Model):
    name = models.CharField(max_length=255)
    #TODO: add GIS data types
    spent = models.ForeignKey(Spending)
    notes = models.ManyToManyField(Note)
    categories = models.ManyToManyField(Category)

