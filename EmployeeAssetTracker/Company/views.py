from django.shortcuts import render
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

import logging, json

from .serializers import CompanySerializer, CompanyLoginSerializer, EmployeeCreateSerializer, EmployeeSerializer
from .models import Employee

log = logging.getLogger('main')

"""
I used FBV for the Company model and CBV for the Employee model CRUD operations as in my interpretation of the system, the
Company model is used in different ways for the REST calls, through different URLs. But the employee model works under the same URL
all across the board.
"""

# Create your views here.
@transaction.atomic
@api_view(['POST'])
def add_company(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        jsonString = json.dumps(serializer.validated_data, default=str)
        log.debug("New Company: " + jsonString)

        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    else:
        log.error("Validation Error")

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def company_login(request):
    serializer = CompanyLoginSerializer(data=request.data)

    if serializer.is_valid():
        jsonString = json.dumps(serializer.data, default=str)
        log.debug("Logging In: " + jsonString)

        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    else:
        log.error("Validation Error")

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

class EmployeeView(APIView):
    @transaction.atomic
    def post(self, request, format=None):
        serializer = EmployeeCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            jsonString = json.dumps(serializer.validated_data, default=str)
            log.debug("New Employee: " + jsonString)

            serializer.set_employee_company(request.session.get("company"))

            serializer.save()

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            log.error("Validation Error")

            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request, id, format=None):
        try:
            employee = Employee.objects.get(id)
            serializer = EmployeeSerializer(employee)

            jsonString = json.dumps(serializer.data, default=str)
            log.debug("Employee: " + jsonString)

            return Response(serializer.data, status=status.HTTP_302_FOUND)
        
        except:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


