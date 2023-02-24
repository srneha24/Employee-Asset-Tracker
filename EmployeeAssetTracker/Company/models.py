from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, null=False, blank=False, unique=True)
    company_name = models.CharField(max_length=70, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'company'

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=20, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, db_column='company', blank=False)

    class Meta:
        managed = True
        db_table = 'employee'