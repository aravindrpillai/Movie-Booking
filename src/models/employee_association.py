from django.db import models
from src.models.employees import Employees
from src.models.agency import Agency
from src.models.branches import Branches

class EmployeeAssociation(models.Model):
    employee = models.ForeignKey(Employees, null=False, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, null=False, on_delete=models.RESTRICT)
    branch = models.ForeignKey(Branches, null=False, on_delete=models.RESTRICT)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    roles = models.JSONField(null=True)
    
    class meta:
        db_name = "employee_association"
        verbose_name = "employee_association"

    