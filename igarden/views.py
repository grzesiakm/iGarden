from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, 'igarden/home.html')

def lists(request):
    return render(request, 'igarden/lists.html')

def find(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'igarden/find.html')
