from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField(blank=True, null=True)
    reason = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.preferred_date})"
