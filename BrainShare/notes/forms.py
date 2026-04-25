from django import forms
from .models import Note, Comment

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'content', 'is_public'] 
        
        labels = {
            'title': 'Название конспекта',
            'category': 'Предмет',
            'content': 'Текст конспекта',
            'is_public': 'Сделать доступным для всех?',
        }
        
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Напиши сюда самое важное...'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Ваш комментарий'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Что думаете об этом конспекте?'}),
        }