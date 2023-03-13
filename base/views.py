import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Quote, BlogPost
from .forms import CreateUserForm, ContactForm

from .lib.email import send_email
from .lib.email import templates

def blogView(request):
    query = request.GET.get('q')
    if query:
        results = BlogPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        results = BlogPost.objects.all().order_by('-created_on')
    context = {
        'posts': results
    }

    return render(request, 'base/post_condensed.html', context)

def profileView(request, username):
    user = User.objects.get(username=username)
    if user:
        if request.user.is_authenticated:
            context = {
                "firstName": user.first_name,
                "lastName": user.last_name,
                "username": username,
                "email": user.email,
            }
            return render(request, 'base/profile.html', context)
        else:
            context = {
                "firstName": user.first_name,
                "lastName": user.last_name,
                "username": username,
            }
            return render(request, 'base/profile.html', context)
    else:
        messages.error(request, "Account for " + username + " not found")
        return redirect("404")

def blogFull(request, slug):
    post = BlogPost.objects.get(slug=slug)
    context = {
        'blog': post,
    }
    return render(request, 'base/post_detailed.html', context)

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
            messages.error(request, "Username or password incorrect.")
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
            name = form.cleaned_data['name'].strip()
            try:
                first_name, last_name = name.split(" ", 1)
                user = form.save(commit=False)
                user.first_name = first_name
                user.last_name = last_name
            except ValueError:
                first_name = name
                user = form.save(commit=False)
                user.first_name = first_name
            finally:
                user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + username)
            return redirect('login')
        messages.error(request, "Form is invalid!")
        return render(request, 'base/login.html')
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

def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login to fill the contact form')
        return redirect('login')
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            
            # send email
            email = request.user.email
            name = request.user.first_name + " " + request.user.last_name
            if len(name) < 3:
                name = request.user.username
            form_message = form.cleaned_data['content']

            response = templates.contact_response(name, form_message)
            send_email.send_simple_message(email, "Thanks for contacting me!", response)

            messages.success(request, 'Form submitted successfully.')
        else:
            messages.error(request, 'Form is invalid, Please try again.')
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