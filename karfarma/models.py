from django.db import models
from django.contrib.auth.models import User
from karjoo.models import Karjoo

class Karfarma(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.TextField()
    company_description = models.TextField()

    def __str__(self):
        return self.name

class Offer(models.Model):
    karfarma = models.ForeignKey(Karfarma, on_delete=models.PROTECT, related_name='offers')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.karfarma.name}"

class Request(models.Model):
    date = models.DateField(auto_now_add=True)
    karjoo = models.ForeignKey(Karjoo, on_delete=models.PROTECT, related_name='requests')
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, related_name='requests')

    def __str__(self):
        return f"Request by {self.karjoo} for {self.offer.title}"

