from rest_framework import serializers
from api.models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "nom"]
        model = Region


class DepartementSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='region.nom', read_only=True)

    class Meta:
        fields = ["id", "nom", "region"]
        model = Departement


class CommuneSerializer(serializers.ModelSerializer):
    departement = serializers.CharField(source='departement.nom',
                                        read_only=True)
    region = serializers.CharField(source='departement.region.nom',
                                   read_only=True)
    quartiers = serializers.JSONField(read_only=True)

    class Meta:
        fields = ["id", "nom", "departement", "region", "quartiers"]
        model = Commune


class QuartierSerializer(serializers.HyperlinkedModelSerializer):
    commune = serializers.CharField(source='commune.nom', read_only=True)

    class Meta:
        fields = '__all__'
        model = Quartier
