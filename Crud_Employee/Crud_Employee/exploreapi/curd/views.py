# profiles/views.py
from rest_framework import generics
from .models import PersonProfile
from .serializers import PersonProfileSerializer

class PersonProfileListCreateView(generics.ListCreateAPIView):
    """
    View to list all person profiles (GET) or create a new person profile (POST).
    """
    queryset = PersonProfile.objects.all()
    serializer_class = PersonProfileSerializer

class PersonProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve (GET), update (PUT/PATCH), or delete (DELETE) a specific person profile
    by its primary key (pk).
    """
    queryset = PersonProfile.objects.all()
    serializer_class = PersonProfileSerializer
    