from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemSerializer,CartSerializer
from .models import Cart,CartItem
# Create your views here.

class CartView(generics.ListAPIView):
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Cart.objects.filter(user=user)
    

class CartItemAddView(generics.CreateAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self,serializer):
        user=self.request.user
        cart,created=Cart.objects.get_or_create(user=user)
        serializer.save(cart=cart)

class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return CartItem.objects.filter(cart__user=user)