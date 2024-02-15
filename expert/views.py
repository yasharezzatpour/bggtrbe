from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Expert,Resume,Collaboration,Tariff,ConnectToExpert
from .serializers import ExpertSerializer,ResumeSerializer,CollaborationSerializer,TariffSerializer,CennctToExpertSerializer


@api_view(['GET'])
def GetExpert(request , id):
    try:
        expert = Expert.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExpertSerializer(expert , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetTariffs(request , expert_id):
    try:
        tarrifs = Tariff.objects.filter(expert= expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TariffSerializer(tarrifs , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetCollaborations(request , expert_id):
    try:
        collaboratins = Collaboration.objects.filter(expert=expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CollaborationSerializer(collaboratins , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetResume(request , expert_id):
    try:
        resume = Resume.objects.filter(expert=expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ResumeSerializer(resume , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetConnectToExperts(request , expert_id):
    try:
        connectToExperts = ConnectToExpert.objects.filter(expert=expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CennctToExpertSerializer(connectToExperts , many= True)
    return Response(serializer.data)