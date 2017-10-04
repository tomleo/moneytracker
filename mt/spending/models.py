# from django.contrib.gis.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(blank=True, default=u'', max_length=255)

    # objects = models.GeoManager()

    def __str__(self):
        return "%s" % self.name


class Note(models.Model):
    """
    Note about something, like a place you ate at
    """
    timestamp = models.DateTimeField('date taken', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default=u'')
    user = models.ForeignKey(User)

    # objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.name


class Place(models.Model):
    """
    decimal  decimal     distance
    places   degrees    (in meters)
    -------  ---------  -----------
      1      0.1000000  11,057.43      11 km
      2      0.0100000   1,105.74       1 km
      3      0.0010000     110.57
      4      0.0001000      11.06
      5      0.0000100       1.11
      6      0.0000010       0.11      11 cm
      7      0.0000001       0.01       1 cm

    -- https://stackoverflow.com/a/16743805

    Latitude in degrees is -90 and +90
    Longitude is in the range -180 and +180

    1+2+1+7 == 11
    1+3+1+7 == 12
    """
    name = models.CharField(max_length=255)
    # Geos Libraries are a nightmare to install
    # removing them until better OS package support is available
    # location = models.PointField(blank=True, null=True)
    lng = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    lat = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    notes = models.ManyToManyField(Note, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    # objects = models.GeoManager()

    def __str__(self):
        return "%s" % self.name


class Spending(models.Model):
    timestamp = models.DateTimeField('date published')
    time_of_purchase = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    description = models.TextField(blank=True, default=u'')
    receipt = models.ImageField(blank=True, null=True)  # upload_to=None
    receipt_text = models.TextField(blank=True,
                                    default=u'')  # Populated via OCR
    place = models.ForeignKey(Place, blank=True, null=True)
    user = models.ForeignKey(User)

    # objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        super(Spending, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.amount
