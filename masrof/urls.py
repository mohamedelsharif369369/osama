from django.urls import path
from . import views

urlpatterns = [
    path('',views.masrof,name='masrof'),
    path('edit_masrof/<int:pk>/',views.edit_masrof,name='edit-masrof'),
    path('delete_masrof/<int:pk>/',views.delete_masrof,name='delete-masrof'),
]