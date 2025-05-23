"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Указываем корень проекта


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tvd8x$$=ce*t3%w(hae7l*dulz977+$+gq&jmq#il+(3)rdrh='  # Секретный ключ, его нужно хранить в безопасности

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Панель администратора Django
    'django.contrib.auth',  # Система аутентификации пользователей
    'django.contrib.contenttypes',  # Основной механизм управления типами данных в Django
    'django.contrib.sessions',  # Сессии пользователей
    'django.contrib.messages',  # Сообщения для пользователей
    'django.contrib.staticfiles',  # Статические файлы (CSS, JS, изображения)
    'ckeditor',  # WYSIWYG редактор для текста
    'ckeditor_uploader',  # Для загрузки изображений в CKEditor
    'sass_processor',  # Для обработки SCSS
    'accounts',  # Приложение для работы с пользователями
    'blog',  # Приложение для постов в блоге
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Защита от атак
    'django.contrib.sessions.middleware.SessionMiddleware',  # Обработка сессий
    'django.middleware.common.CommonMiddleware',  # Основные функции, включая обработку редиректов
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аутентификация пользователей
    'django.contrib.messages.middleware.MessageMiddleware',  # Сообщения для пользователей
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от атак типа clickjacking
]

ROOT_URLCONF = 'myblog.urls'  # Конфигурация URL-ов для проекта

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Шаблонная система Django
        'DIRS': [BASE_DIR / 'templates'],  # Директория для поиска шаблонов
        'APP_DIRS': True,  # Включаем автоматический поиск шаблонов в каждом приложении
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # Обработчик контекста для обработки запросов
                'django.contrib.auth.context_processors.auth',  # Обработчик контекста для пользователей
                'django.contrib.messages.context_processors.messages',  # Обработчик контекста для сообщений
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'  # Приложение WSGI для запуска проекта

# Настройки БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Используем MySQL как базу данных
        'NAME': 'myblog',  # Имя базы данных
        'USER': 'root',  # Пользователь базы данных
        'PASSWORD': 'root',  # Пароль базы данных
        'HOST': 'localhost',  # Хост базы данных
        'PORT': '3306',  # Порт базы данных
        'OPTIONS': {
            'charset': 'utf8mb4',  # Кодировка для поддержки Emoji и других символов
            'use_unicode': True,  # Использование Unicode
        },
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Проверка на схожесть атрибутов пользователя
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Минимальная длина пароля
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Проверка на распространённые пароли
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Проверка на числовые пароли
]

# Настройки для локализации
LANGUAGE_CODE = 'en-us'  # Язык по умолчанию
TIME_ZONE = 'UTC'  # Временная зона по умолчанию
USE_I18N = True  # Включение интернационализации
USE_TZ = True  # Включение использования временных зон

# Настройки для CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"  # Папка для загрузки файлов
CKEDITOR_IMAGE_BACKEND = "pillow"  # Используем Pillow для обработки изображений
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # Запрещаем загружать не изображения
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Кастомная панель инструментов
        'height': 300,  # Высота редактора
        'width': '100%',  # Ширина редактора
        'toolbar_Custom': [
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Blockquote']},
            {'name': 'alignment', 'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'tools', 'items': ['Maximize', 'Source']},
        ],
        'extraPlugins': ','.join([
            'uploadimage',  # Для загрузки изображений
            'colorbutton',  # Для выбора цвета текста и фона
            'font',         # Для выбора шрифта
            'justify',      # Для выравнивания текста
        ]),
    }
}

# Статические файлы
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',  # Для обработки SCSS
]

STATIC_URL = '/static/'  # Путь для доступа к статическим файлам
STATICFILES_DIRS = [BASE_DIR / 'static']  # Директория для поиска статических файлов
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Директория для хранения скомпилированных статических файлов
SASS_PROCESSOR_ROOT = STATICFILES_DIRS[0]  # Путь для обработки SCSS
SASS_PROCESSOR_INCLUDE_DIRS = STATICFILES_DIRS  # Включение всех директорий для SCSS

MEDIA_URL = '/media/'  # Путь для доступа к загруженным файлам
MEDIA_ROOT = BASE_DIR / 'media'  # Директория для хранения загруженных файлов

# URL-ы для входа/выхода
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'blog:post_list'  # Куда перенаправлять после успешного входа
LOGOUT_REDIRECT_URL = 'accounts:login'  # Куда перенаправлять после выхода

# По умолчанию используется BigAutoField для автоинкрементных полей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
