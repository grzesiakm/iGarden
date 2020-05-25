from django.shortcuts import render
from django.views import generic
from PIL import Image
from model.model import Model
from .models import Flower
from .forms import UploadPhotoForm
from .forms import Choose_flower
from lists.forms import AddToListForm
from django.contrib import messages
from lists.models import UserFlowersList


def home(request):
    return render(request, 'igarden/home.html')


def search(request):
    model = Model()
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            f_file = form.cleaned_data['file']
            img = Image.open(f_file)

            try:
                found_index = model.predict(img)[1]
            except ValueError:
                form = UploadPhotoForm()
                return render(request, 'igarden/search.html', {
                    'form': form,
                    'error_message': 'Error processing image'
                })

            try:
                found_flower = Flower.objects.filter(id=found_index)[0]
                return render(request, 'igarden/detail.html', {'flower': found_flower})
            except IndexError:
                form = UploadPhotoForm()
                return render(request, 'igarden/search.html', {
                    'form': form,
                    'error_message': 'Error retrieving flower'
                })
    else:
        form = UploadPhotoForm()
    return render(request, 'igarden/search.html', {'form': form})


def detail(request):
    if request.method == 'POST':
        form = Choose_flower(request.POST)
        if form.is_valid():
            chosen_flower = form.cleaned_data.get('element')
            chosen_flower = Flower.objects.filter(id=chosen_flower.id)[0]
        return render(request, 'igarden/detail.html', {'flower': chosen_flower})
    else:
        form = Choose_flower()
        return render(request, 'igarden/explore.html', {'form': form})


def add_to_list(request):
    if request.method == 'POST':
        form = AddToListForm(request.POST)
        if form.is_valid():
            #obj = flower
            obj = Flower.objects.filter(name="Pansy")[0]
            chosen_list = form.cleaned_data.get('element')
            chosen_list = UserFlowersList.objects.filter(name=chosen_list.name)[0]
            chosen_list.elements.add(obj)
            messages.success(request, f"Flower has been added to the list successfully!")
        return render(request, 'lists/list_detail.html', {'object': chosen_list})
    else:
        form = AddToListForm()
        return render(request, 'igarden/list_add.html', {'form': form})
