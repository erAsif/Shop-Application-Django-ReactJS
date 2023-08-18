from django.shortcuts import render
from .models import InvoiceModel,PaymentModel,FinancialModel
from django.db.models import Sum
from rest_framework.decorators import action

from .serializers import InvoiceSerializer,PaymentSerializer,FinancialSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from productbilling import models
from inventorymanagement.models import Category

# authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class InvoiceView(viewsets.ModelViewSet):
    # authenticate
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializer

    @action(detail=False, methods=['GET'])
    def financial_report(self, request):
        total_revenue = InvoiceModel.objects.aggregate(total=models.Sum('total_purchage'))['total']
        total_expenses = Category.objects.aggregate(total=models.Sum('total_amount'))['total']
        outstanding_balance  = total_revenue - total_expenses 

        return Response({'total_revenue': total_revenue,
                          'total_expenses': total_expenses,
                          'outstanding_balance': outstanding_balance
                          })
    @action(detail=False, methods=['GET'])
    def customer_statement(self, request):
        total_revenue = InvoiceModel.objects.aggregate(total=models.Sum('total_purchage'))['total']
        return Response({'total_revenue': total_revenue})

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
    
