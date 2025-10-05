from rest_framework import serializers

from .models import Customer


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
