from rest_framework import serializers
from core.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material.material_name", read_only=True)
    unit = serializers.CharField(source="material.unit", read_only=True)

    class Meta:
        model = Warehouse
        fields = ["id", "material_name", "unit", "remainder", "price", "batch_number", "received_date"]

class OrderItemSerializer(serializers.Serializer):
    product_code = serializers.IntegerField(help_text="Mahsulot kodi")
    quantity = serializers.IntegerField(min_value=1, help_text="Buyurtma miqdori")

    class Meta:
        swagger_schema_fields = {
            "example": {
                "product_code": 123456788,
                "quantity": 30
            }
        }

class OrderListSerializer(serializers.Serializer):
    orders = OrderItemSerializer(many=True)
