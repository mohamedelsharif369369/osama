from django.urls import path
from . import views

urlpatterns = [
    path('',views.hesabi,name='hesabi'),
    path('edit_hesabi/<int:pk>/',views.edit_hesabi,name='edit-hesabi'),
    path('delete_hesabi/<int:pk>/',views.delete_hesabi,name='delete-hesabi'),
]