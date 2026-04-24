from django.contrib import admin
from .models import Meme

# Register your models here.
@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'likes', 'created_at')
    search_fields = ('title', 'author__username')