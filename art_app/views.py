#polls/views.py in Django tutorial

from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from .models import Inventory, Item
from .forms import ItemForm

# Create your views here.

# Default view /home/
def index(request):
    return render(request, "art_app/index.html")

class InventoryListView(generic.ListView):
    model = Inventory

class ItemListView(generic.ListView):
    model = Item
class ItemDetailView(generic.DetailView):
    model = Item

