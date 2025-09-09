from django.contrib import admin

from vehicles.models import Vehicle, VehicleType


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = 'id', 'license_plate', 'brand', 'model', 'color'
    search_fields = 'license_plate', 'model'
    list_filter = 'vehicle_type',


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'description'
    search_fields = 'name',
