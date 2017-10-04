import decimal

from django.db import models
from django.contrib.auth.models import User


class BudgetLog(models.Model):
    """
    Money allocation towards an item
    """
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey('spending.Category', blank=True, null=True)

    def __str__(self):
        amount = "%s" % (self.amount)
        if self.category:
            result = '%s: %s' % (amount, self.category.name)
        return result


class BudgetItem(models.Model):
    """
    An item user is saving money for
    """
    ANNUAL = 'annually'
    BIMONTHLY = 'bimonthly'
    MONTHLY = 'monthly'
    DAILY = 'daily'
    RATE_CHOICES = (
        (ANNUAL, 'Anually'),
        (BIMONTHLY, 'Bi-Monthly'),
        (MONTHLY, 'Monthly'),
        (DAILY, 'Daily')
    )

    created = models.DateTimeField()
    updated = models.DateTimeField()
    name = models.CharField(max_length=255)
    rate = models.CharField(max_length=65, choices=RATE_CHOICES)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    logs = models.ManyToManyField(BudgetLog)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s\% %s" % (self.name, (self.amount/self.total)*100, self.get_rate_name)

    def total(self):
        try:
            return sum(self.logs.values_list('amount', flat=True))
        except KeyError:
            return decimal.Decimal('0.0')

    def get_rate_name(self):
        return dict(self.RATE_CHOICES).get(self.rate, '')
