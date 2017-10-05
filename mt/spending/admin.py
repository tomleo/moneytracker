# from django.contrib.gis import admin
from django.contrib import admin

from spending.models import Category, Note, Spending, Place

admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Note, admin.ModelAdmin)
admin.site.register(Spending, admin.ModelAdmin)
admin.site.register(Place, admin.ModelAdmin)
