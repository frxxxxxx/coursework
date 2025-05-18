# Импортируем необходимые модули из Django
from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя
from django.db.models.signals import post_save  # Сигналы для отслеживания событий сохранения
from django.dispatch import receiver  # Декоратор для сигналов

# Модель профиля пользователя
class Profile(models.Model):
    # Связь «один-к-одному» с моделью User
    user = models.OneToOneField(
        User,  # Модель, с которой будет связь
        on_delete=models.CASCADE,  # Если пользователь удален, то и профиль тоже
        related_name='profile'  # Через это имя можно получить профиль из объекта User
    )

    # Аватар пользователя: изображение
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/%d/',  # Папка для хранения аватаров с годом, месяцем и днем
        blank=True,  # Поле не обязательно
        null=True  # Поле может быть пустым в базе данных
    )

    # Возможность выбора темы оформления: светлая или темная
    THEME_CHOICES = [
        ('light', 'Светлая'),  # Светлая тема
        ('dark',  'Тёмная'),  # Тёмная тема
    ]
    # Поле для выбора темы
    theme = models.CharField(
        max_length=10,  # Максимальная длина строки (10 символов)
        choices=THEME_CHOICES,  # Доступные варианты для выбора
        default='light'  # Значение по умолчанию — светлая тема
    )

    # Строковое представление профиля (для админки или отладки)
    def __str__(self):
        return f'Профиль {self.user.username}'

# Сигнал: при создании нового пользователя автоматически создаём профиль
@receiver(post_save, sender=User)  # Слушаем сигнал post_save для модели User
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Если пользователь только что был создан
        Profile.objects.create(user=instance)  # Создаем профиль для нового пользователя

# Сигнал: при сохранении пользователя, также сохраняем его профиль
@receiver(post_save, sender=User)  # Слушаем сигнал post_save для модели User
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Сохраняем профиль, связанный с пользователем
