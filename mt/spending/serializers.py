from rest_framework import serializers

from . import models


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
