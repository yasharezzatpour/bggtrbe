from .models import Expert,ConnectToExpert,Collaboration,Resume,Tariff

from rest_framework import serializers


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = '__all__'

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'

class CennctToExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectToExpert
        fields = '__all__'
