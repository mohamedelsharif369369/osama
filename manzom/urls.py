from django.urls import path
from . import views 

urlpatterns = [
    path("", views.manzom, name="manzom"),
    path('edit_manzom/<int:pk>/',views.edit_manzom,name='edit-manzom'),
    path('delete_manzom/<int:pk>/',views.delete_manzom,name='delete-manzom'),
]