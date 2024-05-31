from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Home(APIView):

  def get(self, request):
    users = [
      "Ronny",
      "Lala",
      "Mike"
    ]

    return Response(users)