from django.db import models

from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)

class Transaction(models.Model):
    TYPE = (
        ('Pur', 'Purchase'),
        ('Iou', 'Debt'),
        ('Uom', 'Credits')
    )

    #place = models.ForeignKey()
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    notes = models.TextField()
    type = models.CharField(max_length=6, blank=True, choices=TYPE)
    category = models.ManyToManyField(Category, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()

