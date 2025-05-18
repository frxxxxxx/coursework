# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ClearableFileInput

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Обязательно. В формате: user@example.com')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'theme')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'display: none;',
            }),
            'theme': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Удаляем вывод имени файла
        self.fields['avatar'].label = "Аватар"
        self.fields['avatar'].widget.template_name = 'widgets/custom_clearable_file_input.html'

