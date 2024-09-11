from django.db import models
from django.contrib.auth.models import User
from karfarma.models import Offer


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

 

class Request(models.Model):
    date = models.DateField(auto_now_add=True)
    karjoo = models.ForeignKey(Karjoo, on_delete=models.PROTECT, related_name='requests')
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, related_name='requests')

    def __str__(self):
        return f"Request by {self.karjoo.user.username} for {self.offer.title}"


