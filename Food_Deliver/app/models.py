from django.db import models

# Create your models here.
class OrdersFood(models.Model):
    food_Name = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    
    