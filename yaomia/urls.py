from django.urls import path
from . import views

urlpatterns = [
    path('',views.yaomia,name='yaomia'),
    path('edit_yaomia/<int:pk>/',views.edit_yaomia,name='edit-yaomia'),
    path('delete_yaomia/<int:pk>/',views.delete_yaomia,name='delete-yaomia'),
]