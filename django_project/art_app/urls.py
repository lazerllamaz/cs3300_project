from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("inventory/", include("art_app.urls")),
    path("admin/", admin.site.urls),
    
]