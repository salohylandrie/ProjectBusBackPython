# buses/models.py
from django.db import models

class Bus(models.Model):
    # Définitions des champs pour le modèle Bus
    numligne = models.CharField(max_length=100)
    capacite = models.IntegerField()

    def __str__(self):
        return self.numligne
