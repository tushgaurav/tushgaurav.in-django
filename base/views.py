import random

from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.db.models import F
from .models import Suggestion, Quote

def not_found(request, any):
    quote = random.choice(list(Quote.objects.all()))

    context = {
        "url": any,
        "error_message": quote.text,
        "code": "404"
    }
    return render(request, 'base/not_found.html', context)

def index(request):
    return render(request, 'base/homepage.html')

def about(request):
    return render(request, 'base/about.html')

def submit_suggestion(request):
    if request.method == 'POST':

        pass
    else:
        return redirect('home')