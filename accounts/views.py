from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


# class LoginView(APIView):

#   def post(self, request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     user = authenticate(email=email, password=password)
#     refresh = RefreshToken.for_user(user)

#     tokens = {
#       "access": str(refresh),
#       "refresh": str(refresh.access_token),
#     }

#     return Response(tokens)

