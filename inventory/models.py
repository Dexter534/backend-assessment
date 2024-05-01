from django.db import models

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name