from django.contrib.auth.models import AbstractUser
from django.db import models

# User roles
USER_ROLES = (
    ('student', 'Student'),
    ('recruiter', 'Recruiter'),
    ('coordinator', 'Coordinator'),
)

# Custom User Model
class User(AbstractUser):
    role = models.CharField(max_length=20, choices=USER_ROLES)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email', 'role']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.role})"


# Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    year = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    skills = models.TextField(help_text='Comma-separated skills', blank=True)

    def __str__(self):
        return self.full_name


# Recruiter Profile
class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


# Coordinator Profile
class CoordinatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coordinator_profile')
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

# Placement Coordinate Profile
class PlacementCoordinatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add other fields
