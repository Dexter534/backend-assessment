from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from .models import Supplier, Inventory


class TestCases(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier  = Supplier.objects.create(
            name="The Supplier",
        )
        self.inventory  = Inventory.objects.create(
            name="The item",
            description="The description",
            note="This is a note",
            stock=23,
            availability=True,
            supplier_id=1        
        )

    def testInventoryList(self):
        response = self.client.get(reverse('inventoryList'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testInventoryAPI(self):
        response = self.client.get(reverse('inventoryAPI'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testInventoryDetails(self):
        response = self.client.get(reverse('inventoryDetails', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)