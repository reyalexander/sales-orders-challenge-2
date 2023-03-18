from .models import Order
from .serializer import OrderSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
