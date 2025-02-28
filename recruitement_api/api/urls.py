from django.urls import path
from .views import (
    CandidateListCreate,
    CandidateRetrieveUpdateDestroy,
    RecruiterListCreate,
    RecruiterRetrieveUpdateDestroy
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CandidateListForRecruiters

# Génère une vue Swagger pour l'API
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('candidates/', CandidateListCreate.as_view(), name='candidate-list-create'), # Permet de lister ou de créer des candidats.
    path('candidates/<int:pk>/', CandidateRetrieveUpdateDestroy.as_view(), name='candidate-detail'), #  Permet de récupérer, mettre à jour ou supprimer un recruteur spécifique.

    path('recruiters/', RecruiterListCreate.as_view(), name='recruiter-list-create'), # Permet de lister ou de créer des recruteurs.
    path('recruiters/<int:pk>/', RecruiterRetrieveUpdateDestroy.as_view(), name='recruiter-detail'), # Permet de récupérer, mettre à jour ou supprimer un recruteur spécifique.
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), #Affiche la documentation de l'API avec l'interface Swagger
    path('swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'), #Affiche la documentation de l'API avec l'interface ReDoc.
     path('recruiters/candidates/', CandidateListForRecruiters.as_view(), name='recruiters-candidates-list'), #Permet de récupérer, mettre à jour ou supprimer un recruteur spécifique.

]
