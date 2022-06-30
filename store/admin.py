from django.contrib import admin

from .models import (
    Supplier,
    Yard,
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class YardAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Yard, YardAdmin)
