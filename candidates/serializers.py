from rest_framework import serializers
from .models import Candidate
import re

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive integer.")
        return value

    def validate_phone_number(self, value):
        """
        Validates the phone number using a regex pattern.
        """
        pattern = r'^\+?1?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Phone number must be in a valid format.")
        return value