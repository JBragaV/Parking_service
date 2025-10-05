from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets

from core.permissions import IsOwnerOfVehicleOrRecord

from .models import ParkingSpot, ParkingRecord
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(vehicle__owner__user=user)
