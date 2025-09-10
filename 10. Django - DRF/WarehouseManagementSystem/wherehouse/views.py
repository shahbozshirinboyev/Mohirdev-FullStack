from rest_framework import generics
from core.models import Warehouse
from .serializers import WarehouseSerializer, OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import calculate_materials
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WarehouseListAPIView(generics.ListAPIView):
  queryset = Warehouse.objects.all()
  serializer_class = WarehouseSerializer


class ProductionCalculateAPIView(APIView):
  @swagger_auto_schema(
        request_body=OrderItemSerializer(many=True),
        responses={200: openapi.Response("Hisoblangan natija")}
    )

  def post(self, request, *args, **kwargs):
    serializer = OrderItemSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    orders = serializer.validated_data
    result = calculate_materials(orders)
    return Response(result)
