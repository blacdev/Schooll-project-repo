from .models import OffenderProfile
from rest_framework import serializers


class OffenderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffenderProfile
        fields = ('id', 'speed', 'is_speeding', 'image')
        read_only_fields = ('id',)
        