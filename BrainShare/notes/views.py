from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Comment
from django.contrib.auth.models import User
from .forms import NoteForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'notes/home.html')

def note_list(request):
    notes_db = Note.objects.all() 
    context = {
        "notes": notes_db
    }
    return render(request, 'notes/list.html', context)



def note_detail_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    comments = note.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.note = note
            new_comment.save()
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = CommentForm()

    return render(request, 'notes/note_detail.html', {'note': note, 'comments': comments, 'form': form})

@login_required
def add_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            # ВМЕСТО заглушки ставим реального юзера:
            new_note.author = request.user 
            new_note.save()
            return redirect('notes:note_list')
        # Если форма невалидна, код пойдет дальше к render(request, ...) 
        # и вернет форму с ошибками (Пункт 5 выполнен!)
    else:
        form = NoteForm()
    
    return render(request, 'notes/add_note.html', {'form': form})