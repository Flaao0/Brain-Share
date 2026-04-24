from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meme(models.Model):
    title = models.CharField('Название мема', max_length=100)
    image_path = models.CharField('Путь к картинке', max_length=255, help_text='Например: img/mems/exam.jpg')
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Кто запостил')
    likes = models.IntegerField('Количество лайков', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Мем'
        verbose_name_plural = 'Мемы'

    def __str__(self):
        return self.title