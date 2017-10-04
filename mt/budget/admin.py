from django.contrib import admin

from budget.models import BudgetLog, BudgetItem

class BudgetLogAdmin(admin.ModelAdmin):
    pass

class BudgetItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(BudgetLog, BudgetLogAdmin)
admin.site.register(BudgetItem, BudgetItemAdmin)
