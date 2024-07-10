from django.db import models
from src.models.branches import Branches

class Screens(models.Model):
    branch = models.ForeignKey(Branches, null=False, on_delete=models.RESTRICT)
    number = models.CharField(max_length=10,null=False)

    class meta:
        db_table = "screens"
        verbose_name = "screens"
        unique_together = ("branch", "number")

