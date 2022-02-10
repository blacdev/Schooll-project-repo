from .models import OffenderProfile
from rest_framework import serializers


class OffenderProfileSerializer(serializers.ModelSerializer):
    frontend_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = OffenderProfile
        fields = ('id', 'speed', 'is_speeding', 'image', 'frontend_url')
        read_only_fields = ('id',)
    
    def get_frontend_url(self, obj):
        # get absolute url to offender frontend detail page
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_absolute_url())
        