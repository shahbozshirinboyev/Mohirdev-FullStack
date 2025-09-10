from django.urls import path
from .views import WarehouseListAPIView, ProductionCalculateAPIView

urlpatterns = [
    path("warehouse/", WarehouseListAPIView.as_view(), name="warehouse-list"),
    path("calculate-materials/", ProductionCalculateAPIView.as_view(), name="calculate-materials"),
]
