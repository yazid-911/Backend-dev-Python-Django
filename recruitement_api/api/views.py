from django.shortcuts import render
from rest_framework import generics
from .models import Candidate, Recruiter
from .serializers import CandidateSerializer, RecruiterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Récupère la liste des candidats, ajoute un nouveau candidat
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
   
# Récupère les détails d'un candidat,  Met à jour les informations et Supprime.
class CandidateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = "pk"

# Récupère la liste des recruteurs, ajoute un nouveau recruteur
class RecruiterListCreate(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
 
# Récupère les détails d'un recruteur, Met à jour les informations et supprime
class RecruiterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    lookup_field = "pk"

# Permet aux recruteurs de consulter la liste des candidat.
class CandidateListForRecruiters(APIView):

    def get(self, request):
        candidates = Candidate.objects.all() 
        serializer = CandidateSerializer(candidates, many=True) 
        return Response(serializer.data)


    
