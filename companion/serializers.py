from datetime import date
from rest_framework import serializers
from .models import Companions, Companion_Comments

class Companion_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companion_Comments
        fields = ('id', 'companion_post', 'comment_text', 'replies', 'parent_comment', 'user', 'user_nickname')

    user = serializers.IntegerField(source='user.id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        replies = Companion_Comments.objects.filter(parent_comment=obj.id)
        serializer = Companion_CommentSerializer(replies, many=True)
        return serializer.data
    
    def validate(self, data):
        parent_comment = data.get('parent_comment')
        companion_post = data.get('companion_post')

        if parent_comment and parent_comment.companion_post != companion_post:
            raise serializers.ValidationError("게시글의 주소가 올바르지 않습니다.")

        return data


class CompanionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companions
        fields = ('id', 'area', 'title', 'content', 'comments', 'start_date', 'end_date', 'views', 'age_tag', 'user_nickname', 'created_at', 'updated_at', 'total_recruits', 'current_recruits', 'status')

    comments = Companion_CommentSerializer(many=True, read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    views = serializers.ReadOnlyField()
    age_tag = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def validate(self, data):
        companion_recruits = data.get('companion_recruits')
        current_member = data.get('current_member')

        if companion_recruits < current_member:
            raise serializers.ValidationError("현재 인원이 모집 인원보다 많습니다.")
        if companion_recruits < 2:
            raise serializers.ValidationError("모집 인원은 2명 이상이어야 합니다.")
        if current_member < 1:
            raise serializers.ValidationError("현재 인원은 1명 이상이어야 합니다.")

        return data

    def get_status(self, obj):
        companion_recruits = obj.companion_recruits
        current_member = obj.current_member
        result = '모집완료' if companion_recruits == current_member else '모집중'
        return result

    @staticmethod
    def determine_age_group(age):
        if age < 20:
            return "10대이하"
        elif 20 <= age < 30:
            return "20대"
        elif 30 <= age < 40:
            return "30대"
        elif 40 <= age:
            return "40대이상"

    def get_age_tag(self, obj):
        birth_date = obj.user.birth
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_group = self.determine_age_group(age)
        return age_group

    # local_tag = serializers.SerializerMethodField()

    # def get_local_tag(self, obj):
    #     local = obj.owner.local
    #     return local

    # gender_tag = serializers.SerializerMethodField()

    # def get_gender_tag(self, obj):
    #     gender = obj.owner.gender
    #     return gender