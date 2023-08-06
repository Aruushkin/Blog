from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm
from users.models import User

def main_page_user_view(request):
    context_data = {}  # Предварительное объявление переменной

    if request.method == 'GET':
        users = User.objects.all()
        context_data['users'] = users  # Добавляем users в контекст

    return render(request, 'layouts/index.html', context=context_data)


def register_view(request):
    if request.method == 'GET':
        context_data = {
            'form': RegisterForm,
        }
        return render(request, 'users/register.html', context=context_data)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                 user = User.objects.create_superuser(
                     username=form.cleaned_data.get('username'),
                     password=form.cleaned_data.get('password1')
                 )

                 return redirect('/users/login/')
            else:
                form.add_error('password1', 'password1 != password2')

        return render(request, 'users/register.html', context={
            'form': form
        })


def login_view(request):
    if request.method == 'GET':
        context_data = {
            'form': LoginForm
        }
        return render(request, 'users/login.html', context=context_data)

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            """Authenticate """
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                """Authorization"""
                login(request=request, user=user)
                return redirect('/posts/')
            else:
                form.add_error('username', 'try again :(')
        return render(request, 'users/login.html', context={
            'form': None
        })


def logout_view(request):
    logout(request)
    return redirect('/posts/')
