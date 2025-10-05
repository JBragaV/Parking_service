from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomersSerializer
from .filters import CustomersFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer
    rql_filter_class = CustomersFilter
    permission_classes = [DjangoModelPermissions, IsAdminUser]
