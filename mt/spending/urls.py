from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='spending/index.html')),
    url(r'^add_category/$', views.AddCategory.as_view(), name="add-category"),
    url(r'^add_note/$', views.AddNote.as_view(), name="add-note"),
    url(r'^add_place/$', views.AddPlace.as_view(), name="add-place"),
    url(r'^add_spending/$', views.AddSpending.as_view(), name="add-spending"),
    url(r'^list_category/$', views.ListCategory.as_view(), name="list-category"),
    url(r'^list_note/$', views.ListNote.as_view(), name="list-note"),
    url(r'^list_place/$', views.ListPlace.as_view(), name="list-place"),
    url(r'^list_spending/$', views.ListSpending.as_view(), name="list-spending"),
    
]
