from django.db import models
from django.contrib.auth.models import User


class Karfarma(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

class Offer(models.Model):
    karfarma = models.ForeignKey(Karfarma, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.karfarma.user.username}"


