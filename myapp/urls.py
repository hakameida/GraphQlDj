from django.urls import path
from .views import get_laptops, get_laptop_detail

urlpatterns = [
    path('laptops/', get_laptops, name='laptop-list'),
    path('laptop/<int:laptop_id>/', get_laptop_detail, name='laptop-detail'),
]
