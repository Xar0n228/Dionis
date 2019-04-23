
from .models import *
from django.contrib import admin
from TOWARS.admin import TovarsInline

# Register your models here.
class TowarOrderModelInline(admin.TabularInline):
    model = TowarOrderModel
    extra = 0


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['myStatus']

    class Meta:
        model = OrderStatus
admin.site.register(OrderStatus, OrderStatusAdmin)


class TowarInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TowarOrderModel._meta.fields]
    class Meta:
        model = TowarOrderModel
admin.site.register(TowarOrderModel, TowarInOrderAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [TowarOrderModelInline]
    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)