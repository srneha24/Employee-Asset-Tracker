from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=70, null=False, blank=False)
    number_of_employees = models.IntegerField(null=False, blank=False, default=1)

    class Meta:
        managed = False
        db_table = 'company'

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'employee'