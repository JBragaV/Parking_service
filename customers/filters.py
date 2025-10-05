from dj_rql.filter_cls import AutoRQLFilterClass

from .models import Customer


class CustomersFilter(AutoRQLFilterClass):
    MODEL = Customer
