from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile  # Ou votre modèle CustomUser si vous l'utilisez
from django.contrib.auth import authenticate
from .models import Trajet
from .models import Bus
from .models import Conduct
from .models import RelatBusTrajet

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Profile

User = get_user_model()

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_admin = serializers.BooleanField(write_only=True, default=False)  # Ajout d'un champ pour déterminer si c'est un admin

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin']

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin', False)  # Retirer le champ is_admin des données validées

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        # Créer le profil, avec "admin" si is_admin est vrai, sinon sans rôle
        profile = Profile.objects.create(
            user=user,
            role='admin' if is_admin else None  # Attribuer 'admin' si c'est un admin
        )

        profile.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authentification de l'utilisateur
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Identifiants invalides.')

        # Récupérer le profil de l'utilisateur
        profile = user.profile

        # Retourner le nom d'utilisateur et le rôle (ou None si c'est un utilisateur simple)
        return {
            'username': user.username,
            'role': profile.role if profile.role else None  # Renvoie None si le rôle est vide
        }



class TrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajet
        fields = ['idTrajet', 'pointDepart', 'pointArrive']

    def create(self, validated_data):
        # Crée un nouvel objet Trajet à partir des données validées
        trajet = Trajet.objects.create(**validated_data)
        return trajet

    def update(self, instance, validated_data):
        # Met à jour l'objet Trajet existant
        instance.pointDepart = validated_data.get('pointDepart', instance.pointDepart)
        instance.pointArrive = validated_data.get('pointArrive', instance.pointArrive)
        instance.save()
        return instance 
    

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['idBus', 'numLigne']

    def create(self, validated_data):
        # Crée un nouvel objet Trajet à partir des données validées
        bus = Bus.objects.create(**validated_data)
        return bus

    def update(self, instance, validated_data):
        # Met à jour l'objet Trajet existant
        instance.numLigne = validated_data.get('numLigne', instance.numLigne)
        instance.save()
        return instance     
    
class ConductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conduct
        fields = ['idConduct', 'nomConduct', 'prenomConduct', 'emailConduct']

    def create(self, validated_data):
        # Crée un nouvel objet Trajet à partir des données validées
        conduct = Conduct.objects.create(**validated_data)
        return conduct

    def update(self, instance, validated_data):
        # Met à jour l'objet Trajet existant
        instance.nomConduct = validated_data.get('nomConduct', instance.nomConduct)
        instance.prenomConduct = validated_data.get('prenomConduct', instance.prenomConduct)
        instance.emailConduct = validated_data.get('emailConduct', instance.emailConduct)
        instance.save()
        return instance        
    

#Relation 
class RelatBusTrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatBusTrajet
        fields = ['id', 'trajet', 'bus']   