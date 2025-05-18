# Импортируем необходимые модули и функции для обработки запросов, рендеринга шаблонов и работы с пользователями
from django.shortcuts import render, redirect  # Для отображения шаблонов и перенаправления
from django.contrib.auth import login, logout  # Для входа и выхода пользователя
from django.contrib.auth.decorators import login_required  # Декоратор для защиты представлений от неавторизованных пользователей
from .forms import RegisterForm, LoginForm, ProfileForm  # Импортируем формы для регистрации, входа и профиля

# Представление для страницы регистрации пользователя
def register_view(request):
    # Если пользователь уже авторизован, перенаправляем его на главную страницу блога
    if request.user.is_authenticated:
        return redirect('blog:post_list')

    # Обработка формы при получении POST-запроса
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  # Если форма прошла валидацию
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Авторизуем нового пользователя
            return redirect('accounts:profile')  # Перенаправляем на страницу профиля пользователя

    # Если это GET-запрос, просто отображаем пустую форму регистрации
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

# Представление для страницы входа пользователя
def login_view(request):
    # Если пользователь уже авторизован, перенаправляем его на главную страницу блога
    if request.user.is_authenticated:
        return redirect('blog:post_list')

    # Обработка формы при получении POST-запроса
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():  # Если форма прошла валидацию
            user = form.get_user()  # Получаем пользователя
            login(request, user)  # Авторизуем пользователя
            return redirect('blog:post_list')  # Перенаправляем на страницу блога

    # Если это GET-запрос, просто отображаем пустую форму для входа
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# Представление для выхода пользователя
def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('accounts:login')  # Перенаправляем на страницу входа

# Представление для страницы профиля пользователя (доступно только для авторизованных пользователей)
@login_required
def profile_view(request):
    # Получаем профиль текущего пользователя
    profile = request.user.profile

    # Обработка формы при получении POST-запроса
    if request.method == 'POST':
        pform = ProfileForm(request.POST, request.FILES, instance=profile)  # Создаем форму для редактирования профиля
        if pform.is_valid():  # Если форма прошла валидацию
            pform.save()  # Сохраняем изменения в профиле
            return redirect('accounts:profile')  # Перенаправляем на страницу профиля после сохранения

    # Если это GET-запрос, отображаем форму с текущими данными профиля
    else:
        pform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'pform': pform,  # Отправляем форму в шаблон
        'user': request.user,  # Отправляем текущего пользователя в шаблон
    })
