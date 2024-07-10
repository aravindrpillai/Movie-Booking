from django.db import models

class EmployeeCredentials(models.Model):
    password = models.CharField(max_length=40)
    pwd_last_updated = models.DateField(null=False)
    failed_attempts = models.IntegerField(null=False,default=0)
    locked = models.BooleanField(default=False)

    class meta:
        db_table = "employee_credentials"
        verbose_name = "employee_credentials"


        