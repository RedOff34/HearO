# Main/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Main'

urlpatterns = [
    path('', views.Index, name='index'), # 메인 페이지
    path('MyPage/', views.MyPage), # 마이 페이지
    path('Post/', views.PostMove), # 문의 게시판
    path('Settings/', views.Settings), # 설정
    path('Post/New/', views.PostNew, name = 'PostNew'),
    path('Post/<int:pk>/', views.PostView, name = 'PostView'),
    path('Post/Update/<int:pk>/', views.PostUpdate, name = 'PostUpdate'),
    path('Post/Delete/<int:pk>/', views.PostDelete, name = 'PostDelete'),
    path('Post/DeleteComment/<int:comment_id>/', views.DeleteComment, name='DeleteComment'),
    path('save-audio/', views.save_audio, name='save_audio'),
    path('userhistory/', views.get_user_history, name='get_user_history'),
]