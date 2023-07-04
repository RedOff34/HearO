"""
URL configuration for hearo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import include, path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from hearo.utils import logout_required
from . import views

app_name = 'hearo'

@logout_required
def index(request):
    return render(request, 'Index.html')

def Info(request):
    return render(request, 'Info.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='first'), # 맨 처음들어왔을때 화면
    path('Info/', Info), # 정보화면
    path('SignIn/',include('SignIn.urls')), # 회원가입 페이지
    path('Main/',include('Main.urls')), # 메인 페이지
    path('app/', include('app.urls')), # 어플기능
    path('firebase-messaging-sw.js', views.ServiceWorkerView.as_view(), name='service_worker'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
