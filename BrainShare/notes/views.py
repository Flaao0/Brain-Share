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
    viewed_notes = request.session.get("viewed_notes", [])
    note_id = str(note.pk)
    if note_id in viewed_notes:
        viewed_notes.remove(note_id)
    viewed_notes.insert(0, note_id)
    request.session["viewed_notes"] = viewed_notes[:5]

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


def viewed_notes_history(request):
    viewed_ids = request.session.get("viewed_notes", [])
    ordered_notes = []
    for note_id in viewed_ids:
        note = Note.objects.filter(pk=note_id).first()
        if note:
            ordered_notes.append(note)
    return render(request, "notes/history.html", {"notes": ordered_notes})


def toggle_theme(request):
    next_url = request.META.get("HTTP_REFERER", "/")
    current_theme = request.COOKIES.get("theme", "light")
    new_theme = "dark" if current_theme != "dark" else "light"
    response = redirect(next_url)
    response.set_cookie("theme", new_theme, max_age=60 * 60 * 24 * 365)
    return response

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


@login_required
def edit_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            edited_note = form.save(commit=False)
            edited_note.author = request.user
            edited_note.save()
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})


@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:notes')

    return render(request, 'notes/delete_note_confirm.html', {'note': note})