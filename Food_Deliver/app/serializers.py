from rest_framework import serializers
from app.models import OrdersFood, Customer

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrdersFood
        fields = '__all__'
        
        
        
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'