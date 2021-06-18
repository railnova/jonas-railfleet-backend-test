from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Defect(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(blank=False, null=False, default=now)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
