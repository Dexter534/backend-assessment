from rest_framework import serializers
from .models import Supplier, Inventory

# Supplier serializer that will be used with inventory serializers
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']

# Serializer to show all fields for inventory
class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'

# This serializer is for the main inventory list page
class InventoryListSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    
    class Meta:
        model = Inventory
        fields = ['id','name','supplier','availability']