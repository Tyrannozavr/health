from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

import random
def register(request):
    User = get_user_model()
    if request.POST:
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            context = {'message': 'already exist'}
            return render(request, 'accounts/register.html', context=context)
        password = ''
        for x in range(10):  # Количество символов (16)
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        user = User.objects.create_user(email)
        user.set_password(password)
        context = {'email': email, 'password': password}
    else:
        context = {}
    return render(request, 'accounts/register.html', context=context)


def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('accounts/login')
