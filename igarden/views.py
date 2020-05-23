from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from PIL import Image
from model.model import Model
from .models import Flower
from .forms import UploadPhotoForm


def home(request):
    return render(request, 'igarden/home.html')


def search(request):
    model = Model()
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            f_file = form.cleaned_data['file']
            print(f_file)
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


class Explore(generic.ListView):
    model = Flower
    template_name = 'igarden/explore.html'

    def get_queryset(self):
        return Flower.objects.all()