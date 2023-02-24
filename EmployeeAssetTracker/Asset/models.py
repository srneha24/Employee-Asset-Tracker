from django.db import models

from Company.models import Employee

# Create your models here.
class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    asset_name = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        managed = True
        db_table = "asset"

class Delegation(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, db_column='employee', blank=False)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, db_column='asset', blank=False)
    delegation_time = models.DateTimeField(null=False, blank=False)
    delegated_condition = models.TextField(null=False, blank=False)
    delegated_condition_image = models.ImageField(upload_to="images/delegated_asset/")
    assigned_return_time = models.DateTimeField(null=False, blank=False)
    actual_return_time = models.DateTimeField(null=True, blank=True, default=None)
    returned_condition = models.TextField(null=True, blank=True, default=None)
    returned_condition_image = models.ImageField(upload_to="images/returned_asset/")

    class Meta:
        managed = True
        db_table = "delegation"
