from django.db import models

class Agency(models.Model):
    agency_id = models.CharField(max_length=4, unique=True, null=False)
    name = models.CharField(max_length=30, null=False)

    class meta:
        db_table = "agency"
        verbose_name = "agency"