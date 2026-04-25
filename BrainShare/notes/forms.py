from django import forms
from .models import Note, Comment

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'content', 'image_path']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Запретим слишком короткие или странные заголовки
        if len(title) < 3:
            raise forms.ValidationError("Название слишком короткое!")
        if "фигня" in title.lower(): # Простая защита от мата
            raise forms.ValidationError("Пожалуйста, используйте приличные названия.")
        return title
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Ваш комментарий'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Что думаете об этом конспекте?'}),
        }