from django.db import models
from src.models.agency import Agency

class BranchManager(models.Manager):
    def get_next_branch_id(self, agency):
        last_branch = self.filter(agency = agency).order_by('branch_id').last()
        if not last_branch:
            return agency.agency_id + 'B001'

        last_branch_id = last_branch.branch_id
        last_number = int(last_branch_id[5:])
        new_number = last_number + 1
        new_branch_id =  f'B{new_number:03d}'
        return agency.agency_id + new_branch_id
    
class Branches(models.Model):
    branch_id = models.CharField(max_length=8, unique=True, null=False)
    agency = models.ForeignKey(Agency, null=False, on_delete=models.RESTRICT)
    address = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    pincode = models.CharField(max_length=7, null=False)
    maps_url = models.URLField(null=True)

    objects = BranchManager()

    class meta:
        db_table = "branches"
        verbose_name = "branches"
        unique_together = ("agency", "pincode")


        