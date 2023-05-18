from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    data = {
        'title': 'Django Framework',
        'message': 'Hello, World',
        'lists': [1, 2, 3, 4]
    }
    return render(request, 'core/home.html', data)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

