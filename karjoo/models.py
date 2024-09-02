from django.db import models
from django.contrib.auth.models import User



class Karjoo(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    


class Resume(models.Model):
    karjoo = models.OneToOneField(Karjoo , on_delete=models.PROTECT)
    gender = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    grades = models.CharField(max_length=20)
    work_filed = models.CharField(max_length=20)
    work_experience = models.CharField(max_length=20)




