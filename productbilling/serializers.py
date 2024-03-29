from .models import *
from rest_framework import serializers
from inventorymanagement.serializers import CategorySerializer,InventorySerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    payment_data = PaymentSerializer(many=True,read_only=True)
    class Meta:
        model = InvoiceModel
        fields = '__all__'
        extra_kwargs = {'total_purchage':{'read_only':True}}

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialModel
        fields = '__all__'
        extra_kwargs = {'financial_amount':{'read_only':True}}
