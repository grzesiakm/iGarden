from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from PIL import Image
from model.model import Model
from .models import Flower, UserFlowersList
from .forms import CreateListForm


@method_decorator(login_required, name='dispatch')
class Lists(generic.ListView):
    model = UserFlowersList
    template_name = 'lists/lists.html'

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
        return render(request, 'lists/create_list.html', {'form': form})
    else:
        form = CreateListForm()
        return render(request, 'lists/create_list.html', {'form': form})


@login_required
def fav(request):
    # TODO make this work
    return render(request, 'igarden/base.html')
