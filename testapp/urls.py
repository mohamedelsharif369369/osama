from django.urls import path
from .views import TestListView , TestDetailView , TestUpdateView , TestDeleteView , img , edit_img , delete_img

urlpatterns = [
    path('',TestListView.as_view(),name='test'),
    path('<int:pk>/',TestDetailView.as_view(),name='test-detail'),
    path('<int:pk>/update/',TestUpdateView.as_view(),name='test-update'),
    path('<int:pk>/delete/',TestDeleteView.as_view(),name='test-delete'),
    path('img/',img,name='img'),
    path('edit_img/<int:pk>/',edit_img,name='edit-img'),
    path('delete_img/<int:pk>/',delete_img,name='delete-img'),
]