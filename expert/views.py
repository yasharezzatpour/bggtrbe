from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Expert,Resume,Collaboration,Tariff,ConnectToExpert , ExpertTag , UserInterestedExperts , ExpertLike
from .serializers import ExpertSerializer,ResumeSerializer,CollaborationSerializer,TariffSerializer,CennctToExpertSerializer
from .serializers import UserInterestedExpertsSerializer , ExpertTagSerializer , ExpertLikeSerializer

@api_view(['GET'])
def GetExpert(request , id):
    try:
        expert = Expert.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExpertSerializer(expert , many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserInterestedExperts(request):
    try:
        limit = request.GET['limit'],
        user = request.user

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        userInterests = user.userinterestedexperts_set.all()
        expertTags = ExpertTag.objects.filter(userinterestedexperts__in=userInterests).all()
        experts = Expert.objects.filter(experttag__in = expertTags).all()
    except:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    serializer = ExpertSerializer(experts , many= True)
    return  Response(serializer.data)
@api_view(['GET'])
def GetExpertLikesCount(request , id):
    try:
        expertLikes = ExpertLike.objects.filter(expert= id).all()
    except :
        return  Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExpertLikeSerializer(expertLikes , many= True)
    return  Response(serializer.data.__len__())


@api_view(['GET'])
def GetTariffs(request , expert_id):
    try:
        tarrifs = Tariff.objects.filter(expert= expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TariffSerializer(tarrifs , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetCollaborationsCount(request , expert_id):
    try:
        collaboratins = Collaboration.objects.filter(expert=expert_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CollaborationSerializer(collaboratins , many=True)
    return Response(serializer.data.__len__())

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