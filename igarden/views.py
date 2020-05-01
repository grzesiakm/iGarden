from django.shortcuts import render


def home(request):
    return render(request, 'igarden/home.html')


def lists(request):
    return render(request, 'igarden/lists.html')

