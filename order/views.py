from .models import Order
from .serializer import OrderSerializer
from rest_framework import viewsets

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
