from django.contrib.gis import admin

from spending.models import Category, Note, Spending, Place

admin.site.register(Category, admin.GeoModelAdmin)
admin.site.register(Note, admin.GeoModelAdmin)
admin.site.register(Spending, admin.GeoModelAdmin)
admin.site.register(Place, admin.GeoModelAdmin)
