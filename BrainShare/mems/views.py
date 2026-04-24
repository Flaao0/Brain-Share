from django.shortcuts import render
from .models import Meme
# Create your views here.


def mems_list(request):
    mems_db = Meme.objects.all()
    context = {
        "memes": mems_db
    }
    return render(request, 'mems/all.html', context)