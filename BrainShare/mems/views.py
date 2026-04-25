from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meme
from .forms import MemeForm
# Create your views here.


def mems_list(request):
    mems_db = Meme.objects.all()
    context = {
        "memes": mems_db
    }
    return render(request, 'mems/all.html', context)


@login_required
def add_meme(request):
    if request.method == "POST":
        form = MemeForm(request.POST)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.author = request.user
            meme.save()
            return redirect("mems:meme_feed")
    else:
        form = MemeForm()

    return render(request, "mems/add_meme.html", {"form": form})


@login_required
def edit_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk, author=request.user)

    if request.method == "POST":
        form = MemeForm(request.POST, instance=meme)
        if form.is_valid():
            edited = form.save(commit=False)
            edited.author = request.user
            edited.save()
            return redirect("mems:meme_feed")
    else:
        form = MemeForm(instance=meme)

    return render(request, "mems/edit_meme.html", {"form": form, "meme": meme})


@login_required
def delete_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk, author=request.user)

    if request.method == "POST":
        meme.delete()
        return redirect("mems:meme_feed")

    return render(request, "mems/delete_meme_confirm.html", {"meme": meme})