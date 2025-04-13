from django.shortcuts import render

from rest_framework import viewsets
from .models import JobPost
from .serializers import JobPostSerializer
from rest_framework.permissions import IsAuthenticated

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

