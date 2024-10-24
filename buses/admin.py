# buses/admin.py
from django.contrib import admin
from .models import Trajet

class TrajetAdmin(admin.ModelAdmin):
    list_display = ('idTrajet', 'pointDepart', 'pointArrive')  # Afficher ces champs dans la liste
    search_fields = ('pointDepart', 'pointArrive')  # Permettre la recherche sur ces champs

admin.site.register(Trajet, TrajetAdmin)
