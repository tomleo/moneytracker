from django.conf.urls import include, url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='spending/index.html'))
]
