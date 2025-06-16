from django.db import models
from django.contrib.auth.models import User
from products.models import ProductModel
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    added_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
