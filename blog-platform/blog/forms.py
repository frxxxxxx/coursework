from django import forms
from django.forms import ClearableFileInput
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'cover_image']

    cover_image = forms.ClearableFileInput(attrs={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Настройка виджета для поля cover_image
        self.fields['cover_image'].widget.attrs.update({'class': 'form-control'})

    def clean_cover_image(self):
        # Проверяем, если нужно удалить изображение
        if 'clear_cover_image' in self.data and self.data['clear_cover_image'] == 'on':
            return None  # Убираем изображение
        return self.cleaned_data.get('cover_image')
