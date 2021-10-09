from django.db import models
from django.conf import settings
# Create your models here.


class Advertisements(models.Model):
    advertisement_title = models.CharField(max_length=1000)
    advertisement_subject = models.CharField(max_length=1000)
    advertisement_image = models.ImageField(
        upload_to=settings.MEDIA_ROOT)
