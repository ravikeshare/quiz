from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Quiz, Question, Answer


def login_user(request):
	if request.method == "GET":
		return render(request, 'ques_ans/login.html', {'form': AuthenticationForm()})
	else:
		user = authenticate(requests,
				username=requests.POST.get('username'),
				password = requests.POST.get('password') )
		if not user:
			return render(request, 'ques_ans/login.html', {'form': AuthenticationForm()})
		else:
			login(requests, user)
			return redirect('quiz_list')

def quiz_list(requests):
	quzes = Quiz.objects.filter(is_available=True)
