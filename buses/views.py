from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from rest_framework import status
from .forms import TrajetForm
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializers import TrajetSerializer
from .models import Trajet
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse








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

@api_view(['POST'])
def create_trajet_api(request):
    if request.method == 'POST':
        serializer = TrajetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TrajetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

@api_view(['GET'])
def trajet_list(request):
    trajets = Trajet.objects.all()
    serializer = TrajetSerializer(trajets, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_trajet(request, pk):
    try:
        trajet = Trajet.objects.get(pk=pk)
    except Trajet.DoesNotExist:
        return Response({'error': 'Trajet non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TrajetSerializer(trajet, data=request.data, partial=True)  # Utilisez `partial=True` pour permettre les mises à jour partielles
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_trajet(request, pk):
    try:
        trajet = Trajet.objects.get(pk=pk)
    except Trajet.DoesNotExist:
        return Response({'error': 'Trajet non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    trajet.delete()
    return Response({'message': 'Trajet supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)
