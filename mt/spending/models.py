from django.db import models

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

@python_2_unicode_compatible
class BudgetItem(models.Model):

    start = models.DateTimeField()
    end = models.DateTimeField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)

    #TODO: A budget item has an associated category, however transactions and tags also have an
    # associated category.

@python_2_unicode_compatible
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

    # Purchase transactions should always have an associated budget item
    # while Iou and Uom types do not
    budget_item = models.ForeignKey(BudgetItem, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()

    def __str__(self):
        return u'%s: %s' % (self.amount, self.type)

    class Meta:
        ordering = ('timestamp',)


