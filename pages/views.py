from django.shortcuts import render

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