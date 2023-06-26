# hearo/forms.py

from django import forms
from SignIn.models import User

class LoginForm(forms.Form):
    
    class Meta:
        model = User
        fields = ('user_id', 'password') 