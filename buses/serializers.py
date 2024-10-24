from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile  # Ou votre modèle CustomUser si vous l'utilisez
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES)  # Pour Profile
    admin_code = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'admin_code']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        # Créer le profil avec le rôle et le code admin si fourni
        profile = Profile.objects.create(
            user=user,
            role=validated_data.get('role', 'user')
        )
        
        if profile.role == 'admin':
            profile.admin_code = validated_data.get('admin_code')
            if not profile.admin_code or not profile.admin_code.endswith('ADM'):
                raise serializers.ValidationError('Le code admin doit se terminer par "ADM".')

        profile.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Identifiants invalides.')

        # Récupérer le profil de l'utilisateur
        profile = user.profile
        return {
            'username': user.username,
            'role': profile.role  # Retourner le rôle de l'utilisateur
        }
