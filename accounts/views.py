from django.shortcuts import render
from django.contrib.auth import get_user_model

import random
def register(request):
    User = get_user_model()
    if request.POST:
        email = request.POST.get('email')
        password = ''
        for x in range(10):  # Количество символов (16)
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        user = User.objects.create_user(email)
        user.set_password(password)
        context = {'email': email, 'password': password, 'user': user}
    else:
        context = {}
    return render(request, 'accounts/register.html', context=context)



# from django.contrib.auth import authenticate, login
#
#
# def my_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...