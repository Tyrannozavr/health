from django.shortcuts import render
from django.contrib.auth import get_user_model

import random
def register(request):
    User = get_user_model()
    if request.POST:
        email = request.POST.get('email')
        if User.objects.get(email=email):
            print('exist')
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


