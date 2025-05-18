# Импортируем необходимые модули для обработки URL-адресов и подключения представлений
from django.urls import path  # Импортируем путь для создания маршрутов
from . import views  # Импортируем представления из текущего приложения

# Имя пространства имен для приложения "accounts" — это помогает организовать URL-адреса
# и избегать конфликтов с другими приложениями, если в них есть одинаковые имена путей.
app_name = 'accounts'

# Список маршрутов URL для приложения "accounts"
urlpatterns = [
    # Путь для регистрации нового пользователя
    path('register/', views.register_view, name='register'),
    # Путь для страницы входа в аккаунт
    path('login/', views.login_view, name='login'),
    # Путь для выхода из аккаунта
    path('logout/', views.logout_view, name='logout'),
    # Путь для страницы профиля пользователя (после входа)
    path('profile/', views.profile_view, name='profile'),
]
