from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from rest_framework import status
from .forms import TrajetForm
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializers import TrajetSerializer
from .serializers import BusSerializer
from .serializers import ConductSerializer
from .models import RelatBusTrajet
from .serializers import RelatBusTrajetSerializer
from .models import Trajet
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from .models import Bus
from .forms import  BusForm
from .models import Conduct
from .forms import  ConductForm 







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






@api_view(['POST'])
def create_bus_api(request):
    if request.method == 'POST':
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

@api_view(['GET'])
def bus_list(request):
    buss = Bus.objects.all()
    serializer = BusSerializer(buss, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_bus(request, pk):
    try:
        bus = Bus.objects.get(pk=pk)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BusSerializer(bus, data=request.data, partial=True)  # Utilisez `partial=True` pour permettre les mises à jour partielles
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_bus(request, pk):
    try:
        bus = Bus.objects.get(pk=pk)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    bus.delete()
    return Response({'message': 'Bus supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)



#Relation
# Liste et création de relations
class RelatBusTrajetListCreateView(generics.ListCreateAPIView):
    queryset = RelatBusTrajet.objects.all()
    serializer_class = RelatBusTrajetSerializer

    def create(self, request, *args, **kwargs):
        trajet_id = request.data.get('trajet')
        bus_id = request.data.get('bus')

        if not Trajet.objects.filter(idTrajet=trajet_id).exists():
            return Response({"error": "Trajet introuvable."}, status=status.HTTP_404_NOT_FOUND)

        if not Bus.objects.filter(idBus=bus_id).exists():
            return Response({"error": "Bus introuvable."}, status=status.HTTP_404_NOT_FOUND)

        relation = RelatBusTrajet(trajet_id=trajet_id, bus_id=bus_id)
        relation.save()

        serializer = self.get_serializer(relation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Récupération, mise à jour et suppression d'une relation
class RelatBusTrajetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RelatBusTrajet.objects.all()
    serializer_class = RelatBusTrajetSerializer






class RelatBusTrajetSearchView(APIView):
    def post(self, request, *args, **kwargs):
        point_depart = request.data.get('pointDepart')
        point_arrive = request.data.get('pointArrive')

        if not point_depart or not point_arrive:
            return Response({"error": "Les champs pointDepart et pointArrive sont requis."}, status=status.HTTP_400_BAD_REQUEST)

        # Recherchez les résultats correspondants
        relations = RelatBusTrajet.objects.filter(
            trajet__pointDepart=point_depart,
            trajet__pointArrive=point_arrive
        )

        # Sérialiser les données
        serializer = RelatBusTrajetSerializer(relations, many=True)
        
        # Inclure pointDepart et pointArrive dans la réponse
        response_data = {
            "pointDepart": point_depart,
            "pointArrive": point_arrive,
            "itineraries": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_200_OK)











#con
@api_view(['POST'])
def create_conduct_api(request):
    if request.method == 'POST':
        serializer = ConductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ConductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = ConductSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

@api_view(['GET'])
def conduct_list(request):
    conducts = Conduct.objects.all()
    serializer = ConductSerializer(conducts, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_conduct(request, pk):
    try:
        conduct = Conduct.objects.get(pk=pk)
    except Conduct.DoesNotExist:
        return Response({'error': 'Conducteur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ConductSerializer(conduct, data=request.data, partial=True)  # Utilisez `partial=True` pour permettre les mises à jour partielles
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_conduct(request, pk):
    try:
        conduct = Conduct.objects.get(pk=pk)
    except Conduct.DoesNotExist:
        return Response({'error': 'Conducteur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    conduct.delete()
    return Response({'message': 'Conducteur supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)





