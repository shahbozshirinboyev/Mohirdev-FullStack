from rest_framework import serializers
from core.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material.material_name", read_only=True)
    unit = serializers.CharField(source="material.unit", read_only=True)

    class Meta:
        model = Warehouse
        fields = ["id", "material_name", "unit", "remainder", "price", "batch_number", "received_date"]
