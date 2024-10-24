from django.db import models
from django.contrib.auth.models import User





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    admin_code = models.CharField(max_length=10, blank=True, null=True)  # Code pour les admins



class Trajet(models.Model):
    idTrajet = models.AutoField(primary_key=True)
    pointDepart = models.CharField(max_length=100)
    pointArrive = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pointDepart} - {self.pointArrive}"
    
    
