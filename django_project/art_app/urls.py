from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalogue/", include("art_app.urls")),
]