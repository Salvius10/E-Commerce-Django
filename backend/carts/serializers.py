from rest_framework import serializers
from .models import Cart,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    item_total=serializers.SerializerMethodField()
    class Meta:
        model=CartItem
        fields=["id","product","quantity","added_at","item_total"]

    def get_item_total(self,obj):
        return obj.quantity*obj.product.price


class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(source="cartitem_set",many=True,read_only=True)
    total=serializers.SerializerMethodField()
    class Meta:
        model=Cart
        fields=["id","user","created_at","items","total"]
    def get_total(self,obj):
        cart_items=obj.cartitem_set.all()
        return sum(item.quantity*item.product.price for item in cart_items)

