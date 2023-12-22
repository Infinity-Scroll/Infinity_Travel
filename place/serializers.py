from rest_framework import serializers
from .models import Places, Place_comments
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user_image_url = serializers.ImageField(source='user.profile.image_url', read_only=True)
    user_name = serializers.CharField(source='user.profile.name', read_only=True)

    class Meta:
        model = Place_comments
        fields = ['place', 'user', 'content', 'rating', 'user_image_url', 'user_name']

class PlaceSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Places
        fields = ['name', 'description', 'address', 'category', 'contact', 'website', 'image_url', 'latitude', 'longitude', 'rating','comments']