from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import NewUserForm

import random
def register(request):
    User = get_user_model()
    context = {'email': ''}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            context.email = form.cleaned_data.get('email')
        else:
            form = NewUserForm()
    #     email = request.POST.get('email')
        password = ''
        for x in range(10):  # Количество символов (16)
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    #     # user = User.objects.create_user(email=email, pasword=password)
    #     context = {'email': email, 'password': password, 'form'}
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