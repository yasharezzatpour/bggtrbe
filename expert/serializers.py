from .models import Expert,ConnectToExpert,Collaboration,Resume,Tariff , ExpertTag , UserInterestedExperts , ExpertLike

from rest_framework import serializers


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'

class ExpertTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertTag
        fields = '__all__'

class UserInterestedExpertsSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserInterestedExperts
        fields = '__all__'

class ExpertLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertLike
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
