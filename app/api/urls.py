from django.urls import path
from .views import car_list_create, car_detail

urlpatterns = [
    path('cars/', car_list_create, name='car_list_create'),
    path('cars/<int:pk>/', car_detail, name='car_detail'),
]
