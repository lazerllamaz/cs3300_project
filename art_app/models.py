from django.db import models



class Inventory(models.Model):
    
    title = models.CharField(max_length=100)


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
    itemType = models.CharField(
        max_length=10,
        choices=ITEM_TYPES,
        default=MATERIAL,
    )

    #many-to-one relationship with inventory (many items in 1 inventory)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)