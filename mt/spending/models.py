from django.contrib.gis.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(blank=True, default=u'', max_length=255)

    objects = models.GeoManager()

    def __str__(self):
        return "%s" % self.name


class Note(models.Model):
    """
    Note about something, like a place you ate at
    """
    timestamp = models.DateTimeField('date taken', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default=u'')

    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(blank=True, null=True)
    notes = models.ManyToManyField(Note)
    categories = models.ManyToManyField(Category)

    objects = models.GeoManager()

    def __str__(self):
        return "%s" % self.name


class Spending(models.Model):
    timestamp = models.DateTimeField('date published')
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    description = models.TextField(blank=True, default=u'')
    receipt = models.ImageField(blank=True, null=True)  # upload_to=None
    receipt_text = models.TextField(blank=True,
                                    default=u'')  # Populated via OCR
    place = models.ForeignKey(Place, blank=True, null=True)

    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        super(Spending, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.amount

