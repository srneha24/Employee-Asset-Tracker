from django.db import models

from Company.models import Employee

# Create your models here.
class Asset(models.Model):
    id = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        managed = False
        db_table = "asset"

class Delegation(models.Model):
    id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=False, blank=False)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, null=False, blank=False)
    delegation_time = models.DateTimeField(null=False, blank=False)
    delegated_condition = models.TextField(null=False, blank=False)
    assigned_returned_time = models.DateTimeField(null=False, blank=False)
    actual_returned_time = models.DateTimeField(null=False, blank=False)
    returned_condition = models.TextField(null=False, blank=False)

    class Meta:
        managed = False
        db_table = "delegation"
