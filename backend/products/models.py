from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    category=models.CharField(max_length=200)
    image=models.ImageField()
