from django.forms import ModelForm

from . import models

class SpendingForm(ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['amount', 'notes', 'type', 'category', 'tag']

