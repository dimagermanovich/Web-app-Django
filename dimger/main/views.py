from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from sick_leave.models import tableIncapables


def index(request):
    lists2 = tableIncapables.objects.all()
    return render(request, 'main/index.html', {'lists2': lists2})


def about(request):
    lists2 = tableIncapables.objects.all()
    return render(request, 'main/about.html', {'lists2': lists2})


def contacts(request):
    lists2 = tableIncapables.objects.all()
    return render(request, 'main/contacts.html', {'lists2': lists2})


def register(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Проверяем, что пароли совпадают
        if password == confirm_password:


            try:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')
            except:
                error_msg = 'Имя пользователя уже занято'
                return render(request, 'registration/register.html', {'error_msg': error_msg})
            # Создаем нового пользователя
            user = User.objects.create_user(username=username, email=email, password=password)

            # Авторизуем пользователя
            login(request, user)

            # Перенаправляем пользователя на главную страницу
            return redirect('home')
        else:
            # Если пароли не совпадают, показываем ошибку
            error = "Passwords don't match"
            return render(request, 'registration/register.html', {'error': error})

    # Если метод запроса GET, показываем страницу регистрации
    else:
        return render(request, 'registration/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль. Попробуйте снова.')
    return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')
