
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    # orders/urls.py
    path('create/', views.order_create, name='order-create'),
        path('create/', views.order_create, name='order_create'),

    # path('process/', views.process, name='process'),
    # path('summary/', views.order_summary, name='order_summary'),
    
]
