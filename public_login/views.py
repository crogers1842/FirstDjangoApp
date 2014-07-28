from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.user is not None:
        return render(request, "login/home.html")
    else:
        return render(request, "login/login.html")


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('login/home.html'))
        else:
            return render(request, 'login/login.html', {'error_message': 'User is not an active user.'})
    else:
        return render(request, 'login/login.html', {'error_message': 'Incorrect username or password'})


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login/login.html'))


def create_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return HttpResponseRedirect(reverse("login/home.html"))


def register(request):
    return render(request, "login/register.html")