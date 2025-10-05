from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet, VehicleTypeSerializer


router = DefaultRouter()
router.register('vehicles/types', VehicleTypeSerializer)
router.register('vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
