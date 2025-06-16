from django.shortcuts import render
from .serializers import ProductView
from .models import ProductModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class ProductUserDetailView(generics.RetrieveAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductView
    permission_classes=[IsAuthenticated]

class ProductUserView(generics.ListAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductView
    permission_classes=[IsAuthenticated]

class ProductAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductView
    permission_classes=[IsAdminUser]

class ProductAdminCreate(generics.CreateAPIView):
    queryset=ProductModel.objects.all()
    serializer_class=ProductView
    permission_classes=[IsAdminUser]

