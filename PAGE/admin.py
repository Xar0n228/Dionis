from django.contrib import admin

from .models import *

# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 0

# class SubscriberAdmin (admin.ModelAdmin):
#     # list_display = ["name", "email"]
#     list_display = [field.name for field in Subscriber._meta.fields]
#     list_filter = ['name']
#     search_fields = ['name', 'email']
#
#     fields = ["email"]
#
#     # exclude = ["email"]
# 	# inlines = [FieldMappingInline]
# 	# fields = []
#     # #exclude = ["type"]
# 	# #list_filter = ('report_data',)
# 	# search_fields = ['category', 'subCategory', 'suggestKeyword']
#
#     class Meta:
#         model = Subscriber
#
# admin.site.register(Subscriber, SubscriberAdmin)


class AdminAdminData(admin.ModelAdmin):
    list_display = [field.name for field in A_D._meta.fields]
    class Meta:
        model = A_D
admin.site.register(A_D, AdminAdminData)








# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['image']
#     fields = ['image']
#
#     class Meta:
#         model = ProductImage
#
# admin.site.register(ProductImage, ProductImageAdmin)

# class AddTovarImageInline(admin.ModelAdmin):
#     list_display = [field.name for field in TovarImage._meta.fields]
#     class Meta:
#         model = TovarImage
#
# admin.site.register(TovarImage, AddTovarImageInline)
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
