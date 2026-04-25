from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import StudentProfile
def profile_view(request):
    user_mock = User.objects.first() 
    context = {
        "user": user_mock
    }
    return render(request, 'communities/profile.html', context)



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes:note_list') 
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})