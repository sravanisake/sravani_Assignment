from rest_framework import serializers

from app.models import *
class countryMS(serializers.ModelSerializer):
    class Meta:
        model=country
        fields="__all__"