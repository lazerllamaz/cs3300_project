from django.contrib import admin
from .models import Inventory, Item

# Register your models here.

admin.site.register(Item)
admin.site.register(Inventory)