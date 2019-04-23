from django.contrib import admin
from .models import *

class TovarsInline(admin.TabularInline):
    model = Towar
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = ['mStatus']

    class Meta:
        model = Status
admin.site.register(Status, StatusAdmin)

class AddTovarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Towar._meta.fields]  # список названия столбцоа для отображения
    list_filter = ['status', 'category_new']  # для фильтрации поиска на сайте. Для удобства
    search_fields = ['tovar_key', 'name']
    readonly_fields = ['image_img', ]
    # inlines = [TovarsInline]

    # fields = ['name', 'zena', 'ves', 'description', 'image', 'image_img', 'status']  ################# отображение единицы записи

    class Meta:
        model = Towar
admin.site.register(Towar, AddTovarAdmin)



class CateAdm(admin.ModelAdmin):
    list_display = [field.name for field in Category_new._meta.fields]

    # fields = ['category_key']  # отображение единицы записи ################
    inlines = [TovarsInline]
    class Meta:
        model = Category_new
admin.site.register(Category_new, CateAdm)
