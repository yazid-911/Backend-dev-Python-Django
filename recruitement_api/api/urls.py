from django.urls import path
from .views import (
    CandidateListCreate,
    CandidateRetrieveUpdateDestroy,
    RecruiterListCreate,
    RecruiterRetrieveUpdateDestroy
)

urlpatterns = [
    path('candidates/', CandidateListCreate.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateRetrieveUpdateDestroy.as_view(), name='candidate-detail'),

    path('recruiters/', RecruiterListCreate.as_view(), name='recruiter-list-create'),
    path('recruiters/', CandidateListCreate.as_view(), name='recruiter-list-create'),
    path('recruiters/<int:pk>/', RecruiterRetrieveUpdateDestroy.as_view(), name='recruiter-detail'),
]