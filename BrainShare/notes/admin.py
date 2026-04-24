from django.contrib import admin
from .models import Category, Note

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'is_public')
    list_filter = ('category', 'is_public', 'created_at')
    search_fields = ('title', 'content', 'author__username')