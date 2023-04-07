from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import CreateView, DeleteView,DetailView, ListView, UpdateView
from .models import Item
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = 'inventory_list.html'
    model = Item

class ItemCreateView(CreateView):
    template_name = 'item_create.html'
    model = Item
    fields = ['name', 'description', 'picker','barcode_number']

class ItemUpdateView(UpdateView):
  template_name = 'item_update.html'
  model = Item
  fields = "__all__"

class ItemDeleteView(DeleteView):
  template_name = 'item_delete.html'
  model = Item
  success_url = reverse_lazy("inventory_list")

class ItemDetailView(DetailView):
  template_name = 'item_detail.html'
  model = Item
