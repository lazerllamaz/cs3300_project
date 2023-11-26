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
    path('inventories/<int:inventory_id>/create_item/', views.createItem, name='create-item'),

    #Edit item form
    path('inventories/<int:item_id>/edit_item/', views.editItem, name='edit-item'),

    #delete item
    path('items/<int:item_id>/delete_item/', views.deleteItem, name='delete-item'),

    #User registration
    path('register', views.register, name='register')
]