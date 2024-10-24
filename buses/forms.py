# buses/forms.py
from django import forms
from .models import Trajet

class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['pointDepart', 'pointArrive']  # Ajoutez les champs requis
