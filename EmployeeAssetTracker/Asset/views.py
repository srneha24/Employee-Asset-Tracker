from django.shortcuts import render
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema

import logging, json

from .serializers import AssetSerializer, DelegationSeriializer, AssetStatusSerializer, AssetLogSerializer
from .queries import increase_quantity, reduce_quantity, get_delegation
from .models import Delegation

log = logging.getLogger('main')

# Create your views here.
@extend_schema(responses=AssetSerializer)
@transaction.atomic
@api_view(['POST'])
def new_asset(request):
    serializer = AssetSerializer(data=request.data)

    if serializer.is_valid():
        jsonString = json.dumps(serializer.validated_data, default=str)
        log.debug("New Asset: " + jsonString)

        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    else:
        log.error("Validation Error")

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@extend_schema(responses=DelegationSeriializer)
@transaction.atomic
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def new_delegation(request):
    serializer = DelegationSeriializer(data=request.data)

    if serializer.is_valid():
        jsonString = json.dumps(serializer.validated_data, default=str)
        log.debug("Asset Delegated: " + jsonString)

        serializer.save()
        
        reduce_quantity(serializer.validated_data["asset"])

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    else:
        log.error("Validation Error")

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@extend_schema(responses=DelegationSeriializer)
@transaction.atomic
@api_view(['PATCH'])
@parser_classes([MultiPartParser, FormParser])
def update_delegation_status(request, id):
    delegation = Delegation.objects.get(id=id)
    serializer = DelegationSeriializer(delegation, data=request.data, partial=True)

    if serializer.is_valid():

        if serializer.validated_data["actual_return_time"] != None:
            increase_quantity(serializer.validated_data["asset"])
        
        jsonString = json.dumps(serializer.validated_data, default=str)
        log.debug("Updated Delegation Status: " + jsonString)

        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    else:
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@extend_schema(responses=AssetStatusSerializer)
@api_view(['GET'])
def get_asset_status(request, id):
    try:
        delegation = Delegation.objects.get(id=get_delegation(id))
        serializer = AssetStatusSerializer(delegation)

        jsonString = json.dumps(serializer.data, default=str)
        log.debug("Asset Status: " + jsonString)

        return Response(serializer.data, status=status.HTTP_302_FOUND)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@extend_schema(responses=AssetLogSerializer)
@api_view(['GET'])
def get_asset_log(request, id):
    try:
        delegation = Delegation.objects.get(id=get_delegation(id))
        serializer = AssetLogSerializer(delegation)

        jsonString = json.dumps(serializer.data, default=str)
        log.debug("Asset Log: " + jsonString)

        return Response(serializer.data, status=status.HTTP_302_FOUND)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
