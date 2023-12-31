from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.clients_list, name='list'),
    path('<int:pk>/', views.clients_detail, name='detail'),
    path('<int:pk>/edit/', views.edit_client, name='edit'),
    path('<int:pk>/delete/', views.clients_delete, name='delete'),
    path('<int:pk>/add-comment/', views.clients_detail, name='add_comment'),
    path('add/', views.add_client, name='add'),
    
]
