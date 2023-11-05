from django.db import models
from django.urls import reverse


class Inventory(models.Model):
    
    title = models.CharField(max_length=100)

    #Return default name of Inventory object
    def __str__ (self):
        return self.title
    
    #Return URL to access specific Inventory
    def get_absolute_url(self):
        return reverse("inventory-detail", args=[str(self.id)])


# Create your models here.
class Item(models.Model):

    PRODUCT = "FP"
    MATERIAL = "MT"
    WORK_IN_PROGRESS = "WIP"

    #Choices for item type: "DB-value", "readable name"
    ITEM_TYPES = [
    (PRODUCT, "Finished Product"),
    (MATERIAL, "Material"),
    (WORK_IN_PROGRESS, "Work in progress"),
    ]

    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    item_Type = models.CharField(
        max_length=10,
        choices=ITEM_TYPES,
        default=MATERIAL,
    )

    #Return default name of Item object
    def __str__ (self):
        return self.name
    
    #Return URL to access specific Item
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    #many-to-one relationship with inventory (many items in 1 inventory)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)