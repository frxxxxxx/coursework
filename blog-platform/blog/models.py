from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField("Заголовок", max_length=200)
    content = RichTextUploadingField("Содержимое")  # WYSIWYG с загрузкой изображений
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    cover_image = models.ImageField(
        "Обложка",
        upload_to='covers/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Изображение будет показано в круглом формате над содержимым"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.pk)])

class Attachment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    file = models.FileField("Файл", upload_to='attachments/%Y/%m/%d/')
    uploaded_at = models.DateTimeField("Загружено", auto_now_add=True)

    def __str__(self):
        return self.file.name
