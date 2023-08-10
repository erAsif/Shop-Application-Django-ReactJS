from .serializers import CategorySerializer,InventorySerializer,ReorderSerializer
from .models import Category,Inventory,Reorder
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
# authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class InventoryView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class CategoryView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class LowstockView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    http_method_names = ['get']
    def get_queryset(self):
        lowstock_list = self.queryset
        lowstock_list = lowstock_list.filter(quantity__lte= 11)
        return lowstock_list

class ReorderView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reorder.objects.all()
    serializer_class = ReorderSerializer
    http_method_names = ['post']

class ReportView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
  
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category']
    search_fields = ['=category']

class Search(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inventory.objects.filter()
    serializer_class = InventorySerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name' ]
    search_fields = ['=name']
