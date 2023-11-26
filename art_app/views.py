#polls/views.py in Django tutorial

from typing import Any
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.views import generic
from .models import Inventory, Item
from .forms import ItemForm

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


def createItem(request, inventory_id):
    form = ItemForm()
    inventory = Inventory.objects.get(pk=inventory_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and inventory_id
        project_data = request.POST.copy()
        project_data['inventory_id'] = inventory_id
        
        form = ItemForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the inventory relationship
            project.inventory = inventory
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('inventory-detail', inventory_id)

    context = {'form': form}
    return render(request, 'art_app/item_form.html', context)