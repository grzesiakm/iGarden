from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Flower

def home(request):
    return render(request, 'igarden/home.html')

def lists(request):
    return render(request, 'igarden/lists.html')

def search(request):
    if request.method == 'POST':
        # f_file = request.FILES['flower_file']
        # print(f_file.name)
        # (nazwa, index) = find_kwiatek_mondre_maszyny(f_file)
        return render(request, 'igarden/detail.html', {'flower': Flower.objects.filter(name='Daisy')[0]})
    return render(request, 'igarden/search.html')
