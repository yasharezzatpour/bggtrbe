from django.db import models
from business.models import Business
from users.models import User


class Article (models.Model):
    title  = models.CharField(max_length=255)
    context = models.TextField()
    related_to_business_id = models.ForeignKey(Business , on_delete=models.CASCADE , null=True , blank=True)
    created_date_time = models.DateTimeField(editable=False)
    url_to_media = models.CharField(max_length=255 , null=True , blank=True)
    video_or_image = models.CharField(max_length=255)
    catagory = models.CharField(max_length=255 , default='all')


class ArticleComment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)





class ArticleLike(models.Model):
    article = models.ForeignKey(Article , on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)