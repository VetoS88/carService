"""
    Главный роутер приложения
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = {
    path('cars', include('cars.urls')),
    path('admin/', admin.site.urls),
}
