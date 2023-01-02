from django.shortcuts import render, redirect
from .models import Suggestion

def index(request):
    return render(request, 'base/homepage.html')

def submit_suggestion(request):
    if request.method == 'POST':

        pass
    else:
        return redirect('home')