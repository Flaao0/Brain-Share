from django.shortcuts import render
from .models import Note

# Create your views here.

def home_page(request):
    return render(request, 'notes/home.html')

def note_list(request):
    notes_db = Note.objects.all() 
    context = {
        "notes": notes_db
    }
    return render(request, 'notes/list.html', context)