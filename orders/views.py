from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from common.views import TitleMixin
from orders.forms import OrderForm
from orders.models import Order


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders.html'
    title = 'U-STYLE Orders'
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderCreateVIew(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Order making'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateVIew, self).form_valid(form)