from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from rest_framework import status



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'message': 'Connexion réussie',
                'role': serializer.validated_data['role']
            })
        return Response(serializer.errors, status=400)
    
    
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Utilisateur enregistré avec succès!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
