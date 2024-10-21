from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.exceptions import ValidationError

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extraction des données valides
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Authentification de l'utilisateur
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Connexion réussie
            return Response({"message": "Connexion réussie"}, status=status.HTTP_200_OK)
        else:
            # Échec de la connexion
            return Response({"message": "Nom d'utilisateur ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Vérification si l'utilisateur existe déjà
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({"message": "Un utilisateur avec ce nom d'utilisateur existe déjà."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Tentative d'inscription
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"message": "Inscription réussie"}, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            # Gestion des erreurs de validation
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Gestion des erreurs générales
            return Response({"message": "Une erreur est survenue lors de l'inscription. Veuillez réessayer."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
