from rest_framework.routers import DefaultRouter
from django.urls import path,include
from app.views import CustomerViewSet, FoodViewSet

router = DefaultRouter()

router.register(r'customer' ,CustomerViewSet)
router.register(r'food' ,FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
