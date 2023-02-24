from django.urls import path

from .views import (
    new_asset,
    new_delegation,
    update_delegation_status,
    get_asset_status,
    get_asset_log
)

app_name = 'Asset'

urlpatterns = [
    path('new_asset', new_asset, name="NewAsset"),
    path('new_delegation', new_delegation, name='NewDelegation'),
    path('update_asset_delegation/<int:id>/', update_delegation_status, name="UpdateAssetStatus"),
    path('asset_status', get_asset_status, name="AssetStatus"),
    path('asset_log', get_asset_log, name="AssetLog")
]