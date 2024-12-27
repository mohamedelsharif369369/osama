from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name='products'),
    path('edit_products/<int:pk>/',views.edit_products,name='edit-products'),
    path('delete_products/<int:pk>/',views.delete_products,name='delete-products'),
]