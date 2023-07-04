# app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

app_name = 'app'

urlpatterns = [
    # path('', views.Index, name='index'), # 메인 페이지
     path('save_location/', views.save_location, name='save_location'),  # 스마트폰 GPS 위치 가져오기
     path('show_location/', views.show_location, name='show_location'),
     path('userdanger/', views.get_user_danger, name='get_user_danger'),     
     path('myurl/', views.my_view, name='myview'),
     path('popup1/', views.popup1, name='popup1'),
     path('popup2/', views.popup2, name='popup2'),
     path('get_folder_contents/', views.get_folder_contents, name='get_folder_contents'),
     path('task_emergency_file/', views.task_emergency_file, name='task_emergency_file'),
     path('latesthistory/', views.get_latest_history, name='get_latest_history'),
     path('remove_file/', views.remove_file, name='remove_file'),
     path('getsetting/', views.get_setting, name='get_setting'),
     path('latestdanger/', views.get_latest_danger, name='get_latest_danger'),
     path('uploads3/', views.upload_s3, name='upload_s3'),
     path('sendmessage/', views.send_message, name='send_message'),
     path('shorurl/', views.short_url, name='short_url'),
     path('pushnoti/', views.send_push_notification, name='send_push_notification'),
     path('print_message/', views.print_message, name='print_message'),
    
]