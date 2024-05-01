from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventoryList, name='inventoryList'),
    path('inventory/<int:id>', views.InventoryDetailsView.as_view(), name='inventoryDetails'),
    path('api/inventory/', views.InventoryAPIView.as_view(), name='inventoryAPI')
]