from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def hello(request):
    context = {
        'name': 'Pabz',
        'language': 'Django',
        'is_logged_in': True,
        'skills': ['Python', 'SQL', 'HTML', 'Django'],
    }
    return render(request, 'pages/hello.html', context)

def about(request):
    return render(request, 'pages/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})