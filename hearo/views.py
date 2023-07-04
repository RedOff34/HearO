# hearo/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm
from SignIn.models import User
from django.views.generic import View

def Login(request):
    if request.method == "GET":
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid(): # 유효성 검사

            return redirect('/Main/')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form}) 

class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'firebase-messaging-sw.js', content_type="application/x-javascript")

