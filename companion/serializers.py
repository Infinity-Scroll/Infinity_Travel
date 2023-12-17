from rest_framework import serializers
from .models import Companion, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'companion_post', 'comment_text', 'replies')

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent_comment=obj)
        serializer = CommentSerializer(replies, many=True)
        return serializer.data


class CompanionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Companion
        fields = ('id', 'area', 'title', 'content', 'tags', 'comments', 'schedule_start', 'schedule_end', 'views')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        companion = Companion.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            companion.tags.add(*tag)
        return companion

    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     existing_tags = []

    #     for tag_data in tags_data:
    #         tag_name = tag_data['name']
    #         tag, created = Tag.objects.get_or_create(name=tag_name)
    #         existing_tags.append(tag)

    #     companion = Companion.objects.create(**validated_data)
    #     companion.tags.add(*existing_tags)
    #     return companion
