
from django import forms
from models import UserModel


class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields = ['password', 'username','email','name']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']