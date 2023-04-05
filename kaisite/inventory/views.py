from django.views.generic.base import TemplateView
from .models import Item
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'inventory_list.html'
