from django.contrib.auth.models import User
import factory

from . import models


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
