from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    #Inventory list and detail views
    path("inventories/", views.InventoryListView.as_view(), name="inventories"),
    path("inventories/<int:inventory_id>/", views.InventoryDetailView, name="inventory-detail"),

    #item detail view
    path("items/<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),

    #create item form
    path('inventories/<int:inventory_id>/create_item/', views.createItem, name='create_item'),
]