from rest_framework import serializers
from .models import Candidate, Recruiter

# Serialiseur pour candidat qui permet de convertir des objets Django en données JSON
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__' 
        
# Serialiseur permet de convertir des objets Django (modèles) en données JSON
class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'