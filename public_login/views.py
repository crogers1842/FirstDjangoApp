from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import  reverse
# Create your views here.


def login(request, name, pw):
    user = authenticate(username=name, password=pw)
    if user is not None:
        if user.is_active:
            return HttpResponseRedirect(reverse('home.html'))
        else:
            return render(request, 'public_login/login.html', {'error_message': 'User is not an active user.'})
    else:
        return render(request, 'public_login/login.html', {'error_message': 'Incorrect username or password'})