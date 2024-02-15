from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime
from rest_framework import status
from rest_framework.decorators import api_view

class RegisterView (APIView):
    def post (self , request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView (APIView):
    def post(self ,request):
        phone = request.data['phone']
        password = request.data['password']
        user = User.objects.filter(phone = phone).first()
        if user is None:
            raise AuthenticationFailed('کاربری با این شماره همراه وجود ندارد')
        if not user.check_password(password):
            raise AuthenticationFailed('رمز وارد شده اشتباه است')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload , 'secret' , algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt' , value = token , httponly=True )

        response.data = {
            'jwt': token
        }

        return response
class UserView (APIView):
    def get(self  , request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('UnAuthenticated')
        try:
            payload = jwt.decode(token , 'secret' , algorithms= ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('UnAuthenticated')
        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView (APIView):
    def post (self , request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }
        return response

@api_view(['GET'])
def GetUser(request , id):
    try:
        user = User.objects.filter(id = id).first()
    except:
        return  Response(status= status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)