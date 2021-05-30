from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from configurator.forms import *


def start_page(request):

    return render(request, 'start.html')

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main'))
        form = LoginForm()

        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info['login'], password=info['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return render(request, 'login.html', {'form': form, 'login': 'fail'})

def registration_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main'))

        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            User.objects.create_user(user['email'], user['email'], user['password'])
            login_form = LoginForm()

            return render(request, 'login.html', {'form': login_form})

def advices_view(request):
    return render(request, 'titles.html')

def item_view(request):
    return render(request, 'item.html')

def favorites_view(request):
    return render(request, 'favorites.html')
