# profiles/urls.py
from django.urls import path
from .views import PersonProfileListCreateView, PersonProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('person-profiles/', PersonProfileListCreateView.as_view(), name='person-profile-list-create'),
    path('person-profiles/<int:pk>/', PersonProfileRetrieveUpdateDestroyView.as_view(), name='person-profile-detail'),
]