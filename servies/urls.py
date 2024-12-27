from django.urls import path
from . import views

urlpatterns = [
    path('',views.servies,name='servies'),
    path('edit_servies/<int:pk>/',views.edit_servies,name='edit-servies'),
    path('delete_servies/<int:pk>/',views.delete_servies,name='delete-servies'),
]