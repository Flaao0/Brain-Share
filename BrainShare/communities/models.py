from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    faculty = models.CharField('Факультет', max_length=100, blank=True)
    course = models.PositiveIntegerField('Курс', default=1)
    bio = models.TextField('О себе', blank=True)
    is_mentor = models.BooleanField('Готов помогать другим', default=False)

    class Meta:
        verbose_name = 'Профиль студента'
        verbose_name_plural = 'Профили студентов'

    def __str__(self):
        return f"Студент {self.user.username}"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Если юзер только что создан, создаем ему пустой профиль
        StudentProfile.objects.create(user=instance)