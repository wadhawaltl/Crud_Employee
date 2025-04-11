# profiles/serializers.py
from rest_framework import serializers
from .models import PersonProfile  # Import your PersonProfile model

class PersonProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the PersonProfile model.
    """
    class Meta:
        model = PersonProfile
        fields = '__all__'  # Include all fields from the model
        # or explicitly list fields:
        # fields = ['id', 'name', 'domain', 'role', 'linkedin', 'instagram', 'email', 'github']