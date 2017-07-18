# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import  datetime
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from forms import SignUpForm
from forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password
from models import User


def signup_view(request):
    if request.method == "GET":
        print ('GET REQUEST')
        today = datetime.now()
        print (today)
        signup_form = SignUpForm()
        return render(request, 'index.html', {'today': today, 'signup_form': signup_form})
    elif request.method == 'POST':
            user_data = SignUpForm(request.POST)
            if user_data.is_valid():
                username = user_data.cleaned_data['username']
                full_name = user_data.cleaned_data['full_name']
                email = user_data.cleaned_data['email']
                password = user_data.cleaned_data['password']
                print ('%s %s %s %s' % (username, full_name, email, password))
                # saving data to DB
                user = User(full_name=full_name,
                            password=make_password(password),
                            email=email,
                            username=username)
                user.save()
