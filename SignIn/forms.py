from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from .models import User
import re
from datetime import date
  
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm

class UserCreationForm(forms.ModelForm):
    name = forms.CharField(
    max_length=5, 
    widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'id': 'form-floating-1', 
            'placeholder': '홍길동'}))
     
    GENDER_CHOICES = [
        ('남자', '남자'),
        ('여자', '여자'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    
    user_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'form-floating-3',
            'placeholder': '아이디 입력(6~20자)'
        }))
    
    birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
                'id': 'form-floating-3',
                'style': 'font-size: 0.7em; font-style: italic; color: #aaa',
            }))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'id': 'form-floating-2',
                'placeholder': 'name@example.com'
            }))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '숫자와 문자를 조합해 8자 이상을 입력해주세요.'
            }))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '비밀번호를 한 번 더 입력해주세요.'
            }))
    phone_num = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '01000000000'
            }))
    emergency = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '01000000000'
            }))
    
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '서울시 강남구 역삼동'
            }))
    
    medical_info = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '혈액형, 복용 중인 약, 기저질환 등을 입력해 주세요.'
            }))
    class Meta:
        model = User
        fields = ('user_id', 'name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth', 'medical_info')

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
        if len(user_id) < 6:
            raise forms.ValidationError('아이디는 6자리이상을 입력해주세요.')
        if User.objects.filter(user_id=user_id).exists():
            raise forms.ValidationError('이미 사용중인 아이디입니다.')
        return user_id
    
    
    
    def clean_phone_num(self):  # 핸드폰번호 유효성검사
        phone_num = self.cleaned_data.get("phone_num")
        if len(phone_num) < 11:
            raise forms.ValidationError("연락처는 11자리를 입력해주세요") 
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
    
    def clean_emergency(self):  # 핸드폰번호 유효성검사
        emergency = self.cleaned_data.get("emergency")
        if len(emergency) < 11:
            raise forms.ValidationError("연락처는 11자리를 입력해주세요") 
        return emergency
        
        

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
    name = forms.CharField(
        max_length=5, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'id': 'form-floating-1', 
                'placeholder': '홍길동'}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'id': 'form-floating-2',
                'placeholder': 'name@example.com'
            }))
    
    phone_num = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '01000000000'
            }))
            
    emergency = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '01000000000'
            }))
    
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '서울시 강남구 역삼동'
            }))
    
    medical_info = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '혈액형, 복용 중인 약, 기저질환 등을 입력해 주세요.'
            }))

    class Meta:
        model = User
        fields = ('name', 'email', 'phone_num', 'emergency', 'address','medical_info')
    
    def clean_name(self): # 이름 유효성검사
        name = self.cleaned_data.get("name")
        if not re.match(r'^[가-힣]+$', name):
            raise forms.ValidationError("이름은 한글로 입력해주세요.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('이미 사용 중인 이메일입니다.')
        return email

    def clean_phone_num(self):  # 핸드폰번호 유효성검사
        phone_num = self.cleaned_data.get("phone_num")
        if len(phone_num) < 11:
            raise forms.ValidationError("연락처는 11자리를 입력해주세요") 
        return phone_num
    
    def clean_emergency(self):  # 핸드폰번호 유효성검사
        emergency = self.cleaned_data.get("emergency")
        if len(emergency) < 11:
            raise forms.ValidationError("연락처는 11자리를 입력해주세요") 
        return emergency


# 로그인 폼
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            'required': '아이디를 입력해주세요.',
            'invalid': '잘못된 아이디입니다.',
        },
        label='아이디',
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            'required': '비밀번호를 입력해주세요.',
        },
        label='비밀번호',
    )
    error_messages = {
        'invalid_login': "아이디 또는 비밀번호가 일치하지 않습니다.",
        'inactive': "이 계정은 활성화되지 않았습니다.",
    }
    
    
    
# 비밀번호 변경폼
class PasswordChangeForm(AuthPasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '현재 비밀번호'
            }))

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '새 비밀번호'
            }))

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-floating-3',
                'placeholder': '새 비밀번호 확인'
            }))
    
    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 같지 않습니다.")
        if len(password1) < 8:
            raise forms.ValidationError('비밀번호는 8자리이상을 입력해주세요.')
        if not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1):
            raise forms.ValidationError('비밀번호에 숫자와 문자를 포함해 주세요.')
        return password2
