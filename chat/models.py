from django.db import models
from users.models import User

class Chat ( models.Model ):
    name = models.CharField(max_length=255 )
    descriiption = models.TextField(null=True , blank=True)
    photo = models.CharField(max_length=255 , null= True , blank= True)
    private = models.IntegerField()


class Message (models.Model):
    text = models.TextField()
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE)
    time = models.DateTimeField()


class Member(models.Model):
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)


