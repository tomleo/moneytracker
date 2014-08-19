from django.conf.urls import url, include
from django.contrib import admin

import spending
from spending import views

urlpatterns = [
    #url(r'^$', views.LogSpending.as_view()),
    url(r'^$', include('spending.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
