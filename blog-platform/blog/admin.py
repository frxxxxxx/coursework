from django.contrib import admin
from .models import Post, Attachment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'cover_image')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'post', 'uploaded_at')
