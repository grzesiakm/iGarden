from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from PIL import Image

from model.model import Model
from .models import Flower, UserFlowersList
from .forms import UploadPhotoForm, CreateListForm

def home(request):
    return render(request, 'igarden/home.html')


@method_decorator(login_required, name='dispatch')
class Lists(generic.ListView):
    model = UserFlowersList
    template_name = 'igarden/lists.html'

    def get_queryset(self):
        return UserFlowersList.objects.filter(owner=self.request.user)


@login_required
def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            new_list = UserFlowersList()
            new_list.name = form.cleaned_data['name']
            new_list.owner = request.user
            new_list.save()
            for item in form.cleaned_data['elements']:
                obj = Flower.objects.filter(name=item)[0]
                new_list.elements.add(obj)
        return render(request, 'igarden/create_list.html', {'form': form})
    else:
        form = CreateListForm()
        return render(request, 'igarden/create_list.html', {'form': form})


class Explore(generic.ListView):
    model = Flower
    template_name = 'igarden/explore.html'

    def get_queryset(self):
        return Flower.objects.all()


@login_required
def fav(request):
    # TODO make this work
    return render(request, 'igarden/base.html')

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
