from django.db import models
from users.models import User






class StoryTypes(models.Model):
    name = models.CharField(max_length=255 )
    url_to_image = models.CharField(max_length=255)
class Story (models.Model):
    auther = models.ForeignKey(User , on_delete= models.CASCADE )
    catagory = models.CharField(max_length=255 , default= 'all')
    #zero for not private and one for private
    private = models.IntegerField()
    time = models.TimeField()
    url = models.CharField(max_length=255)
    urlToImage = models.CharField(max_length=255)
    story_type = models.ForeignKey(StoryTypes , on_delete=models.CASCADE)

class StoryLike (models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    story = models.ForeignKey(Story , on_delete = models.CASCADE)

