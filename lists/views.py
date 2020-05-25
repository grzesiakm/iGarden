from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Flower, UserFlowersList
from .forms import CreateListForm, AddToListForm


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
        return redirect('lists-all')
    else:
        form = CreateListForm()
        return render(request, 'lists/list_create.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ListDetailView(generic.DetailView):
    model = UserFlowersList
    template_name = 'lists/list_detail.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(UserFlowersList, id=id_)


@method_decorator(login_required, name='dispatch')
class ListDeleteView(generic.DeleteView):
    model = UserFlowersList
    template_name = 'lists/list_delete.html'
    success_url = reverse_lazy('lists-all')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(UserFlowersList, id=id_)

@login_required
def fav(request):
    # TODO make this work
    return render(request, 'igarden/base.html')