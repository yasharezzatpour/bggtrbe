from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=255 , null=True , blank=True)
    url_to_image = models.CharField(max_length=255)
    description = models.TextField(null=True , blank= True)
    category = models.CharField(max_length=255)

