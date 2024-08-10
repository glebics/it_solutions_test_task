from django.urls import path, include
from .views import car_list_create, car_detail, car_update_delete

urlpatterns = [
    path('cars/', car_list_create, name='car-list-create'),
    path('cars/<int:pk>/', car_detail, name='car-detail'),
    path('cars/<int:pk>/edit/', car_update_delete, name='car-update-delete'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
