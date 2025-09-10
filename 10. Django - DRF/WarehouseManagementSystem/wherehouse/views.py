from rest_framework import generics
from core.models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import calculate_materials

class WarehouseListAPIView(generics.ListAPIView):
  queryset = Warehouse.objects.all()
  serializer_class = WarehouseSerializer

class ProductionCalculateAPIView(APIView):
  def post(self, request):
      data = request.data  # [{product_code, quantity}, ...]
      result = calculate_materials(data)
      return Response(result)
