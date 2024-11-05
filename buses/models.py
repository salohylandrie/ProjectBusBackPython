from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Le champ role peut être un CharField mais il est optionnel
    role = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.role or "User"}'



class Trajet(models.Model):
    idTrajet = models.AutoField(primary_key=True)
    pointDepart = models.CharField(max_length=100)
    pointArrive = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pointDepart} - {self.pointArrive}"
    

class Bus(models.Model):
    idBus = models.AutoField(primary_key=True)
    numLigne = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.numLigne}"   
    
class RelatBusTrajet(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trajet: {self.trajet} - Bus: {self.bus}"  


#Relation
class RelatBusTrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatBusTrajet
        fields = ['id', 'trajet', 'bus']














    
    
class Conduct(models.Model):
    idConduct = models.AutoField(primary_key=True)
    nomConduct = models.CharField(max_length=100)
    prenomConduct = models.CharField(max_length=100)
    emailConduct = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.nomConduct} - {self.prenomConduct} - {self.emailConduct}"       
