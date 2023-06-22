# app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    # path('', views.Index, name='index'), # 메인 페이지
     path('save_location/', views.save_location, name='save_location'),  # 스마트폰 GPS 위치 가져오기
     path('show_location/', views.show_location, name='show_location'),
     path('userdanger/', views.get_user_danger, name='get_user_danger'),     
]


