from rest_framework import serializers

from .models import Story , StoryTypes , StoryLike

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class StoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryTypes
        fields = '__all__'

class StoryLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = '__all__'