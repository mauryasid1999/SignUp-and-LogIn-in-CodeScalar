from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True)
    city=models.CharField(default='city',max_length=150,null=True)
    country=models.CharField(default='country',max_length=150,null=True)
    Institute=models.CharField(max_length=200,null=True)
   # email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile11.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name