from rest_framework import generics
from rest_framework import renderers

from . import models, serializers


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def list(request, *args, **kwargs):
        pass

    def create(request, *args, **kwargs):
        pass

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def retrieve(request, *args, **kwargs):
        pass

    def update(request, *args, **kwargs):
        pass

    def partial_update(request, *args, **kwargs):
        pass

    def destroy(request, *args, **kwargs):
        pass

class NoteListView(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def list(request, *args, **kwargs):
        pass

    def create(request, *args, **kwargs):
        pass

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def retrieve(request, *args, **kwargs):
        pass

    def update(request, *args, **kwargs):
        pass

    def partial_update(request, *args, **kwargs):
        pass

    def destroy(request, *args, **kwargs):
        pass

class PlaceListView(generics.CreateAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def list(request, *args, **kwargs):
        pass

    def create(request, *args, **kwargs):
        pass

class PlaceDetailView(generics.ListCreateAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def retrieve(request, *args, **kwargs):
        pass

    def update(request, *args, **kwargs):
        pass

    def partial_update(request, *args, **kwargs):
        pass

    def destroy(request, *args, **kwargs):
        pass

class SpendingListView(generics.CreateAPIView):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def list(request, *args, **kwargs):
        pass

    def create(request, *args, **kwargs):
        pass

class SpendingDetailView(generics.ListCreateAPIView):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpendingSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,renderers.JSONRenderer)

    def retrieve(request, *args, **kwargs):
        pass

    def update(request, *args, **kwargs):
        pass

    def partial_update(request, *args, **kwargs):
        pass

    def destroy(request, *args, **kwargs):
        pass
