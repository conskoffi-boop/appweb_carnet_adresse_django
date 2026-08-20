from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User (AbstractUser):
    pass 


class Compte (models.Model):
    User = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    username= models.CharField(max_length=180)
    prenom = models.CharField(max_length=180)
    telephone = models.CharField(max_length=20,blank=True , null=True)
    email = models.EmailField()
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.prenom