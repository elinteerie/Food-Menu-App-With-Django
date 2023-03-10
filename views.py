from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from django.template import loader
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,

    }
    return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)


class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html/'


@login_required
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item_form.html', {'form': form})


class CreateItem(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'food/item_form.html'

    def formvaild(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


@login_required
def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item_form.html', {'form': form, 'item': item})


@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item_delete.html', {'item': item})
