from django.contrib import admin

from ProductApp.models import CatagoryModel
from ProductApp.models import ProductModel

# Register your models here.
class CataogryAdmin(admin.ModelAdmin):
    list_display=['name']
    list_filter=['name']
admin.site.register(CatagoryModel,CataogryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price']
admin.site.register(ProductModel,ProductAdmin)