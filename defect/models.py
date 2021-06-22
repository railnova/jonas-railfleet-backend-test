from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from defect.utils import poster
from defect.get_username import current_request

import asyncio

'''
This variable defines the URL of the endpoint to post updates about creation and delete to
'''
url_endpoint_deno = 'http://localhost:8888'


class Defect(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(blank=False, null=False, default=now)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    # Override user based on current request, then do the rest of the save
    def save(self, *args, **kwargs):
        req = current_request()
        self.user = req.user
        super(Defect, self).save(*args, **kwargs)


@receiver(post_save, sender=Defect)
def notify_deno_created(sender, instance, created, **kwargs):
    if created:
        data = {"user": instance.user.pk, "action": 'create'}
        poster(url=url_endpoint_deno, payload=data)


@receiver(post_delete, sender=Defect)
def notify_deno_deleted(sender, instance, **kwargs):
    data = {"user": instance.user.pk, "action": 'delete'}
    poster(url_endpoint_deno, data)
