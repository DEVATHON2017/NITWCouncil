from django.db import models
from django.utils import timezone


class GrievancePost(models.Model):
    DEPARTMENT_CHOICES = (
        ('E', 'Electricity'),
        ('LAN', 'LAN'),
        ('H', 'Hostel'),
        ('A', 'Admin'),
    )
    complainant = models.ForeignKey('auth.User')
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, null=True)
    assigned_to = models.CharField(max_length = 10, null=True)
    heading = models.CharField(max_length=50)
    complaint = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    last_updated_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    def __str__(self):
        return self.heading

    def update(self):
        self.last_updated_date = timezone.now()
        self.save()
