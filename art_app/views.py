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
    return HttpResponse("howdy")