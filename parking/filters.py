from dj_rql.filter_cls import AutoRQLFilterClass

from .models import ParkingRecord, ParkingSpot


class ParkingRecordFilter(AutoRQLFilterClass):
    MODEL = ParkingRecord
    FILTERS = (
        {
            'filter': 'placa',
            'source': 'vehicle__license_plate',
        },
    )


class ParkingSoptFilter(AutoRQLFilterClass):
    MODEL = ParkingSpot
