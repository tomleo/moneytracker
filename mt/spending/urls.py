from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import LogSpending

urlpatterns = patterns('',
    url(r'^$', LogSpending.as_view(), name="log_spending"),
)
