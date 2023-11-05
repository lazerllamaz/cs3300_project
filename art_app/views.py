#polls/views.py in Django tutorial

from typing import Any
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.views import generic
from .models import Inventory, Item
from .forms import ItemForm

from django.db.models import prefetch_related_objects

# Create your views here.

# Default view /home/
def index(request):
    return render(request, "art_app/index.html")

class InventoryListView(generic.ListView):
    model = Inventory

def InventoryDetailView(request, inventory_id):

    inventory = Inventory.objects.get(id=inventory_id)

    item_list = Item.objects.filter(inventory=inventory)

    return render(request, "art_app/inventory_detail.html", {"inventory" : inventory, "item_list" : item_list})


class ItemListView(generic.ListView):
    model = Item
class ItemDetailView(generic.DetailView):
    model = Item