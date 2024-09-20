from rest_framework import serializers
from .models import *

class OneTimeAccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneTimeAccessToken
        fields = ['token', 'form_url', 'expiry', 'is_used']
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields='__all__'
