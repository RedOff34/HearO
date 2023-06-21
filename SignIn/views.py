# SignIn/views.py
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse, JsonResponse
from .forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
import requests
from django.contrib import messages

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from SignIn.forms import UserCreationForm, PasswordResetForm


# Create your views here.
def Index(request):
    return render(request, 'SignInIndex.html')


def signup(request):
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data.get('user_id')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(user_id=user_id, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = forms.UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required
def user_update(request):
    if request.method == 'POST':
        form = forms.UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('../')  # 수정 후 리디렉션할 URL
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'account/user_update.html', {'form': form})



@require_POST
@login_required

def delete(request):
    user = request.user
    user.delete()
    logout(request) # 
    return redirect('../')




@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호를 바꾸면 기존 세션과 일치하지 않게 되어 로그아웃된다. 이를 방지하기 위한 auth_hash 갱신.
            update_session_auth_hash(request, user)  
            return redirect('../')
    
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/user_update_password.html',{'form':form})


from django.core.mail import EmailMessage

def send_email(request):
    subject = "message"							# 타이틀
    message = "메세지 테스트"					# 본문 내용
    to = [""]					# 수신할 이메일 주소	
    EmailMessage(subject=subject, body=message, to=to).send()


@login_required
def get_user_info(request):
    user = request.user
    user_info = {
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email,
        'phone_num': user.phone_num,
        'emergency': user.emergency,
        'address': user.address,
        'gender': user.gender,
        'birth': user.birth,
    }
    # print(user_info)  # 서버 측 콘솔에 정보 출력
    return JsonResponse(user_info)


@login_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'account/profile.html')



class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'account/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'common/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'account/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('login')