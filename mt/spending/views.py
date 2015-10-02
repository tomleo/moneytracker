from rest_framework import generics

from . import models, serializers


class AddCategory(generics.CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class AddNote(generics.CreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class AddPlace(generics.CreateAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer


class AddSpending(generics.CreateAPIView):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer


class ListCategory(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ListNote(generics.ListAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class ListPlace(generics.ListAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer


class ListSpending(generics.ListAPIView):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer
