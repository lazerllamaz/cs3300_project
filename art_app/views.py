#polls/views.py in Django tutorial

from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse


from .models import Inventory, Item
from .forms import ItemForm, NewUserForm

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

# Create an item
def createItem(request, inventory_id):
    
    # Get related inventory for item
    inventory = Inventory.objects.get(pk=inventory_id)

    if request.method == 'POST':

        # Create a new dictionary with form data and inventory_id
        project_data = request.POST.copy()
        project_data['inventory_id'] = inventory_id
        
        form = ItemForm(project_data, request.FILES)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the inventory relationship and save
            project.inventory = inventory
            project.save()

            # Redirect back to the inventory detail page
            return redirect('inventory-detail', inventory_id)
    form = ItemForm()
    context = {'form': form}
    return render(request, 'art_app/add_item.html', context)

# Edit an existing item
def editItem(request, item_id):
    myItem = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        # request.FILES is REQUIRED for HTML to accept images
        form = ItemForm(request.POST, request.FILES, instance=myItem)
        
        if form.is_valid():
            form.save()
            return redirect('item-detail', myItem.pk)
    
    else:
        form = ItemForm(instance=myItem)

    return render(request, "art_app/edit_item.html", {"form": form})

#delete an item
def deleteItem(request, item_id):
    
    item = Item.objects.get(pk=item_id)
    item.delete()
    return  HttpResponseRedirect(reverse('inventories'))

#register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("index")
    
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', context={'form': form})
   