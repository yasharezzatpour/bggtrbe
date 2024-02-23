from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Business , Comparison,Capital,Income,Growth,Staff ,UserBusinessInterests , BusinessTag , BusinessLike , BusinessComment , BusinessFollower
from .serializers import BusinessSerializer , ComparisonSerializer , IncomeSerializer ,GrowthSerializer , StaffSerializer , UserBusinessInterestSerializer ,BusinessFollowerSerializer
from .serializers import CapitalSerializer , BusinessLikeSerializer,BusinessCommentSerializer,BusinessTagSerializer
from rest_framework import status
from users.models import User
from .models import BusinessStaff, BusinessPartnerShip,ConnectToBusiness
from  .serializers import BusinessStaffSerializer, BusinessPartnerShipSerializer, ConnectToBusinessSerializer

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
def GetBusinesses ( request):
    try:
        businesses = Business.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
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
def GetBusinessFollowers(request  , id):
    try:
        businessFollowers = BusinessFollower.objects.filter(business = id).all()
    except:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessFollowerSerializer(businessFollowers , many = True)
    return Response(serializer.data)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteBusienssFollower(request , id):
    try:
        businessFollower = BusinessFollower.objects.filter(id = id).all()
        businessFollower.delete()
    except:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    return  Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostBusinessFollower(request):
    try:
        serializer = BusinessFollowerSerializer(data=request.data)
    except:
        return  Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_200_OK)

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

@api_view(['GET'])
def GetBusinessStaff(request , id):
    try:
        staff = BusinessStaff.objects.filter(business= id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessStaffSerializer(staff , many= True)
    return  Response(serializer.data)

@api_view(['GET'])
def GetBusinessPartnerShip(request , id):
    try:
        partnerShip = BusinessPartnerShip.objects.filter(business=id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BusinessPartnerShipSerializer(partnerShip , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetConnectToBusiness(request , id):
    try:
        connectToBusiness = ConnectToBusiness.objects.filter(business=id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ConnectToBusinessSerializer(connectToBusiness , many=True)
    return Response(serializer.data)