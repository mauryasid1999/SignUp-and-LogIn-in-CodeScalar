from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout

from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, CustomerForm


# Create your views her
from .forms import  CreateUserForm

def index(request):
	return render(request, 'main/index.html')

def register(request):

		form=CreateUserForm()
		if request.method=='POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				
				username=form.cleaned_data.get('username')
				email=form.cleaned_data.get('email')
				send_mail(
					  'Registered For CodeScalar ',
					  'Thank you For Registration .You are successfully registered for CodeScalar. Now,Practice as much as you can.',
					   settings.EMAIL_HOST_USER,
					   [email],
					   fail_silently=False,
				)
				user=form.save()
				Customer.objects.create(
					   user=user,
					   name=user.username,
									
				)
			   
				messages.success(request,'Successfully Account is Created ' +username)

				return redirect('login')
		context={'form':form}
		return render(request, 'main/register.html', context)


def login(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('/dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logout(request):
	auth_logout(request)
	return redirect('login')

@login_required(login_url='login')
def dashboard(request):
	return render(request,'main/dashboard.html')
	
@login_required(login_url='login')
def profile(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'main/profile.html', context)