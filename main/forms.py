from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from . models import *

class CustomerForm(ModelForm):
  class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
  username=forms.CharField(max_length=256)
  email=forms.EmailField(widget=forms.EmailInput)
  password1=forms.CharField(widget=forms.PasswordInput)
  password2=forms.CharField(widget=forms.PasswordInput)

