from django.contrib.auth.models import User
from django.utils import timezone
import factory
from faker import Factory as FakerFactory

from . import models

faker = FakerFactory.create()


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
