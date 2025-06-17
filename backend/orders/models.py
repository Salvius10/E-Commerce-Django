from django.db import models
from django.contrib.auth.models import User
from products.models import ProductModel
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered_at=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=200,default="Pending")



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price_at_purchase_time=models.DecimalField(max_digits=10, decimal_places=2)


