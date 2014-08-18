from django.shortcuts import render

from django.views.generic import View

from .models import Category, Tag, Transaction

class LogSpending(View):

    def get(self, *args, **kwargs):
        render(self.request, 'log_spending.html', {})

    def post(self, *args, **kwargs):
        render(self.request, 'log_spending.html', {})
