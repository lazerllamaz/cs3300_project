from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("inventories/", views.InventoryListView.as_view(), name="inventories"),
    path("inventories/<int:inventory_id>/", views.InventoryDetailView, name="inventory-detail"),

    path("items/<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),
]