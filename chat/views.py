from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Chat , Message,Member
from .serializers import ChatSerializer , MessageSerializer,MemberSerializer



@api_view(['GET'])
def GetChat(request , id):
    try:
        chat = Chat.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ChatSerializer(chat , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetMember(request , id):
    try:
        member = Member.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MemberSerializer(chat , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetMessage(request , id):
    try:
        message = Message.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MessageSerializer(chat , many=True)
    return Response(serializer.data)