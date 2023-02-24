from .models import Asset

from django.db import connection

def reduce_quantity(id):
    asset = Asset.objects.get(id=id)

    asset.quantity = asset.quantity - 1

    asset.save()

def increase_quantity(id):
    asset = Asset.objects.get(id=id)

    asset.quantity = asset.quantity + 1

    asset.save()

def get_delegation(asset):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM delegation WHERE asset = %s ORDER BY id DESC LIMIT 1", [asset])
        result = cursor.fetchall()
        if result[0][0] is None:
            result = None
        else:
            result = result[0][0]
    
    return result
