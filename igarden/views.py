from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Flower, List
from model.model import Model
from PIL import Image

from model.model import Model
from .models import Flower
from .forms import UploadPhotoForm

def home(request):
    return render(request, 'igarden/home.html')

def lists(request):
    context = {
        'flowers': List.objects.all()
    }
    return render(request, 'igarden/lists.html', context)


class FlowerListView(ListView):
    model = List
    template_name = 'igarden/lists.html'
    context_object_name = 'flowers'
    ordering = ['-date_searched']


class FlowerDetailView(DetailView):
    model = List


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    fields = ['flower_name', 'date_searched']
<<<<<<< Updated upstream
=======

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = List
    fields = ['flower_name', 'date_searched']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test(self):
        flower = self.get_object()
        if self.request.user == flower.author:
            return True
        return False


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = List
    success_url = '/'

    def test(self):
        flower = self.get_object()
        if self.request.user == flower.author:
            return True
        return False
>>>>>>> Stashed changes

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = List
    fields = ['flower_name', 'date_searched']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test(self):
        flower = self.get_object()
        if self.request.user == flower.author:
            return True
        return False


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = List
    success_url = '/'

    def test(self):
        flower = self.get_object()
        if self.request.user == flower.author:
            return True
        return False

def search(request):
    model = Model()
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            f_file = request.FILES['file']
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
