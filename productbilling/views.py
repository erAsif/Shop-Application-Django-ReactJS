from django.shortcuts import render
from .models import InvoiceModel,PaymentModel,FinancialModel
from django.db.models import Sum

from .serializers import InvoiceSerializer,PaymentSerializer,FinancialSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class InvoiceView(viewsets.ModelViewSet):
    # authenticate
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializer

class PaymentView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['post','get']
    filter_backends = [SearchFilter]
    search_fields = ['paymentstetus','created_at']


class CustomerStatementView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get']

class ServiceReportView(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['services']

class FinancialView(viewsets.ModelViewSet):
    # authentication_classes = [ BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = FinancialModel.objects.all()
    serializer_class = FinancialSerializer
    http_method_names = ['get'] 
    
