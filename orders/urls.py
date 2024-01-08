from django.urls import path
from . import views

from orders.views import OrderCreateVIew, OrderListView

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateVIew.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
]
