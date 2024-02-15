from django.shortcuts import render

from .models import Banner
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BannerSerializer

@api_view(['GET'])
def GetBanner(request , id):
    try:
        banner = Banner.objects.filter( id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BannerSerializer(banner , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBanners(request , category):
    try:
        banner = Banner.objects.filter( category=category).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BannerSerializer(banner , many=True)
    return Response(serializer.data)
