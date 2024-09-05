from django.db import models
from django.contrib.auth.models import User



class Karjoo(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    


class Resume(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    GRADE_CHOICES = [
        ('HS', 'High School'),
        ('BA', 'Bachelors'),
        ('MA', 'Masters'),
        ('PhD', 'Doctorate'),
    ]
    karjoo = models.OneToOneField(Karjoo , on_delete=models.PROTECT)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    description = models.TextField()
    grades = models.CharField(max_length=20, choices=GRADE_CHOICES)
    work_filed = models.CharField(max_length=20)
    work_experience = models.CharField(max_length=20)




