from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponseRedirect


# Create your views here.
# def index(request, category_slug=None):
#     category = None
#     categories =
#     return render(request, 'accounts/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('shop:index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


# def register(request):
#     if request.method == 'POST':
#         # name = request.POST['name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username already taken.')
#                 return redirect('accounts:register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already exists')
#                 return redirect('accounts:register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email)
#                 user.save()
#                 print('user created')
#                 return redirect('accounts:login')
#         else:
#             messages.info(request, 'Password not matched.')
#             return redirect('accounts:register')
#         # return redirect('/')
#     else:
#         return render(request, 'accounts/registration.html')

def register(request):
    template = 'accounts/registration.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Password do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                auth.login(request, user)
                return redirect('shop:index')
    else:
        form = RegisterForm()
        return render(request, template, {'form': form})
