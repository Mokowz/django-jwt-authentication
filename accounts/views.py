from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from .models import CustomUser

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
  """
  Register a user after they put their details
  """
  queryset = CustomUser.objects.all()
  serializer_class = RegisterSerializer


class LogoutView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    refresh_token = request.data['refresh']
    token = RefreshToken(refresh_token)
    token.blacklist()

    return Response({
      "message": "User logged out successfully"
    })
