from rest_framework import serializers
from inventorymanagement.models import Category,Inventory,Reorder

class InventorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Inventory
      fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
   inventory_data = InventorySerializer(many=True, read_only=True)
   class Meta:
      model = Category
      fields = '__all__'
      extra_kwargs = {'total_amount':{'read_only':True}}

class ReorderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Reorder
      fields = '__all__'
