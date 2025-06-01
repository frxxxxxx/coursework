## Настройка проекта
1. **Клонирование проекта (Зайти в папку через cmd)**:
    - Перенести папку на рабочий стол
    cd <Путь в папку>

2. **Создание виртуального окружения (cmd)**:
    python -m venv venv
    venv\Scripts\activate

   **Если pip не работает**:
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip

3. **Установка зависимостей (cmd)**:
    pip install -r requirements.txt

4. **MySQL**:
        Установить MySQL (https://dev.mysql.com/downloads/installer/). Пароль везде - root.

## Настройка базы данных
1. **Создание базы данных в MySQL (MySQL Command Line)**:
    Ввод пароля - root
    Создание БД - CREATE DATABASE myblog;  ```

2. **Миграция базы данных (cmd)**:
    python manage.py migrate

3. **Генерация пользователей и постов**:
    python seed.py

## Запуск сайта

1. **Запуск сервера Django (cmd)**:
    python manage.py runserver

    Cервер - `http://127.0.0.1:8000/`.