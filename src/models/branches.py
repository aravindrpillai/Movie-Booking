from django.db import models
from src.models.agency import Agency

class Branches(models.Model):
    branch_id = models.CharField(max_length=6, unique=True, null=False)
    agency = models.ForeignKey(Agency, null=False, on_delete=models.RESTRICT)
    address = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    pincode = models.CharField(max_length=7, null=False)
    maps_url = models.URLField(null=True)

    class meta:
        db_table = "branches"
        verbose_name = "branches"
        unique_together = ("agency", "pincode")
        