from rest_framework import serializers

from .models import Asset, Delegation

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'

class DelegationSeriializer(serializers.ModelSerializer):

    class Meta:
        model = Delegation
        fields = '__all__'

class AssetStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delegation
        fields = ['delegation_time', 'delegated_condition', 'delegated_condition_image', 
                  'assigned_return_time', 'actual_return_time', 'returned_condition', 'returned_condition_image']

class AssetLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delegation
        fields = ['delegated_condition', 'delegated_condition_image', 
                  'actual_return_time', 'returned_condition', 'returned_condition_image']
