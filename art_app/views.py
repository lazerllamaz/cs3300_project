from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("howdy")