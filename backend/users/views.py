from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .models import StudentProfile, RecruiterProfile
from .serializers import StudentProfileSerializer, RecruiterProfileSerializer
from rest_framework.permissions import IsAuthenticated

class StudentList(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

class RecruiterList(generics.ListAPIView):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import generics
from .serializers import RegisterStudentSerializer, RegisterRecruiterSerializer

class RegisterStudentView(generics.CreateAPIView):
    serializer_class = RegisterStudentSerializer

class RegisterRecruiterView(generics.CreateAPIView):
    serializer_class = RegisterRecruiterSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Student, Recruiter, Coordinator, Job, Application, Interview
from .serializers import (
    UserSerializer,
    StudentSerializer,
    RecruiterSerializer,
    CoordinatorSerializer,
    JobSerializer,
    ApplicationSerializer,
    InterviewSerializer
)

User = get_user_model()

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # You can change this later for better security

# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Recruiter ViewSet
class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = [permissions.IsAuthenticated]

# Coordinator ViewSet
class CoordinatorViewSet(viewsets.ModelViewSet):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Job ViewSet
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

# Application ViewSet
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

# Interview ViewSet
class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            if User.objects.filter(username=data['username']).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(email=data['email']).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                username=data['username'],
                email=data['email'],
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                password=make_password(data['password'])  # Hash password!
            )

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    user.first_name = request.data.get('first_name', user.first_name)
    user.last_name = request.data.get('last_name', user.last_name)
    user.save()

    return Response({'message': 'Profile updated successfully.'})
# views.py

from .models import Job, Application
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_list(request):
    jobs = Job.objects.all()
    data = [
        {
            'id': job.id,
            'title': job.title,
            'company_name': job.company_name,
            'description': job.description,
            'location': job.location,
            'salary': job.salary,
        }
        for job in jobs
    ]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    Application.objects.create(student=request.user, job=job)
    return Response({'message': 'Applied successfully.'})
