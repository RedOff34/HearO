# SignIn/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'SignIn'

urlpatterns = [
    path('', views.Index), # 회원 가입
    path('login/', views.LoginView.as_view(template_name='index.html'), name='login'), # 로그인
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # 로그아웃
    path('pia/', views.PIA, name='pia'),
    path('pia/signup/', views.signup, name='signup'),          # 회원가입
    path('profile/', views.profile_view, name='profile'), # 프로필 보기
    path('delete/', views.delete, name='delete'),          # 회원탈퇴
    path('update/', views.user_update, name='update'),     # 회원정보수정
    path('password/', views.password, name='password'),    # 비밀번호 변경
    path('get_user_info/', views.get_user_info, name='get_user_info'),  # 회원 정보 GET
    path('check-user-id/', views.CheckUserIdView.as_view(), name='check_user_id'),
]



