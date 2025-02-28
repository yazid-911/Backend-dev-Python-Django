from django.shortcuts import render
from rest_framework import generics
from .models import Candidate, Recruiter
from .serializers import CandidateSerializer, RecruiterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
class CandidateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = "pk"


class RecruiterListCreate(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    
class RecruiterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    lookup_field = "pk"

class CandidateListForRecruiters(APIView):

    def get(self, request):
        candidates = Candidate.objects.all()  # Récupère tous les candidats
        serializer = CandidateSerializer(candidates, many=True)  # Sérialisation
        return Response(serializer.data)


    
