from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Laptop
from .serializers import LaptopMinimalSerializer, LaptopDetailSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_laptops(request):
    laptops = Laptop.objects.all()
    serializer = LaptopMinimalSerializer(laptops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    serializer = LaptopDetailSerializer(laptop)
    return Response(serializer.data)
