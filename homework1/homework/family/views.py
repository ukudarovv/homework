from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import View
from .forms import *


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        if request.user.is_authenticated == True:
            return redirect("index")
        else:
            return render(request, 'login.html', context)


    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            user = authenticate(
                username=username, password=password
            )
            if user:
                login(request, user)
                return redirect("index")
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, 'index.html', context)
