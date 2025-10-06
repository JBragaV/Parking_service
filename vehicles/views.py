from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets

from core.permissions import IsOwnerOfVehicleOrRecord

from .serializers import VehicleSerializer, VehicleTypeSerializer
from . models import Vehicle, VehicleType
from .filters import VehicleFilter, VehicleTypeFilter


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilter
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(owner__user=user)


class VehicleTypeSerializer(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilter
    permission_classes = [DjangoModelPermissions, IsAdminUser]
