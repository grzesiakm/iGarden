from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Flower

def home(request):
    return render(request, 'igarden/home.html')

def lists(request):
    return render(request, 'igarden/lists.html')

def search(request):
    return render(request, 'igarden/search.html')

def upload_file(request):
    if request.method == 'POST':
        f_file = request.FILES['flower_file']
        print(f_file.name)
        result = 1 # here substitute res from machine learning
        return render(request, 'igarden/detail.html', {'flower': Flower.objects.get(id=result)})

    return render(request, 'search.html')
