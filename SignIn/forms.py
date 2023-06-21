from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import User
import re
from datetime import date
  
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ('user_id', 'name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 같지 않습니다")
            
        
        if len(password1) < 8:
            raise forms.ValidationError('비밀번호는 8자리이상을 입력해주세요.')
        
        if not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1):
            raise forms.ValidationError('비밀번호에 숫자와 문자를 포함해 주세요.')
            
        return password2
    
    def clean_user_id(self): # ID 유효성검사
        user_id = self.cleaned_data.get('user_id')
        if not re.match(r'^[a-zA-Z0-9]+$', user_id):
            raise forms.ValidationError('아이디는 영어와 숫자로 구성해주세요.')
        if User.objects.filter(user_id=user_id).exists():
            raise forms.ValidationError('이미 사용중인 아이디입니다.')
        return user_id
    
    
    
    def clean_phone_num(self):  # 핸드폰번호 유효성검사
        phone_num = self.cleaned_data.get("phone_num")
        if len(phone_num) < 11:
            raise forms.ValidationError("핸드폰 번호는 11자리를 입력해주세요") 
        return phone_num
    
    def clean_name(self): # 이름 유효성검사
        name = self.cleaned_data.get("name")
        if not re.match(r'^[가-힣]+$', name):
            raise forms.ValidationError("이름은 한글로 입력해주세요.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용 중인 이메일입니다.')
        return email
        
        

    def clean_birth(self): # 생년월일 유효성검사
        birth = self.cleaned_data.get('birth')
        if birth < date(1900, 1, 1):
            raise forms.ValidationError('올바른 날짜를 입력해 주세요.')
        return birth
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def clean(self):
        pass
    
    
    
# 사용자의 자기 정보 변경 폼
class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields =   ( 'name', 'email', 'phone_num', 'emergency', 'address',)

    
    
class PasswordResetForm(auth_forms.PasswordResetForm):
    username = auth_forms.UsernameField(label="user_id")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(user_id=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(user_id=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'user_id__iexact': self.cleaned_data["username"],  
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )
