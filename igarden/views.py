from django.shortcuts import render
from PIL import Image
from model.model import Model
from .models import Flower

def home(request):
    return render(request, 'igarden/home.html')

def lists(request):
    return render(request, 'igarden/lists.html')

def search(request):
    model = Model()

    if request.method == 'POST':
        f_file = request.FILES['flower_file']
        img = Image.open(f_file)
        found_name = model.predict(img)
        return render(request, 'igarden/detail.html', {'flower': Flower.objects.filter(name=found_name)[0]})
    return render(request, 'igarden/search.html')
