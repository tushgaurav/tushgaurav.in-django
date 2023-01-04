import random

from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.db.models import F
from .models import Suggestion, Quote

def not_found(request, any):
    # Get a random quote for the 404 error screen
    quote_list = list(Quote.objects.all())
    random_quote = random.choice(quote_list)

    context = {
        "url": any,
        "error_message": random_quote.text,
        "code": "404"
    }
    return render(request, 'base/not_found.html', context)

def index(request):
    return render(request, 'base/homepage.html')

def about(request):
    return render(request, 'base/about.html')

def skills(request):
    return render(request, 'base/skills.html')

def submit_suggestion(request):
    if request.method == 'POST':

        pass
    else:
        return redirect('home')