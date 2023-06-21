# SignIn/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'SignIn'

urlpatterns = [
    path('', views.Index), # 회원 가입
    path('login/', auth_views.LoginView.as_view(template_name='account/signin.html'), name='login'), # 로그인
    path('logout/', auth_views.LogoutView.as_view(next_page='/SignIn/'), name='logout'), # 로그아웃
    path('signup/', views.signup, name='signup'),          # 회원가입
    path('delete/', views.delete, name='delete'),          # 회원탈퇴
    path('update/', views.user_update, name='update'),     # 회원정보수정
    path('password/', views.password, name='password'),    # 비밀번호 변경
    path('get_user_info/', views.get_user_info, name='get_user_info'),  # 회원 정보 GET
    path('profile/', views.profile_view, name='profile'), # 프로필 보기
    
    # 비밀번호 초기화
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
	# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'SignIn/password_reset_done.html'),name='password_reset_done' ),
	# # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # # 이메일 발송
    # path('send_email/', views.send_email, name='send_email'),  

]



