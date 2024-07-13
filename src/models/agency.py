from django.db import models

class AgencyManager(models.Manager):
    def get_next_agency_id(self):
        last_agency = self.all().order_by('agency_id').last()
        if not last_agency:
            return 'M001'

        last_agency_id = last_agency.agency_id
        last_number = int(last_agency_id[1:])
        new_number = last_number + 1
        new_agency_id =  f'M{new_number:03d}'
        return new_agency_id
    
class Agency(models.Model):
    agency_id = models.CharField(max_length=4, unique=True, null=False)
    name = models.CharField(max_length=30, null=False)
    website = models.URLField(max_length=40, null=True)
    email = models.EmailField(max_length=35, null=False)

    objects = AgencyManager()

    class meta:
        db_table = "agency"
        verbose_name = "agency"
        unique_together = ("name" , "email")