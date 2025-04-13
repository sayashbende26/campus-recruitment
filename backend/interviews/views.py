from django.shortcuts import render

from rest_framework import viewsets
from .models import Interview
from .serializers import InterviewSerializer
from rest_framework.permissions import IsAuthenticated

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]

