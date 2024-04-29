from django.urls import path
from crud_app import views


urlpatterns = [
    path('lcv/', views.laptop_create_view, name='add_url'),
    path('lrv/', views.laptop_retrieve_view, name='retrieve_url'),
    path('luv/<int:pk>/', views.laptop_update_view, name='update_url'),
    path('ldv/<int:pk>/', views.laptop_delete_view, name='delete_url')
]
