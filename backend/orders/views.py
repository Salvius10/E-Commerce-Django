from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderItemSerializer,OrderSerializer
from .models import Order,OrderItem
from carts.models import Cart,CartItem

# Create your views here.


class OrderView(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)
    

class OrderHistoryView(generics.ListAPIView):
    serializer_class=OrderItemSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return OrderItem.objects.filter(order__user=user)
    

class OrderCreateView(generics.CreateAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return  Order.objects.filter(user=user)
    def perform_create(self, serializer):
        user=self.request.user
        cart=Cart.objects.get(user=user)
        cart_items=CartItem.objects.filter(cart=cart)
        total_price=sum(item.quantity*item.product.price for item in cart_items)
        order=serializer.save(user=user,total_price=total_price)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase_time=item.product.price
            )
        cart_items.delete()


