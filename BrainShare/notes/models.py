from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField('Название предмета', max_length=100)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField('Заголовок конспекта', max_length=255)
    content = models.TextField('Текст конспекта')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', verbose_name='Предмет')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    
    is_public = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'

    def __str__(self):
        return self.title