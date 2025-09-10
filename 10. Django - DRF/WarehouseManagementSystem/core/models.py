import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.product_name} ({self.product_code})"


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)  # masalan: m², dona, m

    def __str__(self):
        return f"{self.material_name} ({self.unit})"


class ProductMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="materials")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="products")
    quantity = models.FloatField()  # qancha xomashyo kerak (masalan 0.8 m² mato)

    def __str__(self):
        return f"{self.product.product_name} → {self.material.material_name} ({self.quantity} {self.material.unit})"


class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="warehouses")
    remainder = models.FloatField()  # omborda nechta qolgan
    price = models.DecimalField(max_digits=12, decimal_places=2)
    batch_number = models.CharField(max_length=50, blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.material.material_name} | {self.remainder} {self.material.unit} | {self.price} so'm"