from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("inventories/", views.InventoryListView.as_view(), name="inventories"),
    path("inventories/<int:pk>/", views.ItemListView.as_view(), name="inventory-detail"),

    path("inventories/<int:inventory_id>/<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),
]