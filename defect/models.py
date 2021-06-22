from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Defect(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(blank=False, null=False, default=now)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    # Override user based on current request, then do the rest of the save
    def save(self, *args, **kwargs):
        req = current_request()
        self.user = req.user
        super(Defect, self).save(*args, **kwargs)

