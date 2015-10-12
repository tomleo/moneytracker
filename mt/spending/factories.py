import random

from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.utils import timezone
import factory
from factory.fuzzy import BaseFuzzyAttribute
from faker import Factory as FakerFactory


from . import models

faker = FakerFactory.create()


class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0, 90.0))


class UserFactory(factory.django.DjangoModelFactory):

    password = "asdf"

    class Meta:
        model = User

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', cls.password)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = 'Cats'


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Note

    timestamp = timezone.now()
    name = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())


class PlaceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Place
    name = factory.LazyAttribute(lambda x: faker.name())
    location = FuzzyPoint()

    @factory.post_generation
    def notes(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for note in extracted:
                self.notes.add(note)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.notes.add(category)

class SpendingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Spending
    amount = factory.LazyAttribute(lambda x: random.randint(1,1000) + random.randint(0,99) / 100.0)
    description = factory.LazyAttribute(lambda x: faker.text())
    receipt_text = factory.LazyAttribute(lambda x: faker.text())
    place = factory.SubFactory(PlaceFactory)
