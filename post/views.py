from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserPost , BusinessPost , BusinessPostComment, BusinessPostLike
from .serializers import UserPostSerializer , BusinessPostSerializer , BusinessPostCommentSerializer,BusinessPostLikeSerializer
from rest_framework import status


@api_view(['GET'])
def GetUserPost(request , id):
    try:
        post = UserPost.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def GetUserPosts(request ):
    try:
        post = UserPost.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserPostSerializer(post , many= True)
    return Response(serializer.data)
@api_view(['GET'])
def GetBusinessPost(request , id):
    try:
        post = BusinessPost.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessPostSerializer(post , many= True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBusinessPosts(requset ):
    try:
        post = BusinessPost.objects.all()
    except:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessPostSerializer(post , many= True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBusinessPostComments(request , id):
    try:
        postComments = BusinessPostComment.objects.filter(id=id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessPostCommentSerializer(postComments , many = True)
    return  Response(serializer.data)
@api_view(['GET'])
def GetBsuinessPostLikes(request , id):
    try:
        postLikes = BusinessPostLike.objects.filter(business=id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessPostLikeSerializer(postLikes , many= True)
    return Response(serializer.data)

