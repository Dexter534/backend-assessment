from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Inventory, Supplier
from .serializers import InventorySerializer, InventoryListSerializer, SupplierSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class InventoryAPIView(APIView):
    def get(self, request, format=None):
        if request.GET.get("name"): # If there is query parameter, find the object
            inventory_name = request.GET.get("name")
            inventory = Inventory.objects.filter(name = inventory_name)
        else: # Else just show all
            inventory = Inventory.objects.all()

        serializer = InventoryListSerializer(inventory, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class InventoryDetailsView(APIView):

    # Template Renderer to render data into the template
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, id, format=None):
        inventory = get_object_or_404(Inventory, pk=id) # Shortcut to show 404 if the object is not found
        serializer = InventorySerializer(inventory)
        return Response(serializer.data,template_name='inventory_details.html', status=status.HTTP_200_OK)


def inventoryList(request):
    inventory_view = InventoryAPIView()
    response = inventory_view.get(Request(request)) # This view gets it's data from the DRF API View
    return render(request, 'inventory_list.html', {"inventory": response.data}, status=status.HTTP_200_OK)