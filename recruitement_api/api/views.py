from django.shortcuts import render
from rest_framework import generics
from .models import Candidate, Recruiter
from .serializers import CandidateSerializer, RecruiterSerializer

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
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
class RecruiterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    lookup_field = "pk"
