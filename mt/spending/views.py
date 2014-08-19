from django.shortcuts import render, redirect

from django.views.generic import View

from . import forms
#from . import models # Category, Tag, Transaction

class LogSpending(View):
    def get(self, *args, **kwargs):
        render(self.request, 'log_spending.html', {'test': 'test'})

    def post(self, *args, **kwargs):
        render(self.request, 'log_spending.html', {'test': 'test'})

def log_spending(request):
    form = forms.SpendingForm()
    if request.method == 'POST':
        form = forms.SpendingForm(request.POST)
        if form.is_valid:
            form.save()
            redirect('log_spending_success')
    return render(request, 'log_spending.html', {'form': form})

def log_spending_success(request):
    return render(request, 'log_spending_success.html')
