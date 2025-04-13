from django.db import models
from applications.models import Application

INTERVIEW_STATUS = (
    ('scheduled', 'Scheduled'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)

class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interviews')
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=INTERVIEW_STATUS, default='scheduled')
    meeting_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Interview for {self.application.student.full_name} - {self.application.job_post.title}"
