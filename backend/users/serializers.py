from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentProfile, RecruiterProfile, PlacementCoordinatorProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = '__all__'

class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = RecruiterProfile
        fields = '__all__'
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import StudentProfile, RecruiterProfile

class RegisterStudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = StudentProfile
        fields = ['username', 'password', 'full_name', 'contact_number', 'resume', 'skills']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        student = StudentProfile.objects.create(user=user, **validated_data)
        return student

class RegisterRecruiterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = RecruiterProfile
        fields = ['username', 'password', 'company_name', 'contact_number']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        recruiter = RecruiterProfile.objects.create(user=user, **validated_data)
        return recruiter
from .models import StudentProfile, RecruiterProfile, CoordinatorProfile

from jobs.models import Job, Application
from interviews.models import Interview


User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type']

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfileSerializer
        fields = ['id', 'user', 'resume', 'skills', 'department']

# Recruiter Serializer
class RecruiterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = RecruiterProfileSerializer
        fields = ['id', 'user', 'company_name', 'position']

# Coordinator Serializer
class CoordinatorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PlacementCoordinatorProfile
        fields = ['id', 'user', 'department']

# Job Serializer
class JobSerializer(serializers.ModelSerializer):
    recruiter = RecruiterSerializer()

    class Meta:
        model = Job
        fields = ['id', 'recruiter', 'title', 'description', 'location', 'package', 'deadline']

# Application Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    job = JobSerializer()

    class Meta:
        model = Application
        fields = ['id', 'student', 'job', 'status']

# Interview Serializer
class InterviewSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer()

    class Meta:
        model = Interview
        fields = ['id', 'application', 'date', 'mode', 'result']
