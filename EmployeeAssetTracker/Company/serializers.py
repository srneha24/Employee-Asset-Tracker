from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

from .models import Company, Employee

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        # Hashing the password
        validated_data['password'] = make_password(validated_data['password'])

        # Call the parent create() method to create the model instance
        instance = super().create(validated_data)

        return instance

class CompanyLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        try:
            company = Company.objects.get(username=data['username'])
            
            # Matching the password
            if check_password(data['password'], company.password):
                return company
            else:
                raise serializers.ValidationError("Company not found")
        except Company.DoesNotExist:
            raise serializers.ValidationError("Company not found.")

"""
The EmployeeCreateSerializer class has been written considering that the company is already signed in and adding in a new
employee of theirs to the system. So, the id of the company is saved in a session variable on the client side, and is retrieved
from there in the view. 
"""


class EmployeeCreateSerializer(serializers.ModelSerializer):

    def set_employee_company(self, company):
        self.company = company

    def create(self, validated_data):
        # Add the company
        validated_data['company'] = self.company

        # Call the parent create() method to create the model instance
        instance = super().create(validated_data)

        return instance
    
    class Meta:
        model = Employee
        fields = ['employee_name', 'designation']

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
