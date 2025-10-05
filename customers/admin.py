from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'phone', 'created_at'
    list_display_links = 'id', 'name'
    search_fields = 'id', 'name', 'phone', 'cpf'
