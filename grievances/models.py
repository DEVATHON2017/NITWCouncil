from django.db import models
from django.utils import timezone


class GrievancePost(models.Model):
    complainant = models.ForeignKey('auth.User')
    #assigned_to = models.ForeignKey()
    heading = models.CharField(max_length=20)
    complaint = models.TextField()
    posted_date = models.DateTimeField(
            default=timezone.now)
    last_updated_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.heading

    def update(self):
        self.update_date = timezone.now()
        self.save()
