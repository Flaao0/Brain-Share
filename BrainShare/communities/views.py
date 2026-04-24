from django.shortcuts import render
from django.contrib.auth.models import User

def profile_view(request):
    user_mock = User.objects.first() 
    context = {
        "user": user_mock
    }
    return render(request, 'communities/profile.html', context)