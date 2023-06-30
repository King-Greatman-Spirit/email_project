from django.shortcuts import render, redirect

def home(request):
    context = {
        'username': 'King Greatman Spirit'
    }
    return render(request, 'home.html', context)
