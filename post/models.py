from django.db import models
from users.models import User
from business.models import Business
class UserPost(models.Model):
    created_by_user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_date_time = models.DateTimeField()
    caption = models.TextField( null= True , blank= True)
    url_to_media = models.CharField(max_length=255 , null= True , blank= True)
    video_or_image = models.CharField(max_length=10 , null= True , blank= True)

class BusinessPost(models.Model):
    created_by_business = models.ForeignKey(Business , on_delete= models.CASCADE)
    created_date_time = models.DateTimeField()
    caption = models.TextField(null= True , blank= True)
    url_to_media = models.CharField(max_length=255 , null= True , blank= True)
    video_or_image = models.CharField(max_length=10 , null= True , blank= True)

class BusinessPostComment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(BusinessPost , on_delete= models.CASCADE)
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField()

class BusinessPostLike(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    post = models.ForeignKey(BusinessPost , on_delete= models.CASCADE)
    business = models.ForeignKey(Business , on_delete= models.CASCADE)
