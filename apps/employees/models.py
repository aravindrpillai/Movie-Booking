from django.db import models

class Employees(models.Model):
    employee_id = models.UUIDField(unique=True)
    full_name = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=10, null=False, unique=True)

    class Meta:
        db_table = "employees"
        verbose_name = "employees"