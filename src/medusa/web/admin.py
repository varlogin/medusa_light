from django.contrib import admin

from .models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    pass
