from django.http.response import ResponseHeaders
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND



# Create your views here.

class RegisterAPIVIEW(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        User.objects.create_user(username=username, password=password)
        return Response(data={'message':'user saved'})
    
class LoginAPIView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        if user:
            try: 
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token':token.key})
        return Response(status=status.HTTP_404_NOT_FOUND)


