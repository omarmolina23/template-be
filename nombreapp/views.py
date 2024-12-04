from django.shortcuts import render

# Create your views here.

from .models import Product
from .serializers import ProductSerializer

#from django.http import JsonResponse
from django.core.serializers import serialize

from rest_framework import routers, serializers, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from utils.permissions import CustomDjangoModelPermissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    """
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_filters = ['description']
    filterset_fields = ['description']
    search_fields = ['id', 'description']
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    """
    