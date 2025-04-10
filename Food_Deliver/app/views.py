from rest_framework import viewsets
from app.models import OrdersFood, Customer
from app.serializers import FoodSerializers, CustomerSerializers
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    
    
    
class FoodViewSet(viewsets.ModelViewSet):
    queryset = OrdersFood.objects.all()
    serializer_class = FoodSerializers