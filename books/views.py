from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  permission_classes = [IsAuthenticated]
  serializer_class = BookSerializer