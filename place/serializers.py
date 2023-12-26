from rest_framework import serializers
from .models import Places, Place_comments
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user_image_url = serializers.ImageField(source='user.profile.image_url', read_only=True)
    user_name = serializers.CharField(source='user.profile.name', read_only=True)

    class Meta:
        model = Place_comments
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Places
        fields = '__all__'