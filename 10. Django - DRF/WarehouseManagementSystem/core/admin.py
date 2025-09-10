from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_code")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("material_name", "unit")


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ("product", "material", "quantity")


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("material", "remainder", "price", "batch_number", "received_date")
