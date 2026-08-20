from django.db import models
from gestion_user.models import User 
# Create your models here.


######### le models contact ##############
# Nom, prenom
# Telephone
# Email
# Notes / commentaires
# Photo (optionnel)
# Date de creation / derniere modification


class Contact(models.Model):
    user = models.ForeignKey( User ,null=True,blank=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=180)
    prenom=models.CharField(max_length=200 , null=True,blank=True)
    telephone=models.CharField(max_length=20)
    email = models.EmailField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    date_creation = models.DateField(auto_now_add=True)
    derniere_modification = models.DateField(auto_now=True)
    adresse = models.CharField(max_length=300,null=True,blank=True)



    def __str__(self):
        return self.nom


