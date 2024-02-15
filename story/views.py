from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Story ,StoryTypes , StoryLike
from .serializers import StorySerializer , StoryTypeSerializer , StoryLikeSerializer
from rest_framework import status

@api_view(['GET'])
def GetStory(request , id):
    try:
        stories = Story.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StorySerializer(stories , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetStories(request , story_type_id):
    try:
        stories = Story.objects.filter(story_type_id = story_type_id).all()
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = StorySerializer(stories , many= True)
    return Response(serializer.data)

@api_view(['GET'])
def GetStoryTypes(request):
    try:
        storyTypes = StoryTypes.objects.all()
    except:
        return  Response(status= status.HTTP_404_NOT_FOUND)
    serializer = StoryTypeSerializer(storyTypes , many=True)
    return  Response(serializer.data)





@api_view(['POST'])
def PostStory(request , api_key , catagoty):
    
    try:
        api_key = request.GET['api_key']
        catagory = request.GET['catagory']
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if api_key == 1234:
        setializer = StorySerializer(data=request.data ,many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE'])
def DeleteStory (request , api_key , catagory):
    pass

def GetStoryLikes (request , story_id):
    try:
        storiyLikes = StoryLike.objects.filter(id = story_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StoryLikeSerializer(storiyLikes , many=True)
    return Response(serializer.data)