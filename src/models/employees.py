from django.db import models
from src.models.employee_credentials import EmployeeCredentials

class Employees(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, null=False)
    fullname = models.CharField(max_length=40, null=False)
    photo = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=False)
    lwd = models.DateField(null=True)
    active = models.BooleanField(default=False)
    email = models.EmailField(max_length=40, unique=True, null=True)
    mobile = models.CharField(max_length=10, unique=True, null=False)
    mobile_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class meta:
        db_table = "employees"
        verbose_name = "employees"


