from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Business , Comparison,Capital,Income,Growth,Staff ,UserBusinessInterests , BusinessTag , BusinessLike , BusinessComment
from .serializers import BusinessSerializer , ComparisonSerializer , IncomeSerializer ,GrowthSerializer , StaffSerializer , UserBusinessInterestSerializer
from .serializers import CapitalSerializer , BusinessLikeSerializer,BusinessCommentSerializer,BusinessTagSerializer
from rest_framework import status
from users.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetBusiness(request , id):
    try:
        business = Business.objects.filter(id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessSerializer(business , many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserBusiness(request , owner_id):
    print(owner_id)
    try:

        business = Business.objects.filter(owner = owner_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessSerializer(business , many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetBusinesses ( request):
    try:
        limit = request.GET['limit']
        catagory = request.GET['catagory']
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        businesses = Business.objects.filter(catagory=catagory).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if businesses.count() >= int(limit):
        businesses = businesses[0:int(limit)]
    else:
        businesses = businesses[0:businesses.count()]
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserBusinessInterests(request , user_id):
    try:
        userBusinessInterests = UserBusinessInterests.objects.filter(user = user_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserBusinessInterestSerializer(userBusinessInterests , many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserInterestedBusinesses(request):
    try:
        limit = request.GET['limit'],
        user = request.user

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        userInterests = user.userbusinessinterests_set.all()
        businessTags = BusinessTag.objects.filter(userbusinessinterests__in = userInterests).all()
        businesses = Business.objects.filter(businesstag__in = businessTags).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer  = BusinessSerializer(businesses , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetCapital (request ,id):
    try:
        capital = Capital.objects.filter(for_business_id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CapitalSerializer(capital , many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetIncome (request ,id):
    try:
        income = Income.objects.filter(for_business_id= id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IncomeSerializer(income , many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetGrowth (request ,id):
    try:
        growth = Growth.objects.filter(for_business_id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GrowthSerializer(growth , many=True)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetStaff (request ,id):
    try:
        staff = Staff.objects.filter(for_business_id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StaffSerializer(staff , many=True)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetComparison (request ,id):
    try:
        comparison = Comparison.objects.filter(for_business_id = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ComparisonSerializer(comparison , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBusinessLikes(request , id):
    try:
        businessLikes = BusinessLike.objects.filter(business = id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessLikeSerializer(businessLikes , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetBusinessComments(request , id):
    try:
        businessComments = BusinessComment.objects.filter(business= id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessCommentSerializer(businessComments , many= True)
    return  Response(serializer.data)

@api_view(['GET'])
def GetBusinessTags(request , id):
    try:
        businessTags = BusinessTag.objects.filter(business=id).all()
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = BusinessTagSerializer(businessTags , many= True)
    return  Response(serializer.data)
