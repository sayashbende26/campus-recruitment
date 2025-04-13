from django.shortcuts import render

from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

from users.models import StudentProfile
from jobs.models import JobPost
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def resume_filter(request, job_id):
    job = JobPost.objects.get(id=job_id)
    required_skills = set(skill.strip().lower() for skill in job.required_skills.split(','))

    students = StudentProfile.objects.all()
    matching_students = []

    for student in students:
        student_skills = set(skill.strip().lower() for skill in student.skills.split(','))
        if required_skills & student_skills:
            matching_students.append({
                "id": student.id,
                "full_name": student.full_name,
                "skills": student.skills,
            })

    return Response(matching_students)
