import random
from datetime import timedelta

import factory
from faker import Factory as FakerFactory
from django.utils import timezone


from . import models

faker = FakerFactory.create()


def get_random_date(start_date, days_before=0, days_after=0):
    """
    Return datetime that is x number of days_before start_date
    and y number of days_after start_date
    """
    random_day = random.randint(-days_before, days_after)
    return start_date + timedelta(days=random_day)


class BudgetLogFactory(factory.django.DjangoModelFactory):

    date = factory.LazyAttribute(get_random_date(timezone.now(), days_before=random.randint(31)))
    amount = factory.LazyAttribute(lambda x: random.random() * 100)
    category = factory.SubFactory('spending.models.Category')

    class Meta:
        model = models.BudgetLog


class BudgetItemFactory(factory.django.DjangoModelFactory):

    created = timezone.now()
    updated = factory.LazyAttribute(lambda item: item.created - timedelta(days=random.randint(1, 31)))
    name = faker.name()
    rate = factory.LazyAttribute(random.choice(dict(models.BudgetItem.RATE_CHOICES).keys()))
    amount = random.random() * 100
    user = models.SubFactory(UserFactory)

    class Meta:
        models.BudgetItem

    @factory.post_generation
    def logs(self, created, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for log in extracted:
                self.logs.add(log)

