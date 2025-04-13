from django.db import models
from users.models import RecruiterProfile

JOB_TYPES = (
    ('full_time', 'Full Time'),
    ('internship', 'Internship'),
    ('part_time', 'Part Time'),
)

class JobPost(models.Model):
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField(help_text='Comma-separated required skills', blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.title} at {self.recruiter.company_name}"
