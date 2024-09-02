from django.db import models
from django.contrib.auth.models import User
from karjoo.models import Karjoo




class Karfarma(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    address = models.TextField()
    company_description = models.TextField()



class Offer(models.Model):
    karfarma = models.ForeignKey(Karfarma ,on_delete = models.PROTECT)
    date = models.DateField()
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField()
    status = models.BooleanField()



class Request(models.Model):
    date = models.DateField()
    karjoo = models.ForeignKey(Karjoo ,on_delete=models.PROTECT)
    offer = models.ForeignKey(Offer , on_delete= models.PROTECT)


