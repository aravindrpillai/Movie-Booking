from django.db import models

class Customers(models.Model):
    customers_id = models.UUIDField(unique=True)
    full_name = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=10, null=False, unique=True)

    class Meta:
        db_table = "customers"
        verbose_name = "customers"