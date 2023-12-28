from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import User
from core.models import TimestampedModel, AreaModel

class LimitedURLField(models.URLField):
    def __init__(self, *args, **kwargs):
        self.max_urls = kwargs.pop('max_urls', 3)
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        urls = [url for url in model_instance.image_url if url]  # 값이 있는 URL만 필터링
        if len(urls) > self.max_urls:
            raise ValidationError(f"업로드 할 수 있는 URL의 최대치는 {self.max_urls}개 입니다.")


class Companions(TimestampedModel, AreaModel):
    STATUS_CHOICES = [
        ('모집중', '모집중'),
        ('모집완료', '모집완료'),
    ]
    TOTAL_RECRUITS_CHOICES = [
        ('총2명', '총2명'),
        ('총3명', '총3명'),
        ('총4명', '총4명'),
        ('총5명', '총5명'),
        ('총6명', '총6명'),
        ('총7명', '총7명'),
        ('총8명', '총8명'),
        ('총9명', '총9명'),
        ('총10명이상', '총10명이상'),
    ]
    CURRENT_RECRUITS_CHOICES = [
        ('1명', '1명'),
        ('2명', '2명'),
        ('3명', '3명'),
        ('4명', '4명'),
        ('5명', '5명'),
        ('6명', '6명'),
        ('7명', '7명'),
        ('8명', '8명'),
        ('9명', '9명'),
        ('10명이상', '10명이상'),
    ]
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    views = models.IntegerField(default=0, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_recruits = models.CharField(max_length=10, choices=TOTAL_RECRUITS_CHOICES, default='총2명', blank=True)
    current_recruits = models.CharField(max_length=10, choices=CURRENT_RECRUITS_CHOICES, default='1명', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='모집중', blank=True)
    thumbnail_image_url = models.ImageField(upload_to="companion/image_url/", blank=True, null=True) # , default="기본 썸네일 URL")
    sub_image_url_a = models.ImageField(upload_to="companion/image_url/", blank=True, null=True)
    sub_image_url_b = models.ImageField(upload_to="companion/image_url/", blank=True, null=True)
    sub_image_url_c = models.ImageField(upload_to="companion/image_url/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def increase_views(self):
        self.views += 1
        self.save()
        
    class Meta:
        ordering = ['-created_at']


class Companion_Comments(models.Model):
    comment_text = models.TextField()
    parent_comment = models.ForeignKey('self', related_name='companion_replies', null=True, blank=True, on_delete=models.CASCADE)
    companion_post = models.ForeignKey(Companions, related_name='companion_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text