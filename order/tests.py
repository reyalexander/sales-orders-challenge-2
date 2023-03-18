from django.test import TestCase
from .models import Order
from django.contrib.auth.models import User

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        Order.objects.create(
            id_user=cls.user,
            order_code='ORDER001',
            total_price=10.00,
            status='PROCESSING'
        )

    def test_order_fields(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.id_user, self.user)
        self.assertEqual(order.order_code, 'ORDER001')
        self.assertEqual(order.total_price, 10.00)
        self.assertEqual(order.status, 'PROCESSING')

    def test_order_created_at(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.created_at)

    def test_order_updated_at(self):
        order = Order.objects.get(id=1)
        order.status = 'COMPLETED'
        order.save()
        self.assertIsNotNone(order.updated_at)