from rest_framework import serializers
from .models import ProductModel

class ProductView(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields=["id","name","description","price","stock","category","image"]

    