import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import F
from .models import Suggestion, Quote, Message

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, ContactForm

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

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password incorrect.")
    context = {

    }

    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + username)
        return redirect('login')
    else:
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'base/register.html', context)

def index(request):
    return render(request, 'base/homepage.html')

def about(request):
    return render(request, 'base/about.html')

def skills(request):
    return render(request, 'base/skills.html')

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('home')
        return HttpResponse("FORM DATA IS INVALID")
        
    else:
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'base/contact.html', context)


@login_required(login_url='login')
def submit_suggestion(request):
    if request.method == 'POST':

        pass
    else:
        return redirect('home')