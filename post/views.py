from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework import status


@api_view(['GET'])
def GetPost(request , id):

    try:
        post = Post.objects.filter(id = id).first()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post)
    return Response(serializer.data)