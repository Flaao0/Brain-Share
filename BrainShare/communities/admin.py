from django.contrib import admin
from .models import StudentProfile

# Register your models here.
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'faculty', 'course', 'is_mentor')
    
    list_filter = ('faculty', 'course', 'is_mentor')
    
    search_fields = ('user__username', 'faculty')