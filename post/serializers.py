from rest_framework import serializers
from .models import UserPost ,  BusinessPost , BusinessPostComment , BusinessPostLike


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'

class BusinessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPost
        fields = '__all__'

class BusinessPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPostComment
        fields = '__all__'

class BusinessPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPostLike
        fields = '__all__'