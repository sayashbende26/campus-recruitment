from django.db import models
from users.models import StudentProfile
from jobs.models import JobPost

APPLICATION_STATUS = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)

class Application(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='applications')
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='applications/resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='pending')

    def __str__(self):
        return f"{self.student.full_name} - {self.job_post.title}"
