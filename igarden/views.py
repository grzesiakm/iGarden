from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'igarden/home.html')


def lists(request):
    return render(request, 'igarden/lists.html')


def search(request):
    return render(request, 'igarden/search.html')


def upload_file(request):
    if request.method == 'POST':
        f_file = request.FILES['flower_file']
        fs = FileSystemStorage()
        fs.save(f_file.name, f_file)
        print(f_file.name)
    return render(request, 'search.html')


