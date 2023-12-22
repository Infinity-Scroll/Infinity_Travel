from rest_framework import serializers
from .models import Places, Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['place','user','content', 'rating']

class PlaceSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Places
        fields = ['name', 'description', 'address', 'category', 'contact', 'website', 'image_url', 'latitude', 'longitude', 'rating']