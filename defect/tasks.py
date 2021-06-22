import requests
import time

# from celery.decorators import task
from celery import shared_task


@shared_task
def celery_poster(url, payload):
    print("starting delayed post")
    response = requests.post(url, payload)
    print(response)
