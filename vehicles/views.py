from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets

from .serializers import VehicleSerializer, VehicleTypeSerializer
from . models import Vehicle, VehicleType

from core.permissions import IsOwnerOfVehicleOrRecord


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(owner__user=user)


class VehicleTypeSerializer(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
