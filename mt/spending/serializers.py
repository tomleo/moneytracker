from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spending
