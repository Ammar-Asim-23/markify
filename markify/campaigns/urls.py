from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('<int:pk>/send-mail',views.send_email, name='send_email' ),
    path('', views.campaigns_list, name='list')
    
]
