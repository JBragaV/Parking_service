from django.contrib import admin

from parking.models import ParkingSpot, ParkingRecord

admin.site.site_header = 'Administração do JOCIMAR'


@admin.register(ParkingRecord)
class ParkingRercordAdmin(admin.ModelAdmin):
    list_display = 'id', 'vehicle', 'parking_spot', 'entry_time', 'exit_time'
    list_display_links = 'id', 'vehicle', 'parking_spot'
    search_fields = 'vehicle__license_plate', 'parking_spot__spot_number'
    list_filter = 'vehicle', 'parking_spot'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = 'id', 'spot_number', 'is_occupied'
    list_display_links = 'id', 'spot_number'
    search_fields = 'spot_number', 'is_occupied'
    list_filter = 'is_occupied',
