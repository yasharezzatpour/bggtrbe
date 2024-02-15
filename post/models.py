from django.db import models
from users.models import User
class Post(models.Model):
    created_by_user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_date_time = models.DateTimeField()
    caption = models.TextField()
    url_to_media = models.CharField(max_length=255)
    video_or_image = models.CharField(max_length=10)