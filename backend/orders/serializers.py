from rest_framework import serializers
from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=["id","product","quantity","price_at_purchase_time"]

class OrderSerializer(serializers.ModelSerializer):
    ordered_items=OrderItemSerializer(source="orderitem_set",many=True,read_only=True)
    class Meta:
        model=Order
        fields=["id","user","ordered_items","ordered_at","total_price","status"]
        read_only_fields = ["user", "total_price", "ordered_at", "status", "ordered_items"]