from django.urls import path
from .views import (
    CameraListView,
    CameraDetailView,
    CameraCreateView,
    CameraUpdateView,
    CameraDeleteView,
)

urlpatterns = [
    path('', CameraListView.as_view(), name='product_list'),
    path('product/<int:pk>/', CameraDetailView.as_view(), name='product_detail'),
    path('product/add/', CameraCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', CameraUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', CameraDeleteView.as_view(), name='product_delete'),
]


