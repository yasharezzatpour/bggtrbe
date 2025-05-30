from django.db import models
from users.models import User
from business.models import Business

class Expert(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255 , null=True , blank=True)
    rating = models.CharField(max_length=255 , null=True , blank= True)
    about = models.TextField(null=True , blank= True)
    blue_check = models.CharField(max_length=15 , default='false')
    url_to_image = models.CharField(max_length=255 , null= True , blank=True)


class ExpertTag(models.Model):
    name = models.CharField(max_length=255 )
    expert = models.ForeignKey(Expert , on_delete= models.CASCADE)

class UserInterestedExperts(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    expertTag = models.ForeignKey(ExpertTag , on_delete= models.CASCADE)

class ExpertLike (models.Model):
    expert = models.ForeignKey(Expert , on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)

class Resume(models.Model):
    expert = models.ForeignKey(Expert , on_delete=models.CASCADE)
    title = models.CharField(max_length=255 , null=True , blank=True)
    detail = models.TextField(null=True , blank= True)
    rating = models.CharField(max_length=255,null=True , blank= True)
    url_to_project_image = models.CharField(max_length=255 , null=True , blank=True)


class Collaboration(models.Model):
    expert = models.ForeignKey(Expert , on_delete=models.CASCADE)
    business = models.ForeignKey(Business , on_delete=models.CASCADE , null=True , blank=True)
    user = models.ForeignKey(User , on_delete= models.CASCADE , null= True , blank= True)

class Tariff(models.Model):
    expert = models.ForeignKey(Expert , on_delete=models.CASCADE)
    name = models.CharField(max_length=255 , null=True , blank= True)
    detail = models.TextField(null=True , blank=True)
    rating = models.CharField(max_length=255,null=True , blank=True)
    price = models.CharField(max_length=255 , null=True , blank=True)

class ConnectToExpert(models.Model):
    url = models.CharField(max_length=255)
    expert = models.ForeignKey(Expert , on_delete=models.CASCADE)
    name = models.CharField(max_length=255 , null=True , blank= True)
