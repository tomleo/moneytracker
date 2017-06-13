from rest_framework import serializers
from django.contrib.auth.models import User
from drf_extra_fields.geo_fields import PointField

from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['name', 'description']


class PlaceSerializer(serializers.ModelSerializer):

    location = PointField()

    class Meta:
        model = models.Place
        fields = ['name', 'location', 'notes', 'categories']

class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spending
        fields = ['amount', 'description', 'receipt', 'receipt_text', 'place']
