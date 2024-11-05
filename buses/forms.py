# buses/forms.py
from django import forms
from .models import Trajet
from .models import Bus
from .models import Conduct

class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['pointDepart', 'pointArrive']  # Ajoutez les champs requis


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['numLigne']  # Ajoutez les champs requis

class ConductForm(forms.ModelForm):
    class Meta:
        model = Conduct
        fields = ['nomConduct', 'emailConduct', 'prenomConduct']  # Ajoutez les champs requis        