from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from products.models import ProductModel
from products.serializers import ProductView
from orders.serializers import OrderSerializer
from orders.models import Order
from carts.serializers import CartSerializer
from carts.models import Cart

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class ProfileUserView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user

class AdminUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAdminUser]

class AdminUserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAdminUser]

class AdminProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductView
    permission_classes=[IsAdminUser]

class AdminOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAdminUser]

class AdminCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    permission_classes=[IsAdminUser]